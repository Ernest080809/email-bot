import os
import json
import uuid
from datetime import datetime, date
from pathlib import Path
from typing import Optional, List, Dict, Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import anthropic

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

GOALS_FILE    = DATA_DIR / "goals.json"
HABITS_FILE   = DATA_DIR / "habits.json"
NOTES_FILE    = DATA_DIR / "notes.json"
BUSINESS_FILE = DATA_DIR / "business.json"
PROFILE_FILE  = DATA_DIR / "profile.json"
CHAT_FILE     = DATA_DIR / "mentor_chat.json"


def read_json(path: Path, default=None):
    if default is None:
        default = []
    try:
        if path.exists():
            return json.loads(path.read_text())
        return default
    except Exception:
        return default


def write_json(path: Path, data):
    path.write_text(json.dumps(data, indent=2, default=str))


def now_iso():
    return datetime.now().isoformat()


def today_str():
    return date.today().isoformat()


# ── Pydantic models ────────────────────────────────────────────────────────────

class GoalCreate(BaseModel):
    title: str
    description: str = ""
    category: str = "personal"
    priority: str = "medium"
    target_date: Optional[str] = None
    milestones: List[Dict] = []


class GoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    progress: Optional[int] = None
    target_date: Optional[str] = None
    milestones: Optional[List[Dict]] = None
    status: Optional[str] = None


class HabitCreate(BaseModel):
    name: str
    category: str = "health"
    frequency: str = "daily"
    icon: str = "✓"
    color: str = "#7c6ff7"


class NoteCreate(BaseModel):
    title: str
    content: str = ""
    tags: List[str] = []
    category: str = "general"
    pinned: bool = False


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
    category: Optional[str] = None
    pinned: Optional[bool] = None


class BusinessCreate(BaseModel):
    name: str
    type: str = "project"
    revenue_goal: float = 0
    description: str = ""


class BusinessUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    revenue: Optional[float] = None
    revenue_goal: Optional[float] = None
    tasks: Optional[List[Dict]] = None
    notes: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None


class ProfileData(BaseModel):
    answers: Dict[str, Any] = {}
    completed_onboarding: bool = False


class MentorMessage(BaseModel):
    message: str


# ── Goals ──────────────────────────────────────────────────────────────────────

@router.get("/goals")
def get_goals():
    return read_json(GOALS_FILE)


@router.post("/goals")
def create_goal(goal: GoalCreate):
    goals = read_json(GOALS_FILE)
    new_goal = {
        "id": str(uuid.uuid4()),
        "title": goal.title,
        "description": goal.description,
        "category": goal.category,
        "priority": goal.priority,
        "progress": 0,
        "target_date": goal.target_date,
        "milestones": goal.milestones,
        "status": "active",
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    goals.append(new_goal)
    write_json(GOALS_FILE, goals)
    return new_goal


@router.put("/goals/{goal_id}")
def update_goal(goal_id: str, update: GoalUpdate):
    goals = read_json(GOALS_FILE)
    for g in goals:
        if g["id"] == goal_id:
            for field, val in update.model_dump(exclude_none=True).items():
                g[field] = val
            g["updated_at"] = now_iso()
            write_json(GOALS_FILE, goals)
            return g
    raise HTTPException(404, "Goal not found")


@router.delete("/goals/{goal_id}")
def delete_goal(goal_id: str):
    goals = read_json(GOALS_FILE)
    write_json(GOALS_FILE, [g for g in goals if g["id"] != goal_id])
    return {"ok": True}


# ── Habits ─────────────────────────────────────────────────────────────────────

@router.get("/habits")
def get_habits():
    return read_json(HABITS_FILE)


@router.post("/habits")
def create_habit(habit: HabitCreate):
    habits = read_json(HABITS_FILE)
    new_habit = {
        "id": str(uuid.uuid4()),
        "name": habit.name,
        "category": habit.category,
        "frequency": habit.frequency,
        "icon": habit.icon,
        "color": habit.color,
        "completions": {},
        "created_at": now_iso(),
    }
    habits.append(new_habit)
    write_json(HABITS_FILE, habits)
    return new_habit


@router.post("/habits/{habit_id}/checkin")
def checkin_habit(habit_id: str):
    habits = read_json(HABITS_FILE)
    today = today_str()
    for h in habits:
        if h["id"] == habit_id:
            completions = h.setdefault("completions", {})
            completions[today] = completions.get(today, 0) + 1
            write_json(HABITS_FILE, habits)
            return h
    raise HTTPException(404, "Habit not found")


@router.post("/habits/{habit_id}/uncheckin")
def uncheckin_habit(habit_id: str):
    habits = read_json(HABITS_FILE)
    today = today_str()
    for h in habits:
        if h["id"] == habit_id:
            completions = h.setdefault("completions", {})
            if completions.get(today, 0) > 0:
                completions[today] -= 1
                if completions[today] == 0:
                    del completions[today]
            write_json(HABITS_FILE, habits)
            return h
    raise HTTPException(404, "Habit not found")


@router.delete("/habits/{habit_id}")
def delete_habit(habit_id: str):
    habits = read_json(HABITS_FILE)
    write_json(HABITS_FILE, [h for h in habits if h["id"] != habit_id])
    return {"ok": True}


# ── Notes ──────────────────────────────────────────────────────────────────────

@router.get("/notes")
def get_notes():
    notes = read_json(NOTES_FILE)
    return sorted(notes, key=lambda n: (not n.get("pinned", False), n.get("updated_at", "")), reverse=False)


@router.post("/notes")
def create_note(note: NoteCreate):
    notes = read_json(NOTES_FILE)
    new_note = {
        "id": str(uuid.uuid4()),
        "title": note.title,
        "content": note.content,
        "tags": note.tags,
        "category": note.category,
        "pinned": note.pinned,
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    notes.append(new_note)
    write_json(NOTES_FILE, notes)
    return new_note


@router.put("/notes/{note_id}")
def update_note(note_id: str, update: NoteUpdate):
    notes = read_json(NOTES_FILE)
    for n in notes:
        if n["id"] == note_id:
            for field, val in update.model_dump(exclude_none=True).items():
                n[field] = val
            n["updated_at"] = now_iso()
            write_json(NOTES_FILE, notes)
            return n
    raise HTTPException(404, "Note not found")


@router.delete("/notes/{note_id}")
def delete_note(note_id: str):
    notes = read_json(NOTES_FILE)
    write_json(NOTES_FILE, [n for n in notes if n["id"] != note_id])
    return {"ok": True}


# ── Business ───────────────────────────────────────────────────────────────────

@router.get("/business")
def get_business():
    return read_json(BUSINESS_FILE)


@router.post("/business")
def create_business(biz: BusinessCreate):
    businesses = read_json(BUSINESS_FILE)
    new_biz = {
        "id": str(uuid.uuid4()),
        "name": biz.name,
        "type": biz.type,
        "status": "active",
        "revenue": 0.0,
        "revenue_goal": biz.revenue_goal,
        "description": biz.description,
        "tasks": [],
        "notes": "",
        "created_at": now_iso(),
    }
    businesses.append(new_biz)
    write_json(BUSINESS_FILE, businesses)
    return new_biz


@router.put("/business/{biz_id}")
def update_business(biz_id: str, update: BusinessUpdate):
    businesses = read_json(BUSINESS_FILE)
    for b in businesses:
        if b["id"] == biz_id:
            for field, val in update.model_dump(exclude_none=True).items():
                b[field] = val
            write_json(BUSINESS_FILE, businesses)
            return b
    raise HTTPException(404, "Business not found")


@router.delete("/business/{biz_id}")
def delete_business(biz_id: str):
    businesses = read_json(BUSINESS_FILE)
    write_json(BUSINESS_FILE, [b for b in businesses if b["id"] != biz_id])
    return {"ok": True}


# ── Profile ────────────────────────────────────────────────────────────────────

@router.get("/profile")
def get_profile():
    return read_json(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})


@router.post("/profile")
def save_profile(profile: ProfileData):
    current = read_json(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    current["answers"].update(profile.answers)
    current["completed_onboarding"] = profile.completed_onboarding
    write_json(PROFILE_FILE, current)
    return current


# ── Mentor Chat ────────────────────────────────────────────────────────────────

@router.get("/mentor/chat")
def get_chat():
    return read_json(CHAT_FILE, default=[])


@router.post("/mentor/chat")
def mentor_chat(msg: MentorMessage):
    profile = read_json(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    history = read_json(CHAT_FILE, default=[])

    profile_context = ""
    answers = profile.get("answers", {})
    if answers:
        lines = [f"- {k}: {v}" for k, v in answers.items() if v]
        if lines:
            profile_context = "\n\nWhat I know about this person:\n" + "\n".join(lines)

    system_prompt = f"""You are a world-class life mentor, executive coach, and trusted advisor.
You blend the strategic brilliance of Tim Ferriss, the emotional depth of Brené Brown, and the motivational fire of Tony Robbins.

Your mission:
- Help this person achieve their goals across all life areas (personal, health, career, finances, relationships)
- Give specific, actionable advice tailored to their exact situation — never generic platitudes
- Ask 1–2 sharp follow-up questions to dig deeper when appropriate
- Challenge limiting beliefs with compassion and evidence
- Celebrate wins; reframe setbacks as data
- Be direct, warm, and occasionally funny
- Keep responses concise and high-impact (2–4 paragraphs max)
{profile_context}

Today's date: {date.today().strftime("%B %d, %Y")}"""

    messages = [{"role": m["role"], "content": m["content"]} for m in history[-20:]]
    messages.append({"role": "user", "content": msg.message})

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=messages,
    )
    reply = response.content[0].text

    history.append({"role": "user",      "content": msg.message, "timestamp": now_iso()})
    history.append({"role": "assistant", "content": reply,       "timestamp": now_iso()})
    write_json(CHAT_FILE, history)

    return {"reply": reply}


@router.delete("/mentor/chat")
def clear_chat():
    write_json(CHAT_FILE, [])
    return {"ok": True}


# ── Stats ──────────────────────────────────────────────────────────────────────

@router.get("/stats")
def get_stats():
    goals      = read_json(GOALS_FILE)
    habits     = read_json(HABITS_FILE)
    notes      = read_json(NOTES_FILE)
    businesses = read_json(BUSINESS_FILE)
    today      = today_str()

    active_goals    = [g for g in goals    if g.get("status") == "active"]
    completed_goals = [g for g in goals    if g.get("status") == "completed"]
    completed_today = sum(1 for h in habits if today in h.get("completions", {}))
    total_revenue   = sum(b.get("revenue", 0) for b in businesses)

    return {
        "goals":    {"total": len(goals),   "active": len(active_goals), "completed": len(completed_goals)},
        "habits":   {"total": len(habits),  "completed_today": completed_today},
        "notes":    {"total": len(notes)},
        "business": {"total": len(businesses), "revenue": total_revenue},
    }
