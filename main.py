"""
main.py
-------
FastAPI application exposing the AI Stylist endpoints.

Endpoints
---------
POST /api/analyze          – analyze a website URL, returns analysis + quiz
POST /api/recommendations  – submit quiz answers, returns product recommendations
POST /api/outfit-image     – (optional) generate outfit image for user photo
GET  /                     – serve the SPA frontend
"""

import os
import uuid
import json
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, HttpUrl
from dotenv import load_dotenv

load_dotenv()

from website_analyzer import analyze_website
from quiz_generator import generate_quiz
from recommendation_engine import get_recommendations
from image_generator import generate_outfit_image

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="AI Vintage Stylist",
    description="Personalised style quiz and product recommendations for vintage fashion shops.",
    version="1.0.0",
)

FRONTEND_DIR = Path(__file__).parent / "frontend"

# ---------------------------------------------------------------------------
# In-memory session store
# (swap for Redis / DB in production)
# ---------------------------------------------------------------------------

_sessions: dict[str, dict] = {}


def _new_session() -> str:
    sid = str(uuid.uuid4())
    _sessions[sid] = {}
    return sid


def _get_session(session_id: str) -> dict:
    if session_id not in _sessions:
        raise HTTPException(status_code=404, detail="Session not found. Please start a new analysis.")
    return _sessions[session_id]


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class AnalyzeRequest(BaseModel):
    url: str  # validated below


class QuizAnswersRequest(BaseModel):
    session_id: str
    answers: dict[str, str]  # {"q1": "b", "q2": "a", ...}


# ---------------------------------------------------------------------------
# API routes
# ---------------------------------------------------------------------------

@app.post("/api/analyze")
async def api_analyze(body: AnalyzeRequest):
    """
    Step 1: Analyze a vintage fashion website.
    Returns a session_id, the full analysis, and the custom quiz.
    """
    url = body.url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        analysis = analyze_website(url)
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"Could not analyze website: {exc}")

    try:
        quiz = generate_quiz(analysis)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Quiz generation failed: {exc}")

    session_id = _new_session()
    _sessions[session_id] = {
        "url": url,
        "analysis": analysis,
        "quiz": quiz,
    }

    return {
        "session_id": session_id,
        "shop_name": analysis.get("shop_name", ""),
        "tagline": analysis.get("tagline", ""),
        "aesthetic_summary": analysis.get("aesthetic_summary", ""),
        "quiz": quiz,
    }


@app.post("/api/recommendations")
async def api_recommendations(body: QuizAnswersRequest):
    """
    Step 2: Submit quiz answers and receive personalised product recommendations.
    """
    session = _get_session(body.session_id)

    analysis = session.get("analysis")
    quiz = session.get("quiz")
    if not analysis or not quiz:
        raise HTTPException(status_code=400, detail="Session has no analysis/quiz data.")

    try:
        result = get_recommendations(analysis, quiz, body.answers)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Recommendation engine failed: {exc}")

    session["recommendations"] = result
    session["answers"] = body.answers

    return result


@app.post("/api/outfit-image")
async def api_outfit_image(
    session_id: Annotated[str, Form()],
    photo: Annotated[UploadFile | None, File()] = None,
):
    """
    Step 3 (optional): Generate an outfit image.
    Accepts an optional user photo upload.
    """
    session = _get_session(session_id)

    recommendations = session.get("recommendations")
    if not recommendations:
        raise HTTPException(
            status_code=400,
            detail="No recommendations found. Complete the quiz first.",
        )

    recs = recommendations.get("recommendations", [])
    if not recs:
        raise HTTPException(status_code=400, detail="No recommended products found.")

    top_rec = recs[0]
    style_profile = recommendations.get("style_profile", "")

    photo_bytes: bytes | None = None
    if photo and photo.filename:
        content_type = photo.content_type or ""
        if not content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Uploaded file must be an image.")
        photo_bytes = await photo.read()
        if len(photo_bytes) > 10 * 1024 * 1024:  # 10 MB cap
            raise HTTPException(status_code=400, detail="Image too large (max 10 MB).")

    result = generate_outfit_image(photo_bytes, top_rec, style_profile)
    return result


# ---------------------------------------------------------------------------
# Frontend serving
# ---------------------------------------------------------------------------

# Serve static assets (CSS, JS, images)
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
