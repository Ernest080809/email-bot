"""
image_generator.py
------------------
Handles the optional "try-it-on" feature.

Flow:
  1. User uploads their photo.
  2. We build a detailed outfit description from the top recommended product.
  3. We call the Replicate virtual-try-on / outfit-generation API.
  4. We return the generated image URL.

If REPLICATE_API_TOKEN is not set, the module returns a graceful "not available"
response instead of crashing so the rest of the system keeps working.

Replicate model used:
  cuuupid/virtual-try-on  (or idm-vton) – state-of-the-art garment transfer.
  Falls back to prompt-based SDXL generation if the try-on model is unavailable.
"""

import os
import time
import base64
import httpx
from anthropic import Anthropic

REPLICATE_TOKEN = os.getenv("REPLICATE_API_TOKEN", "")
REPLICATE_API = "https://api.replicate.com/v1"

anthropic_client = Anthropic()


# ---------------------------------------------------------------------------
# Outfit description builder (uses Claude to generate a rich text prompt)
# ---------------------------------------------------------------------------

def _build_outfit_prompt(recommendation: dict, style_profile: str) -> str:
    """
    Use Claude to turn a product recommendation into a detailed visual prompt
    suitable for an image generation model.
    """
    product_name = recommendation.get("product_name", "vintage outfit")
    why_for_you = recommendation.get("why_for_you", "")
    tags = ", ".join(recommendation.get("style_tags", []))

    response = anthropic_client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Product: {product_name}\n"
                    f"Style tags: {tags}\n"
                    f"Stylist note: {why_for_you}\n"
                    f"Customer style profile: {style_profile}\n\n"
                    "Write a concise, vivid image-generation prompt (under 120 words) "
                    "describing a full-body fashion photo of a person wearing this outfit. "
                    "Include fabric textures, colours, fit, and the overall mood. "
                    "Do not include any brand names, faces, or identifiable features. "
                    "Return only the prompt text, no preamble."
                ),
            }
        ],
    )
    return response.content[0].text.strip()


# ---------------------------------------------------------------------------
# Replicate helpers
# ---------------------------------------------------------------------------

def _replicate_predict(model: str, input_data: dict, timeout: int = 120) -> str | None:
    """
    Submits a prediction to Replicate and polls until completion.
    Returns the output URL string, or None on failure.
    """
    headers = {
        "Authorization": f"Token {REPLICATE_TOKEN}",
        "Content-Type": "application/json",
    }
    with httpx.Client(timeout=30) as http:
        # Create prediction
        resp = http.post(
            f"{REPLICATE_API}/predictions",
            headers=headers,
            json={"version": model, "input": input_data},
        )
        if resp.status_code not in (200, 201):
            return None
        prediction = resp.json()
        prediction_id = prediction.get("id")
        if not prediction_id:
            return None

        # Poll
        deadline = time.time() + timeout
        while time.time() < deadline:
            time.sleep(3)
            poll = http.get(
                f"{REPLICATE_API}/predictions/{prediction_id}",
                headers=headers,
            )
            data = poll.json()
            status = data.get("status")
            if status == "succeeded":
                output = data.get("output")
                if isinstance(output, list):
                    return output[0]
                return output
            if status in ("failed", "canceled"):
                return None
    return None


def _encode_image(image_bytes: bytes) -> str:
    """Return a data URI for the image."""
    return "data:image/jpeg;base64," + base64.b64encode(image_bytes).decode()


# ---------------------------------------------------------------------------
# Virtual try-on (IDM-VTON on Replicate)
# ---------------------------------------------------------------------------

# Latest public IDM-VTON version on Replicate (update if needed)
_VTON_MODEL = (
    "cuuupid/idm-vton:"
    "906425dbca90663ff5427624839572cc56ea7d380343d13e2a4c4b09d7f6a07"
)

def _try_on(user_photo_bytes: bytes, garment_image_url: str, product_name: str) -> str | None:
    """
    Attempt a virtual try-on using IDM-VTON on Replicate.
    Returns image URL on success, None on failure.
    """
    human_b64 = _encode_image(user_photo_bytes)
    input_data = {
        "human_img": human_b64,
        "garm_img": garment_image_url,
        "garment_des": product_name,
        "is_checked": True,
        "is_checked_crop": False,
        "denoise_steps": 30,
        "seed": 42,
    }
    return _replicate_predict(_VTON_MODEL, input_data)


# ---------------------------------------------------------------------------
# Prompt-based outfit generation fallback (SDXL)
# ---------------------------------------------------------------------------

_SDXL_MODEL = (
    "stability-ai/sdxl:"
    "7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc"
)

def _generate_outfit_image(outfit_prompt: str) -> str | None:
    """
    Generate an outfit image from a text prompt using SDXL.
    """
    input_data = {
        "prompt": outfit_prompt + ", full body shot, fashion editorial, soft natural lighting",
        "negative_prompt": "face, portrait, ugly, blurry, watermark, text",
        "width": 768,
        "height": 1024,
        "num_inference_steps": 30,
    }
    return _replicate_predict(_SDXL_MODEL, input_data)


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def generate_outfit_image(
    user_photo_bytes: bytes | None,
    top_recommendation: dict,
    style_profile: str,
) -> dict:
    """
    Main entry point.

    Parameters
    ----------
    user_photo_bytes   : raw bytes of the uploaded photo, or None
    top_recommendation : first item from recommendations list
    style_profile      : customer style profile string

    Returns
    -------
    {
        "success": bool,
        "image_url": "url or empty string",
        "method": "virtual_try_on | generated | unavailable",
        "message": "human-readable status"
    }
    """
    if not REPLICATE_TOKEN:
        return {
            "success": False,
            "image_url": "",
            "method": "unavailable",
            "message": (
                "Image generation is not configured. "
                "Set REPLICATE_API_TOKEN in your .env file to enable this feature."
            ),
        }

    garment_url = top_recommendation.get("product_image", "")

    # 1. Try virtual try-on if we have both a photo and a garment image
    if user_photo_bytes and garment_url:
        result_url = _try_on(user_photo_bytes, garment_url, top_recommendation.get("product_name", ""))
        if result_url:
            return {
                "success": True,
                "image_url": result_url,
                "method": "virtual_try_on",
                "message": "Here's how you might look wearing this piece.",
            }

    # 2. Fall back to prompt-based SDXL generation
    outfit_prompt = _build_outfit_prompt(top_recommendation, style_profile)
    result_url = _generate_outfit_image(outfit_prompt)
    if result_url:
        return {
            "success": True,
            "image_url": result_url,
            "method": "generated",
            "message": "Here's an AI-generated outfit inspiration based on your style.",
        }

    return {
        "success": False,
        "image_url": "",
        "method": "unavailable",
        "message": "Image generation failed. Please try again later.",
    }
