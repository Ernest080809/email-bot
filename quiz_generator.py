"""
quiz_generator.py
-----------------
Takes the structured website analysis produced by website_analyzer.py and uses
Claude to generate a fully customised, store-specific style quiz.

The quiz is NOT generic.  Every question is grounded in the specific aesthetic,
era vocabulary, product categories, and colour palette of the analysed shop.
"""

import re
import json
from anthropic import Anthropic

client = Anthropic()

_QUIZ_SYSTEM = """\
You are a creative fashion stylist and UX copywriter for a vintage clothing brand.
Your job is to write a personalised style quiz that feels like it was made exclusively
for one specific vintage shop.

Rules:
- Every question must reference the shop's own aesthetic vocabulary, eras, and product
  catalogue.  A user should feel this quiz could ONLY belong to this exact store.
- Questions must be friendly, engaging, and slightly playful in tone.
- Each question has exactly 4 answer options.
- Each answer option must include a short "style_tag" (a 1-3 word label the backend
  uses to match products) and an "emoji" for visual appeal.
- Return ONLY valid JSON matching the schema below – no prose, no markdown fences.
"""

_QUIZ_SCHEMA = """\
{
  "quiz_title": "string  (catchy, store-specific title)",
  "quiz_intro": "string  (1-2 sentence intro personalised to the shop)",
  "questions": [
    {
      "id": "q1",
      "question": "string",
      "context_hint": "string  (1 short sentence explaining why this question matters)",
      "options": [
        { "id": "a", "text": "string", "style_tag": "string", "emoji": "string" },
        { "id": "b", "text": "string", "style_tag": "string", "emoji": "string" },
        { "id": "c", "text": "string", "style_tag": "string", "emoji": "string" },
        { "id": "d", "text": "string", "style_tag": "string", "emoji": "string" }
      ]
    }
  ]
}
"""

_REQUIRED_QUESTION_TYPES = [
    "occasion / lifestyle  (where does the user wear these clothes?)",
    "sub-aesthetic preference (which micro-trend within this shop's style appeals most?)",
    "era / decade preference (which decade's fashion resonates with the user?)",
    "silhouette / fit preference (how does the user like clothes to fit?)",
    "colour mood (what colour story suits the user best?)",
    "style icon or cultural reference (who inspires the user's look?)",
    "shopping intention (what is the user looking for today?)",
]


def generate_quiz(analysis: dict) -> dict:
    """
    Given a website analysis dict, return the quiz dict.
    Raises on Claude errors or JSON parsing failures.
    """
    quiz_themes = analysis.get("quiz_themes", {})
    shop_name = analysis.get("shop_name", "this shop")

    prompt = f"""
SHOP ANALYSIS:
{json.dumps(analysis, indent=2)}

---
You must now create a {len(_REQUIRED_QUESTION_TYPES)}-question style quiz for {shop_name}.

Generate exactly one question for each of these required types, in this order:
{chr(10).join(f"{i+1}. {t}" for i, t in enumerate(_REQUIRED_QUESTION_TYPES))}

Additional constraints:
- Use the shop's quiz_themes as your primary vocabulary source for answer options.
- Reference specific product categories and style_keywords found in the analysis.
- The quiz_title must include or allude to the shop's name or tagline.
- Answer options must feel hand-crafted for this store, not copy-paste generic.
- style_tag values will be used programmatically for product matching – keep them
  concise, lowercase, hyphenated (e.g. "70s-boho", "oversized-blazer", "dusty-rose").

Return the JSON object matching exactly this schema:
{_QUIZ_SCHEMA}
""".strip()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,
        system=_QUIZ_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    quiz = json.loads(raw)

    # Ensure question IDs are sequential strings
    for i, q in enumerate(quiz.get("questions", []), start=1):
        q["id"] = f"q{i}"

    return quiz
