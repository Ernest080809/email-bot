"""
recommendation_engine.py
------------------------
Takes the user's quiz answers and the website analysis (including product catalogue)
and uses Claude to produce highly personalised product recommendations with
reasoning tailored to the individual user's expressed style profile.
"""

import re
import json
from anthropic import Anthropic

client = Anthropic()

_RECO_SYSTEM = """\
You are an expert personal stylist for a vintage clothing boutique.
You have access to the shop's product catalogue and a customer's style quiz answers.
Your job is to select the best matching products and write personalised, compelling
recommendation copy that makes the customer feel truly understood.

Rules:
- Recommend 3 to 5 products maximum.
- Only recommend products that actually appear in the catalogue.
- For each product write a short, personal "why it's perfect for you" note (2-3 sentences)
  that references the customer's specific quiz answers.
- Also generate a "style_profile" summary: a 2-3 sentence portrait of this customer's
  personal style, written in second person ("Your style is…").
- Return ONLY valid JSON matching the schema below – no prose, no markdown fences.
"""

_RECO_SCHEMA = """\
{
  "style_profile": "string  (second-person portrait of the customer's style)",
  "style_profile_title": "string  (a catchy 3-5 word title for their style, e.g. 'The Velvet Wanderer')",
  "recommendations": [
    {
      "product_name": "string",
      "product_url": "string",
      "product_image": "string",
      "product_price": "string",
      "match_score": "integer 1-100",
      "why_for_you": "string  (personalised explanation)",
      "style_tags": ["list of matching style tags"]
    }
  ],
  "styling_tip": "string  (one actionable outfit tip for this customer using the recommended items)"
}
"""


def _build_style_tags_from_answers(quiz: dict, answers: dict) -> list[str]:
    """
    Cross-reference question IDs and chosen option IDs to extract style_tags.
    answers = { "q1": "b", "q2": "a", ... }
    """
    tags = []
    for question in quiz.get("questions", []):
        qid = question["id"]
        chosen_option_id = answers.get(qid)
        if not chosen_option_id:
            continue
        for option in question.get("options", []):
            if option["id"] == chosen_option_id:
                tags.append(option.get("style_tag", ""))
                break
    return [t for t in tags if t]


def _format_answers_for_prompt(quiz: dict, answers: dict) -> str:
    lines = []
    for question in quiz.get("questions", []):
        qid = question["id"]
        chosen_option_id = answers.get(qid)
        question_text = question.get("question", "")
        chosen_text = ""
        chosen_tag = ""
        for option in question.get("options", []):
            if option["id"] == chosen_option_id:
                chosen_text = option.get("text", "")
                chosen_tag = option.get("style_tag", "")
                break
        lines.append(
            f"Q: {question_text}\n"
            f"   Answer: {chosen_text}  [tag: {chosen_tag}]"
        )
    return "\n\n".join(lines)


def get_recommendations(
    analysis: dict,
    quiz: dict,
    answers: dict,
) -> dict:
    """
    Main entry point.
    analysis  – from website_analyzer.analyze_website()
    quiz      – from quiz_generator.generate_quiz()
    answers   – dict mapping question IDs to selected option IDs,
                e.g. {"q1": "c", "q2": "a", ...}

    Returns the recommendations dict.
    """
    style_tags = _build_style_tags_from_answers(quiz, answers)
    formatted_answers = _format_answers_for_prompt(quiz, answers)
    products = analysis.get("products", [])
    shop_name = analysis.get("shop_name", "the shop")

    prompt = f"""
SHOP: {shop_name}
AESTHETIC SUMMARY: {analysis.get("aesthetic_summary", "")}
STYLE KEYWORDS: {", ".join(analysis.get("style_keywords", []))}

--- CUSTOMER QUIZ ANSWERS ---
{formatted_answers}

DERIVED STYLE TAGS: {", ".join(style_tags)}

--- PRODUCT CATALOGUE ({len(products)} items) ---
{json.dumps(products, indent=2)}

---
Based on the customer's quiz answers and derived style tags, choose the 3-5 best
matching products from the catalogue above and write personalised recommendation copy.

Return the JSON object matching exactly this schema:
{_RECO_SCHEMA}
""".strip()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2500,
        system=_RECO_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    result = json.loads(raw)

    # Patch in full product data for any fields the LLM left empty
    name_map = {p["name"]: p for p in products}
    for rec in result.get("recommendations", []):
        source = name_map.get(rec.get("product_name"), {})
        for field in ("product_url", "product_image", "product_price"):
            if not rec.get(field):
                key = field.replace("product_", "")
                rec[field] = source.get(key, source.get("url" if key == "url" else key, ""))

    return result
