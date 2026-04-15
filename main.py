"""
main.py
-------
FastAPI application for the AI Vintage Stylist.

Two sets of endpoints
─────────────────────
1. Widget API  (/api/shop/*)   – called by the embeddable widget.js from
   Shopify stores.  Requires X-API-Key header.

2. Internal SPA (/api/*)       – called by the built-in test frontend
   (useful for development and demos).

3. Static serving
   GET  /widget.js  → serves the embeddable widget script
   GET  /           → serves the SPA test frontend
"""

import os
import time
import uuid
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException, Header, UploadFile, File, Form, Request
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from website_analyzer import analyze_website, analyze_shopify_store
from quiz_generator import generate_quiz
from recommendation_engine import get_recommendations
from image_generator import generate_outfit_image

# ---------------------------------------------------------------------------
# App + CORS
# ---------------------------------------------------------------------------

app = FastAPI(
    title="AI Vintage Stylist",
    description="Personalised style quiz and product recommendations for vintage fashion shops.",
    version="2.0.0",
)

# Allow requests from any Shopify store domain (and localhost for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # lock this down to specific domains in production
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

FRONTEND_DIR = Path(__file__).parent / "frontend"
WIDGET_PATH  = Path(__file__).parent / "widget.js"

# ---------------------------------------------------------------------------
# API key validation
# ---------------------------------------------------------------------------

# Comma-separated list in .env:  API_KEYS=key1,key2,key3
_VALID_KEYS: set[str] = {
    k.strip() for k in os.getenv("API_KEYS", "").split(",") if k.strip()
}


def _require_api_key(x_api_key: str | None) -> None:
    """Raise 401 if the key is missing or not in the allowed set."""
    if not _VALID_KEYS:
        # No keys configured → open access (dev mode)
        return
    if not x_api_key or x_api_key not in _VALID_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing API key.")


# ---------------------------------------------------------------------------
# Shop analysis cache  (in-memory, 24-hour TTL per domain)
# Swap for Redis in production for multi-process deployments.
# ---------------------------------------------------------------------------

_SHOP_CACHE: dict[str, dict] = {}   # domain → {"data": analysis_dict, "ts": float}
_CACHE_TTL  = 24 * 3600             # 24 hours


def _get_cached_analysis(domain: str) -> dict | None:
    entry = _SHOP_CACHE.get(domain)
    if entry and (time.time() - entry["ts"]) < _CACHE_TTL:
        return entry["data"]
    return None


def _set_cached_analysis(domain: str, data: dict) -> None:
    _SHOP_CACHE[domain] = {"data": data, "ts": time.time()}


# ---------------------------------------------------------------------------
# In-memory session store  (swap for Redis / DB in production)
# ---------------------------------------------------------------------------

_sessions: dict[str, dict] = {}


def _new_session(data: dict | None = None) -> str:
    sid = str(uuid.uuid4())
    _sessions[sid] = data or {}
    return sid


def _get_session(session_id: str) -> dict:
    s = _sessions.get(session_id)
    if s is None:
        raise HTTPException(status_code=404, detail="Session not found. Please start a new analysis.")
    return s


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class AnalyzeRequest(BaseModel):
    url: str

class ShopAnalyzeRequest(BaseModel):
    shop_domain: str   # e.g. "myvintageshop.com"

class QuizAnswersRequest(BaseModel):
    session_id: str
    answers: dict[str, str]


# ---------------------------------------------------------------------------
# Widget endpoint
# ---------------------------------------------------------------------------

@app.get("/widget.js", include_in_schema=False)
async def serve_widget():
    """Serve the embeddable widget JavaScript file."""
    if not WIDGET_PATH.exists():
        raise HTTPException(status_code=404, detail="widget.js not found.")
    return FileResponse(
        WIDGET_PATH,
        media_type="application/javascript",
        headers={
            "Cache-Control": "public, max-age=3600",   # browsers cache for 1 h
        },
    )


# ---------------------------------------------------------------------------
# WIDGET API  (/api/shop/*)
# ---------------------------------------------------------------------------

@app.post("/api/shop/analyze")
async def shop_analyze(
    body: ShopAnalyzeRequest,
    x_api_key: Annotated[str | None, Header()] = None,
):
    """
    Widget step 1: Analyse a Shopify store and return a custom quiz.
    The analysis is cached per domain for 24 hours so repeat visitors are instant.
    """
    _require_api_key(x_api_key)

    domain = body.shop_domain.lower().strip()
    # Strip protocol if the widget accidentally sends a full URL
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]

    # ── Serve from cache if available ──
    cached = _get_cached_analysis(domain)
    if cached:
        # Create a fresh session pointing at the cached analysis + quiz
        session_id = _new_session({
            "domain":   domain,
            "analysis": cached["analysis"],
            "quiz":     cached["quiz"],
        })
        return {
            "session_id":        session_id,
            "shop_name":         cached["analysis"].get("shop_name", ""),
            "tagline":           cached["analysis"].get("tagline", ""),
            "aesthetic_summary": cached["analysis"].get("aesthetic_summary", ""),
            "quiz":              cached["quiz"],
            "from_cache":        True,
        }

    # ── Fresh analysis ──
    try:
        analysis = analyze_shopify_store(domain)
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"Could not analyse store: {exc}")

    try:
        quiz = generate_quiz(analysis)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Quiz generation failed: {exc}")

    _set_cached_analysis(domain, {"analysis": analysis, "quiz": quiz})

    session_id = _new_session({
        "domain":   domain,
        "analysis": analysis,
        "quiz":     quiz,
    })

    return {
        "session_id":        session_id,
        "shop_name":         analysis.get("shop_name", ""),
        "tagline":           analysis.get("tagline", ""),
        "aesthetic_summary": analysis.get("aesthetic_summary", ""),
        "quiz":              quiz,
        "from_cache":        False,
    }


@app.post("/api/shop/recommendations")
async def shop_recommendations(
    body: QuizAnswersRequest,
    x_api_key: Annotated[str | None, Header()] = None,
):
    """Widget step 2: Submit quiz answers, receive personalised recommendations."""
    _require_api_key(x_api_key)

    session  = _get_session(body.session_id)
    analysis = session.get("analysis")
    quiz     = session.get("quiz")
    if not analysis or not quiz:
        raise HTTPException(status_code=400, detail="Session has no analysis/quiz data.")

    try:
        result = get_recommendations(analysis, quiz, body.answers)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Recommendation engine failed: {exc}")

    session["recommendations"] = result
    session["answers"]         = body.answers
    return result


@app.post("/api/shop/outfit-image")
async def shop_outfit_image(
    session_id: Annotated[str, Form()],
    photo: Annotated[UploadFile | None, File()] = None,
    x_api_key: Annotated[str | None, Header()] = None,
):
    """Widget step 3 (optional): Generate an outfit image."""
    _require_api_key(x_api_key)

    session = _get_session(session_id)
    recs    = session.get("recommendations", {}).get("recommendations", [])
    if not recs:
        raise HTTPException(status_code=400, detail="No recommendations found. Complete the quiz first.")

    photo_bytes: bytes | None = None
    if photo and photo.filename:
        if not (photo.content_type or "").startswith("image/"):
            raise HTTPException(status_code=400, detail="Uploaded file must be an image.")
        photo_bytes = await photo.read()
        if len(photo_bytes) > 10 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="Image too large (max 10 MB).")

    style_profile = session.get("recommendations", {}).get("style_profile", "")
    return generate_outfit_image(photo_bytes, recs[0], style_profile)


# ---------------------------------------------------------------------------
# INTERNAL SPA API  (/api/*)  – for your own test frontend
# ---------------------------------------------------------------------------

@app.post("/api/analyze")
async def api_analyze(body: AnalyzeRequest):
    """SPA step 1: Analyse any website URL."""
    url = body.url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        analysis = analyze_website(url)
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"Could not analyse website: {exc}")

    try:
        quiz = generate_quiz(analysis)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Quiz generation failed: {exc}")

    session_id = _new_session({"url": url, "analysis": analysis, "quiz": quiz})

    return {
        "session_id":        session_id,
        "shop_name":         analysis.get("shop_name", ""),
        "tagline":           analysis.get("tagline", ""),
        "aesthetic_summary": analysis.get("aesthetic_summary", ""),
        "quiz":              quiz,
    }


@app.post("/api/recommendations")
async def api_recommendations(body: QuizAnswersRequest):
    """SPA step 2: Submit quiz answers."""
    session  = _get_session(body.session_id)
    analysis = session.get("analysis")
    quiz     = session.get("quiz")
    if not analysis or not quiz:
        raise HTTPException(status_code=400, detail="Session has no analysis/quiz data.")

    try:
        result = get_recommendations(analysis, quiz, body.answers)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Recommendation engine failed: {exc}")

    session["recommendations"] = result
    session["answers"]         = body.answers
    return result


@app.post("/api/outfit-image")
async def api_outfit_image(
    session_id: Annotated[str, Form()],
    photo: Annotated[UploadFile | None, File()] = None,
):
    """SPA step 3 (optional): Generate outfit image."""
    session = _get_session(session_id)
    recs    = session.get("recommendations", {}).get("recommendations", [])
    if not recs:
        raise HTTPException(status_code=400, detail="Complete the quiz first.")

    photo_bytes: bytes | None = None
    if photo and photo.filename:
        if not (photo.content_type or "").startswith("image/"):
            raise HTTPException(status_code=400, detail="Uploaded file must be an image.")
        photo_bytes = await photo.read()
        if len(photo_bytes) > 10 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="Image too large (max 10 MB).")

    style_profile = session.get("recommendations", {}).get("style_profile", "")
    return generate_outfit_image(photo_bytes, recs[0], style_profile)


# ---------------------------------------------------------------------------
# Frontend serving (SPA)
# ---------------------------------------------------------------------------

if (FRONTEND_DIR / "static").exists():
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR / "static"), name="static")


@app.get("/")
async def root():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/quiz")
async def quiz_page():
    return FileResponse(FRONTEND_DIR / "quiz.html")

@app.get("/results")
async def results_page():
    return FileResponse(FRONTEND_DIR / "results.html")


# ---------------------------------------------------------------------------
# Dev entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
