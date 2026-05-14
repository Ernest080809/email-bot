"""
telegram_bot.py
───────────────
Personal Dashboard Telegram Bot powered by Claude AI.

Sections:
  📊 Overview   — daily stats at a glance
  🎯 Goals      — add / track / complete goals
  💪 Habits     — daily check-ins with streaks
  📝 Notes      — quick capture, pin, search
  💼 Business   — projects, revenue, tasks
  🤖 Mentor     — AI coaching chat (Claude)
  📋 Profile    — 100-question onboarding
"""

import os
import json
import uuid
import logging
from datetime import datetime, date, timedelta
from pathlib import Path

import anthropic
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes,
)
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ── Data helpers ───────────────────────────────────────────────────────────────

DATA_DIR      = Path("data")
DATA_DIR.mkdir(exist_ok=True)

GOALS_FILE    = DATA_DIR / "goals.json"
HABITS_FILE   = DATA_DIR / "habits.json"
NOTES_FILE    = DATA_DIR / "notes.json"
BUSINESS_FILE = DATA_DIR / "business.json"
PROFILE_FILE  = DATA_DIR / "profile.json"
CHAT_FILE     = DATA_DIR / "mentor_chat.json"


def rj(path: Path, default=None):
    if default is None:
        default = []
    try:
        return json.loads(path.read_text()) if path.exists() else default
    except Exception:
        return default


def wj(path: Path, data):
    path.write_text(json.dumps(data, indent=2, default=str))


def now_iso() -> str:
    return datetime.now().isoformat()


def today() -> str:
    return date.today().isoformat()


def calc_streak(completions: dict) -> int:
    d = date.today()
    s = 0
    while d.isoformat() in completions:
        s += 1
        d -= timedelta(days=1)
    return s


def bar(pct: int, w: int = 8) -> str:
    filled = round(pct / 100 * w)
    return "▓" * filled + "░" * (w - filled)


def p_emoji(p: str) -> str:
    return {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(p, "⚪")


def c_emoji(c: str) -> str:
    return {
        "personal": "👤", "health": "💪", "business": "💼",
        "financial": "💰", "learning": "📚", "relationship": "❤️",
    }.get(c, "🎯")


# ── Conversation states ────────────────────────────────────────────────────────

(
    MAIN,
    GOAL_TITLE, GOAL_CATEGORY, GOAL_PRIORITY, GOAL_DATE, GOAL_PROGRESS,
    HABIT_NAME, HABIT_CATEGORY, HABIT_ICON,
    NOTE_TITLE, NOTE_CONTENT,
    BIZ_NAME, BIZ_TYPE, BIZ_GOAL, BIZ_REVENUE, BIZ_TASK,
    MENTOR_MODE,
    OB_ANSWER,
) = range(18)


# ── 100-question onboarding ────────────────────────────────────────────────────

ONBOARDING = [
    {"type": "header", "title": "👤 Who Are You?"},
    {"type": "q", "id": "name",            "text": "What's your full name?"},
    {"type": "q", "id": "age",             "text": "How old are you?"},
    {"type": "q", "id": "location",        "text": "Where do you live? (city / country)"},
    {"type": "q", "id": "values",          "text": "What are your top 3 core values in life?"},
    {"type": "q", "id": "personality",     "text": "Describe yourself in 3 words"},
    {"type": "q", "id": "relationship",    "text": "What's your relationship status?"},
    {"type": "q", "id": "children",        "text": "Do you have children? (yes/no — how many?)"},
    {"type": "q", "id": "happiness",       "text": "What makes you truly happy?"},
    {"type": "q", "id": "proudest",        "text": "What are you most proud of in your life?"},
    {"type": "q", "id": "strength",        "text": "What's your biggest personality strength?"},

    {"type": "header", "title": "🌟 Vision & Goals"},
    {"type": "q", "id": "top_goal",        "text": "What's your #1 goal right now?"},
    {"type": "q", "id": "five_year",       "text": "Where do you want to be in 5 years?"},
    {"type": "q", "id": "success_meaning", "text": "What does success mean to you personally?"},
    {"type": "q", "id": "biggest_dream",   "text": "What's your biggest dream?"},
    {"type": "q", "id": "no_failure",      "text": "What would you do if you knew you couldn't fail?"},
    {"type": "q", "id": "legacy",          "text": "What legacy do you want to leave behind?"},
    {"type": "q", "id": "procrastinating", "text": "What's one goal you've been putting off?"},
    {"type": "q", "id": "top_priorities",  "text": "What are your top 3 priorities in life right now?"},
    {"type": "q", "id": "fulfillment",     "text": "What would need to change for you to feel truly fulfilled?"},
    {"type": "q", "id": "perfect_day",     "text": "Describe your perfect day in detail"},

    {"type": "header", "title": "💪 Health & Wellness"},
    {"type": "q", "id": "health_rating",   "text": "Rate your overall health right now (1–10)"},
    {"type": "q", "id": "sleep_hours",     "text": "How many hours do you sleep per night?"},
    {"type": "q", "id": "exercise_freq",   "text": "How often do you exercise per week?"},
    {"type": "q", "id": "diet",            "text": "What does your typical diet look like?"},
    {"type": "q", "id": "health_goal",     "text": "What's your biggest health goal?"},
    {"type": "q", "id": "health_issues",   "text": "Do you have any health challenges or conditions?"},
    {"type": "q", "id": "water",           "text": "How much water do you drink daily?"},
    {"type": "q", "id": "morning_routine", "text": "Describe your current morning routine"},
    {"type": "q", "id": "stress_mgmt",     "text": "How do you manage stress?"},
    {"type": "q", "id": "health_habit",    "text": "What's one health habit you most want to build?"},

    {"type": "header", "title": "💼 Career & Business"},
    {"type": "q", "id": "current_work",    "text": "What do you do for work currently?"},
    {"type": "q", "id": "work_type",       "text": "Are you employed, self-employed, or a business owner?"},
    {"type": "q", "id": "career_goal",     "text": "What's your biggest career or business goal?"},
    {"type": "q", "id": "work_love",       "text": "What do you love most about your work?"},
    {"type": "q", "id": "work_challenge",  "text": "What do you find most challenging about your work?"},
    {"type": "q", "id": "biz_idea",        "text": "Do you have a business idea you want to pursue?"},
    {"type": "q", "id": "target_market",   "text": "Who does your business serve / who is your target market?"},
    {"type": "q", "id": "income_goal",     "text": "What's your monthly income or revenue goal?"},
    {"type": "q", "id": "skills_building", "text": "What professional skills are you actively developing?"},
    {"type": "q", "id": "competitors",     "text": "Who are your competitors or peers in your field?"},
    {"type": "q", "id": "work_hours",      "text": "How many hours per week do you work?"},
    {"type": "q", "id": "work_tools",      "text": "What tools or platforms are essential to your work?"},
    {"type": "q", "id": "team",            "text": "Do you have a team or work alone?"},
    {"type": "q", "id": "top_achievement", "text": "What's your biggest professional achievement so far?"},
    {"type": "q", "id": "ten_x",          "text": "What one thing would make your career/business 10x better?"},

    {"type": "header", "title": "💰 Money & Finances"},
    {"type": "q", "id": "finance_rating",  "text": "Rate your financial health right now (1–10)"},
    {"type": "q", "id": "emergency_fund",  "text": "Do you have an emergency fund? (how many months?)"},
    {"type": "q", "id": "financial_goal",  "text": "What's your biggest financial goal this year?"},
    {"type": "q", "id": "investments",     "text": "Do you invest? (stocks, real estate, crypto, other?)"},
    {"type": "q", "id": "debt",            "text": "Do you have debt you're working to pay off?"},
    {"type": "q", "id": "budget",          "text": "Do you follow a monthly budget?"},
    {"type": "q", "id": "income_range",    "text": "What's your approximate monthly income?"},
    {"type": "q", "id": "money_fear",      "text": "What's your biggest financial fear?"},
    {"type": "q", "id": "passive_income",  "text": "Do you have any passive income streams?"},
    {"type": "q", "id": "fin_freedom",     "text": "What would financial freedom look like for you?"},

    {"type": "header", "title": "❤️ Relationships & Social"},
    {"type": "q", "id": "family",          "text": "How are your family relationships?"},
    {"type": "q", "id": "close_friends",   "text": "How many close friends do you have?"},
    {"type": "q", "id": "romantic",        "text": "Are you in a romantic relationship? How is it?"},
    {"type": "q", "id": "conflict_style",  "text": "How do you handle conflict with others?"},
    {"type": "q", "id": "comm_style",      "text": "How would you describe your communication style?"},
    {"type": "q", "id": "network",         "text": "Do you have a strong professional network?"},
    {"type": "q", "id": "role_models",     "text": "Who are your mentors or role models?"},
    {"type": "q", "id": "rel_improve",     "text": "Is there a relationship you want to improve?"},
    {"type": "q", "id": "social_balance",  "text": "How do you balance social time vs. alone time?"},
    {"type": "q", "id": "valued_qualities","text": "What qualities do you value most in people around you?"},

    {"type": "header", "title": "🧠 Mental & Emotional"},
    {"type": "q", "id": "mental_rating",   "text": "Rate your mental health right now (1–10)"},
    {"type": "q", "id": "anxiety",         "text": "Do you experience anxiety or stress regularly?"},
    {"type": "q", "id": "handle_failure",  "text": "How do you typically handle failure or setbacks?"},
    {"type": "q", "id": "inner_critic",    "text": "What does your inner critic say most often?"},
    {"type": "q", "id": "gratitude",       "text": "Do you practice gratitude or journaling?"},
    {"type": "q", "id": "peace",           "text": "What brings you the most peace?"},
    {"type": "q", "id": "mindfulness",     "text": "Do you meditate or practice mindfulness?"},
    {"type": "q", "id": "emotional_block", "text": "What's your biggest emotional challenge?"},
    {"type": "q", "id": "recharge",        "text": "How do you recharge when you're drained?"},
    {"type": "q", "id": "limiting_belief", "text": "What belief about yourself holds you back the most?"},

    {"type": "header", "title": "📚 Learning & Growth"},
    {"type": "q", "id": "books_year",      "text": "How many books do you read per year?"},
    {"type": "q", "id": "skills_wanted",   "text": "What skills do you most want to develop?"},
    {"type": "q", "id": "content",         "text": "What podcasts, shows, or content do you consume most?"},
    {"type": "q", "id": "courses",         "text": "Do you take courses or attend workshops?"},
    {"type": "q", "id": "passion",         "text": "What's your biggest intellectual passion?"},
    {"type": "q", "id": "learn_style",     "text": "How do you learn best? (reading / watching / doing / other)"},
    {"type": "q", "id": "current_mentor",  "text": "Do you currently have a mentor or coach?"},
    {"type": "q", "id": "wish_learned",    "text": "What do you wish you had learned earlier in life?"},
    {"type": "q", "id": "skill_master",    "text": "What one skill do you want to master in the next year?"},
    {"type": "q", "id": "best_invest",     "text": "What's the best investment you've made in yourself?"},

    {"type": "header", "title": "🌿 Lifestyle & Habits"},
    {"type": "q", "id": "ideal_schedule",  "text": "What does your ideal daily schedule look like?"},
    {"type": "q", "id": "hobbies",         "text": "What are your main hobbies or passions?"},
    {"type": "q", "id": "travel",          "text": "Where do you want to travel or live?"},
    {"type": "q", "id": "bad_habit",       "text": "What's one bad habit you want to break?"},
    {"type": "q", "id": "current_morning", "text": "What does your current morning actually look like?"},
    {"type": "q", "id": "screen_time",     "text": "How much screen time do you average per day?"},
    {"type": "q", "id": "wl_balance",      "text": "What's your ideal work-life balance?"},
    {"type": "q", "id": "daily_joy",       "text": "What's one thing you do every day that brings you joy?"},

    {"type": "header", "title": "🔮 Challenges & Your Future"},
    {"type": "q", "id": "biggest_challenge","text": "What's your biggest challenge right now?"},
    {"type": "q", "id": "held_back",       "text": "What has held you back the most in life?"},
    {"type": "q", "id": "overcome",        "text": "What limiting beliefs do you most want to overcome?"},
    {"type": "q", "id": "one_change",      "text": "If you could change one thing about your life today, what would it be?"},
    {"type": "q", "id": "perfect_life",    "text": "Describe your perfect life in vivid detail"},
    {"type": "q", "id": "mentor_help",     "text": "What do you most need help with from a mentor?"},
    {"type": "q", "id": "ninety_days",     "text": "What's one thing you want to accomplish in the next 90 days?"},
]

TOTAL_QUESTIONS = sum(1 for i in ONBOARDING if i["type"] == "q")


# ── UI helpers ─────────────────────────────────────────────────────────────────

def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📊 Overview", callback_data="overview"),
         InlineKeyboardButton("🎯 Goals",    callback_data="goals")],
        [InlineKeyboardButton("💪 Habits",   callback_data="habits"),
         InlineKeyboardButton("📝 Notes",    callback_data="notes")],
        [InlineKeyboardButton("💼 Business", callback_data="business"),
         InlineKeyboardButton("🤖 Mentor",   callback_data="mentor")],
        [InlineKeyboardButton("📋 Profile / Onboarding", callback_data="onboarding")],
    ])


def back_kb(label="🏠 Main Menu", data="menu") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(label, callback_data=data)]])


async def send(update: Update, text: str, kb=None, parse_mode="HTML"):
    kw = dict(text=text, parse_mode=parse_mode, reply_markup=kb)
    if update.callback_query:
        try:
            await update.callback_query.edit_message_text(**kw)
            return
        except Exception:
            msg = update.callback_query.message
    else:
        msg = update.message
    await msg.reply_text(**kw)


# ── /start ─────────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    name = profile.get("answers", {}).get("name", "")
    hi = f"Hey <b>{name}</b>! 👋" if name else "Hey there! 👋"
    tip = (
        "\n\n💡 <i>Tap <b>Profile / Onboarding</b> to complete your 100-question "
        "profile so I can mentor you properly!</i>"
        if not profile.get("completed_onboarding") else ""
    )
    await update.message.reply_text(
        f"{hi} Welcome to your <b>Personal Dashboard</b> 🚀\n\n"
        "Track goals, habits, notes, and business — and get AI-powered mentoring "
        "from Claude.\n\nWhat would you like to do?" + tip,
        parse_mode="HTML",
        reply_markup=main_menu_kb(),
    )
    return MAIN


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 <b>Main Menu</b>", parse_mode="HTML", reply_markup=main_menu_kb()
    )
    return MAIN


async def cb_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        "🏠 <b>Main Menu</b>", parse_mode="HTML", reply_markup=main_menu_kb()
    )
    return MAIN


# ── Overview ───────────────────────────────────────────────────────────────────

async def show_overview(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()

    goals      = rj(GOALS_FILE)
    habits     = rj(HABITS_FILE)
    notes      = rj(NOTES_FILE)
    businesses = rj(BUSINESS_FILE)
    td         = today()

    active     = [g for g in goals if g.get("status") == "active"]
    completed  = [g for g in goals if g.get("status") == "completed"]
    h_done     = sum(1 for h in habits if td in h.get("completions", {}))
    revenue    = sum(b.get("revenue", 0) for b in businesses)
    avg_prog   = (sum(g.get("progress", 0) for g in active) // len(active)) if active else 0

    txt = (
        f"📊 <b>Dashboard — {date.today().strftime('%B %d, %Y')}</b>\n"
        f"{'─'*32}\n\n"
        f"🎯 <b>Goals</b>  Active: {len(active)}  ✅ Done: {len(completed)}\n"
        f"   {bar(avg_prog)} {avg_prog}% avg progress\n\n"
        f"💪 <b>Habits</b>  {h_done}/{len(habits)} done today "
        f"{'🔥' if h_done == len(habits) > 0 else '⏳'}\n\n"
        f"📝 <b>Notes</b>  {len(notes)} saved\n\n"
        f"💼 <b>Business</b>  {len(businesses)} projects  "
        f"💰 ${revenue:,.2f} total revenue\n"
    )

    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎯 Goals",    callback_data="goals"),
         InlineKeyboardButton("💪 Habits",   callback_data="habits")],
        [InlineKeyboardButton("📝 Notes",    callback_data="notes"),
         InlineKeyboardButton("💼 Business", callback_data="business")],
        [InlineKeyboardButton("🤖 Mentor",   callback_data="mentor"),
         InlineKeyboardButton("🏠 Menu",     callback_data="menu")],
    ])
    await send(update, txt, kb)
    return MAIN


# ── Goals ──────────────────────────────────────────────────────────────────────

async def show_goals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
    goals = [g for g in rj(GOALS_FILE) if g.get("status") == "active"]

    if not goals:
        txt = "🎯 <b>Goals</b>\n\nNo active goals yet. Add your first one!"
    else:
        txt = f"🎯 <b>Active Goals</b> ({len(goals)})\n\n"
        for g in goals[:8]:
            pct = g.get("progress", 0)
            txt += (
                f"{p_emoji(g.get('priority','medium'))} <b>{g['title']}</b>\n"
                f"   {bar(pct)} {pct}%"
            )
            if g.get("target_date"):
                txt += f"  📅 {g['target_date']}"
            txt += "\n\n"

    rows = [[InlineKeyboardButton("➕ Add Goal", callback_data="goal_add")]]
    if goals:
        rows.append([InlineKeyboardButton("✏️ Manage Goals", callback_data="goal_manage")])
    rows.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    await send(update, txt, InlineKeyboardMarkup(rows))
    return MAIN


async def goal_manage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    goals = [g for g in rj(GOALS_FILE) if g.get("status") == "active"]
    if not goals:
        await send(update, "No active goals.", back_kb())
        return MAIN
    buttons = [
        [InlineKeyboardButton(
            f"{p_emoji(g.get('priority','medium'))} {g['title'][:32]} ({g.get('progress',0)}%)",
            callback_data=f"goal_view_{g['id']}"
        )] for g in goals[:8]
    ]
    buttons.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    await send(update, "🎯 <b>Select a goal:</b>", InlineKeyboardMarkup(buttons))
    return MAIN


async def goal_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    gid = update.callback_query.data.replace("goal_view_", "")
    g = next((x for x in rj(GOALS_FILE) if x["id"] == gid), None)
    if not g:
        await send(update, "Goal not found.", back_kb())
        return MAIN
    pct = g.get("progress", 0)
    txt = (
        f"🎯 <b>{g['title']}</b>\n\n"
        f"{c_emoji(g.get('category','personal'))} {g.get('category','').title()}  "
        f"{p_emoji(g.get('priority','medium'))} {g.get('priority','').title()} priority\n\n"
        f"Progress: {bar(pct)} <b>{pct}%</b>\n"
    )
    if g.get("description"):
        txt += f"\n📋 {g['description']}\n"
    if g.get("target_date"):
        txt += f"\n📅 Target: {g['target_date']}"
    milestones = g.get("milestones", [])
    if milestones:
        txt += "\n\n<b>Milestones:</b>\n"
        for m in milestones:
            txt += f"  {'✅' if m.get('done') else '⬜'} {m.get('title','')}\n"
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("📈 Update Progress", callback_data=f"goal_prog_{gid}"),
         InlineKeyboardButton("✅ Complete",         callback_data=f"goal_done_{gid}")],
        [InlineKeyboardButton("🗑️ Delete",           callback_data=f"goal_del_{gid}"),
         InlineKeyboardButton("◀️ Back",              callback_data="goal_manage")],
    ])
    await send(update, txt, kb)
    return MAIN


async def goal_prog_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data["edit_gid"] = update.callback_query.data.replace("goal_prog_", "")
    await send(update, "📈 Enter new progress (0–100):",
               InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="goals")]]))
    return GOAL_PROGRESS


async def goal_prog_save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        pct = max(0, min(100, int(update.message.text.strip())))
    except ValueError:
        await update.message.reply_text("Enter a number 0–100.")
        return GOAL_PROGRESS
    gid = context.user_data.get("edit_gid")
    goals = rj(GOALS_FILE)
    for g in goals:
        if g["id"] == gid:
            g["progress"] = pct
            g["updated_at"] = now_iso()
            if pct == 100:
                g["status"] = "completed"
    wj(GOALS_FILE, goals)
    msg = "🎉 Goal completed! Amazing!" if pct == 100 else "✅ Progress updated!"
    await update.message.reply_text(msg, reply_markup=main_menu_kb())
    return MAIN


async def goal_complete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("🎉 Completed!")
    gid = update.callback_query.data.replace("goal_done_", "")
    goals = rj(GOALS_FILE)
    for g in goals:
        if g["id"] == gid:
            g["status"] = "completed"
            g["progress"] = 100
            g["updated_at"] = now_iso()
    wj(GOALS_FILE, goals)
    await send(update, "🎉 <b>Goal completed! You're crushing it!</b>", main_menu_kb())
    return MAIN


async def goal_delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Deleted")
    gid = update.callback_query.data.replace("goal_del_", "")
    wj(GOALS_FILE, [g for g in rj(GOALS_FILE) if g["id"] != gid])
    await send(update, "🗑️ Goal deleted.",
               InlineKeyboardMarkup([[InlineKeyboardButton("🎯 Goals", callback_data="goals"),
                                      InlineKeyboardButton("🏠 Menu",  callback_data="menu")]]))
    return MAIN


async def goal_add_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await send(update, "🎯 <b>Add Goal</b>\n\nWhat's the title of your goal?",
               InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="goals")]]))
    return GOAL_TITLE


async def goal_get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["new_goal"] = {"title": update.message.text.strip()}
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("👤 Personal",     callback_data="gc_personal"),
         InlineKeyboardButton("💪 Health",        callback_data="gc_health")],
        [InlineKeyboardButton("💼 Business",      callback_data="gc_business"),
         InlineKeyboardButton("💰 Financial",     callback_data="gc_financial")],
        [InlineKeyboardButton("📚 Learning",      callback_data="gc_learning"),
         InlineKeyboardButton("❤️ Relationship",  callback_data="gc_relationship")],
    ])
    await update.message.reply_text("Category?", reply_markup=kb)
    return GOAL_CATEGORY


async def goal_get_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data["new_goal"]["category"] = update.callback_query.data.replace("gc_", "")
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("🔴 High",   callback_data="gp_high"),
        InlineKeyboardButton("🟡 Medium", callback_data="gp_medium"),
        InlineKeyboardButton("🟢 Low",    callback_data="gp_low"),
    ]])
    await send(update, "Priority?", kb)
    return GOAL_PRIORITY


async def goal_get_priority(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data["new_goal"]["priority"] = update.callback_query.data.replace("gp_", "")
    await send(update, "📅 Target date? (YYYY-MM-DD or type <code>skip</code>)", parse_mode="HTML")
    return GOAL_DATE


async def goal_get_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text.strip()
    goal = context.user_data["new_goal"]
    goal["target_date"] = None if txt.lower() == "skip" else txt
    goals = rj(GOALS_FILE)
    goals.append({
        "id": str(uuid.uuid4()), "title": goal["title"], "description": "",
        "category": goal.get("category", "personal"),
        "priority": goal.get("priority", "medium"),
        "progress": 0, "target_date": goal.get("target_date"),
        "milestones": [], "status": "active",
        "created_at": now_iso(), "updated_at": now_iso(),
    })
    wj(GOALS_FILE, goals)
    await update.message.reply_text(
        f"✅ <b>Goal added!</b>\n🎯 {goal['title']}",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎯 Goals", callback_data="goals"),
                                            InlineKeyboardButton("🏠 Menu",  callback_data="menu")]]),
    )
    context.user_data.pop("new_goal", None)
    return MAIN


# ── Habits ─────────────────────────────────────────────────────────────────────

async def show_habits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
    habits = rj(HABITS_FILE)
    td = today()

    if not habits:
        txt = "💪 <b>Habits</b>\n\nNo habits yet. Add your first habit!"
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("➕ Add Habit", callback_data="habit_add")],
                                   [InlineKeyboardButton("🏠 Menu", callback_data="menu")]])
    else:
        done = sum(1 for h in habits if td in h.get("completions", {}))
        txt = f"💪 <b>Habits — {date.today().strftime('%b %d')}</b>  {done}/{len(habits)} done\n\n"
        buttons = []
        for h in habits:
            checked = td in h.get("completions", {})
            s = calc_streak(h.get("completions", {}))
            label = f"{'✅' if checked else '⬜'} {h.get('icon','✓')} {h['name']}"
            if s > 1:
                label += f" 🔥{s}"
            act = f"habit_un_{h['id']}" if checked else f"habit_ck_{h['id']}"
            buttons.append([InlineKeyboardButton(label, callback_data=act)])
        buttons.append([
            InlineKeyboardButton("➕ Add",    callback_data="habit_add"),
            InlineKeyboardButton("🗑️ Delete", callback_data="habit_del_menu"),
            InlineKeyboardButton("🏠 Menu",   callback_data="menu"),
        ])
        kb = InlineKeyboardMarkup(buttons)
    await send(update, txt, kb)
    return MAIN


async def habit_toggle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    data = update.callback_query.data
    checking = data.startswith("habit_ck_")
    hid = data.replace("habit_ck_", "").replace("habit_un_", "")
    habits = rj(HABITS_FILE)
    td = today()
    for h in habits:
        if h["id"] == hid:
            comp = h.setdefault("completions", {})
            if checking:
                comp[td] = comp.get(td, 0) + 1
            elif comp.get(td, 0) > 0:
                comp[td] -= 1
                if comp[td] == 0:
                    del comp[td]
    wj(HABITS_FILE, habits)
    await show_habits(update, context)
    return MAIN


async def habit_del_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    habits = rj(HABITS_FILE)
    if not habits:
        await send(update, "No habits to delete.", back_kb("◀️ Back", "habits"))
        return MAIN
    buttons = [[InlineKeyboardButton(f"🗑️ {h.get('icon','✓')} {h['name']}",
                                     callback_data=f"habit_rm_{h['id']}")] for h in habits]
    buttons.append([InlineKeyboardButton("◀️ Back", callback_data="habits")])
    await send(update, "Select habit to delete:", InlineKeyboardMarkup(buttons))
    return MAIN


async def habit_remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Deleted")
    hid = update.callback_query.data.replace("habit_rm_", "")
    wj(HABITS_FILE, [h for h in rj(HABITS_FILE) if h["id"] != hid])
    await send(update, "🗑️ Habit deleted.",
               InlineKeyboardMarkup([[InlineKeyboardButton("💪 Habits", callback_data="habits")]]))
    return MAIN


async def habit_add_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await send(update,
               "💪 <b>Add Habit</b>\n\nWhat habit do you want to build?\n"
               "e.g. <i>Morning workout</i>, <i>Read 30 min</i>, <i>Meditate</i>",
               InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="habits")]]))
    return HABIT_NAME


async def habit_get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["new_habit"] = {"name": update.message.text.strip()}
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("💪 Health",   callback_data="hc_health"),
         InlineKeyboardButton("🧠 Mindset",  callback_data="hc_mindset")],
        [InlineKeyboardButton("💼 Business", callback_data="hc_business"),
         InlineKeyboardButton("📚 Learning", callback_data="hc_learning")],
        [InlineKeyboardButton("👤 Personal", callback_data="hc_personal")],
    ])
    await update.message.reply_text("Category?", reply_markup=kb)
    return HABIT_CATEGORY


async def habit_get_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data["new_habit"]["category"] = update.callback_query.data.replace("hc_", "")
    await send(update, "What emoji icon represents this habit?\n(e.g. 🏃 💧 📖 🧘 ✍️)")
    return HABIT_ICON


async def habit_get_icon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    h = context.user_data["new_habit"]
    h["icon"] = (update.message.text.strip() or "✓")[:4]
    colors = {"health": "#00cfa8", "mindset": "#7c6ff7", "business": "#f59e0b",
              "learning": "#3b82f6", "personal": "#ec4899"}
    habits = rj(HABITS_FILE)
    habits.append({
        "id": str(uuid.uuid4()), "name": h["name"],
        "category": h.get("category", "health"), "frequency": "daily",
        "icon": h["icon"], "color": colors.get(h.get("category", "health"), "#7c6ff7"),
        "completions": {}, "created_at": now_iso(),
    })
    wj(HABITS_FILE, habits)
    await update.message.reply_text(
        f"✅ Habit added!\n{h['icon']} <b>{h['name']}</b>",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💪 Habits", callback_data="habits"),
                                            InlineKeyboardButton("🏠 Menu",   callback_data="menu")]]),
    )
    context.user_data.pop("new_habit", None)
    return MAIN


# ── Notes ──────────────────────────────────────────────────────────────────────

async def show_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
    notes = sorted(rj(NOTES_FILE),
                   key=lambda n: (not n.get("pinned"), n.get("updated_at", "")), reverse=False)
    if not notes:
        txt = "📝 <b>Notes</b>\n\nNo notes yet!"
    else:
        txt = f"📝 <b>Notes</b> ({len(notes)})\n\n"
        for n in notes[:5]:
            pin = "📌" if n.get("pinned") else "📄"
            preview = n.get("content", "")[:60]
            txt += f"{pin} <b>{n['title']}</b>\n   {preview}{'…' if len(n.get('content',''))>60 else ''}\n\n"
    rows = [[InlineKeyboardButton("➕ Add Note", callback_data="note_add")]]
    if notes:
        rows.append([InlineKeyboardButton("📋 All Notes", callback_data="note_list")])
    rows.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    await send(update, txt, InlineKeyboardMarkup(rows))
    return MAIN


async def note_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    notes = sorted(rj(NOTES_FILE),
                   key=lambda n: (not n.get("pinned"), n.get("updated_at", "")), reverse=False)
    if not notes:
        await send(update, "No notes.", back_kb())
        return MAIN
    buttons = [
        [InlineKeyboardButton(f"{'📌' if n.get('pinned') else '📄'} {n['title'][:35]}",
                              callback_data=f"note_v_{n['id']}")] for n in notes[:10]
    ]
    buttons.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    await send(update, "📝 <b>Your Notes:</b>", InlineKeyboardMarkup(buttons))
    return MAIN


async def note_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    nid = update.callback_query.data.replace("note_v_", "")
    n = next((x for x in rj(NOTES_FILE) if x["id"] == nid), None)
    if not n:
        await send(update, "Note not found.", back_kb())
        return MAIN
    pin = "📌" if n.get("pinned") else "📄"
    txt = f"{pin} <b>{n['title']}</b>\n\n{n.get('content', '')}"
    if n.get("tags"):
        txt += "\n\n🏷️ " + " ".join(f"#{t}" for t in n["tags"])
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("📌 Toggle Pin", callback_data=f"note_pin_{nid}"),
         InlineKeyboardButton("🗑️ Delete",     callback_data=f"note_rm_{nid}")],
        [InlineKeyboardButton("◀️ Back",        callback_data="note_list")],
    ])
    await send(update, txt[:4000], kb)
    return MAIN


async def note_pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    nid = update.callback_query.data.replace("note_pin_", "")
    notes = rj(NOTES_FILE)
    for n in notes:
        if n["id"] == nid:
            n["pinned"] = not n.get("pinned", False)
            n["updated_at"] = now_iso()
    wj(NOTES_FILE, notes)
    # Refresh the view via a fake callback
    update.callback_query.data = f"note_v_{nid}"
    await note_view(update, context)
    return MAIN


async def note_delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Deleted")
    nid = update.callback_query.data.replace("note_rm_", "")
    wj(NOTES_FILE, [n for n in rj(NOTES_FILE) if n["id"] != nid])
    await send(update, "🗑️ Note deleted.",
               InlineKeyboardMarkup([[InlineKeyboardButton("📝 Notes", callback_data="notes")]]))
    return MAIN


async def note_add_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await send(update, "📝 <b>Add Note</b>\n\nTitle?",
               InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="notes")]]))
    return NOTE_TITLE


async def note_get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["new_note"] = {"title": update.message.text.strip()}
    await update.message.reply_text("Now write the note content:")
    return NOTE_CONTENT


async def note_get_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    n = context.user_data["new_note"]
    n["content"] = update.message.text.strip()
    notes = rj(NOTES_FILE)
    notes.append({
        "id": str(uuid.uuid4()), "title": n["title"], "content": n["content"],
        "tags": [], "category": "general", "pinned": False,
        "created_at": now_iso(), "updated_at": now_iso(),
    })
    wj(NOTES_FILE, notes)
    await update.message.reply_text(
        f"✅ <b>Note saved!</b>\n📄 {n['title']}",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Notes", callback_data="notes"),
                                            InlineKeyboardButton("🏠 Menu",  callback_data="menu")]]),
    )
    context.user_data.pop("new_note", None)
    return MAIN


# ── Business ───────────────────────────────────────────────────────────────────

async def show_business(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
    bizs = rj(BUSINESS_FILE)
    if not bizs:
        txt = "💼 <b>Business</b>\n\nNo projects yet. Add your first!"
    else:
        total = sum(b.get("revenue", 0) for b in bizs)
        txt = f"💼 <b>Business Dashboard</b>\n💰 Total Revenue: <b>${total:,.2f}</b>\n\n"
        for b in bizs[:5]:
            pct = min(100, int(b["revenue"] / b["revenue_goal"] * 100)) if b.get("revenue_goal") else 0
            pending = sum(1 for t in b.get("tasks", []) if not t.get("done"))
            txt += (
                f"🚀 <b>{b['name']}</b> {'🟢' if b.get('status')=='active' else '⏸️'}\n"
                f"   💰 ${b.get('revenue',0):,.0f} / ${b.get('revenue_goal',0):,.0f}  {bar(pct,6)}\n"
                f"   📋 {pending} pending tasks\n\n"
            )
    rows = [[InlineKeyboardButton("➕ Add Project", callback_data="biz_add")]]
    if bizs:
        rows.append([InlineKeyboardButton("📊 Manage", callback_data="biz_manage")])
    rows.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    await send(update, txt, InlineKeyboardMarkup(rows))
    return MAIN


async def biz_manage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    bizs = rj(BUSINESS_FILE)
    if not bizs:
        await send(update, "No projects.", back_kb())
        return MAIN
    buttons = [[InlineKeyboardButton(f"🚀 {b['name']}", callback_data=f"biz_v_{b['id']}")] for b in bizs[:8]]
    buttons.append([InlineKeyboardButton("🏠 Menu", callback_data="menu")])
    await send(update, "💼 Select a project:", InlineKeyboardMarkup(buttons))
    return MAIN


async def biz_view(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    bid = update.callback_query.data.replace("biz_v_", "")
    context.user_data["cur_bid"] = bid
    b = next((x for x in rj(BUSINESS_FILE) if x["id"] == bid), None)
    if not b:
        await send(update, "Not found.", back_kb())
        return MAIN
    pct = min(100, int(b["revenue"] / b["revenue_goal"] * 100)) if b.get("revenue_goal") else 0
    pending = [t for t in b.get("tasks", []) if not t.get("done")]
    done_ct = sum(1 for t in b.get("tasks", []) if t.get("done"))
    txt = (
        f"🚀 <b>{b['name']}</b>\n"
        f"{b.get('type','').title()}  |  {b.get('status','').title()}\n\n"
        f"💰 ${b.get('revenue',0):,.2f} / ${b.get('revenue_goal',0):,.0f}  {bar(pct)} {pct}%\n\n"
    )
    if b.get("description"):
        txt += f"📋 {b['description']}\n\n"
    if pending:
        txt += "<b>Pending Tasks:</b>\n"
        for t in pending[:5]:
            txt += f"  ⬜ {t.get('title','')}\n"
        txt += "\n"
    if done_ct:
        txt += f"✅ {done_ct} completed tasks\n"
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("💰 Log Revenue", callback_data=f"biz_rev_{bid}"),
         InlineKeyboardButton("➕ Add Task",     callback_data=f"biz_task_{bid}")],
        [InlineKeyboardButton("✅ Done Task",    callback_data=f"biz_td_{bid}"),
         InlineKeyboardButton("🗑️ Delete",        callback_data=f"biz_rm_{bid}")],
        [InlineKeyboardButton("◀️ Back",          callback_data="biz_manage")],
    ])
    await send(update, txt, kb)
    return MAIN


async def biz_rev_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data["cur_bid"] = update.callback_query.data.replace("biz_rev_", "")
    await send(update, "💰 Enter new total revenue (e.g. <code>1500</code>):",
               InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="business")]]))
    return BIZ_REVENUE


async def biz_rev_save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amt = float(update.message.text.strip().replace(",", "").replace("$", ""))
    except ValueError:
        await update.message.reply_text("Enter a valid number.")
        return BIZ_REVENUE
    bid = context.user_data.get("cur_bid")
    bizs = rj(BUSINESS_FILE)
    for b in bizs:
        if b["id"] == bid:
            b["revenue"] = amt
    wj(BUSINESS_FILE, bizs)
    await update.message.reply_text(
        f"✅ Revenue updated to <b>${amt:,.2f}</b>",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💼 Business", callback_data="business"),
                                            InlineKeyboardButton("🏠 Menu",     callback_data="menu")]]),
    )
    return MAIN


async def biz_task_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data["cur_bid"] = update.callback_query.data.replace("biz_task_", "")
    await send(update, "➕ Enter task title:",
               InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="business")]]))
    return BIZ_TASK


async def biz_task_save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    title = update.message.text.strip()
    bid = context.user_data.get("cur_bid")
    bizs = rj(BUSINESS_FILE)
    for b in bizs:
        if b["id"] == bid:
            b.setdefault("tasks", []).append({"id": str(uuid.uuid4()), "title": title, "done": False})
    wj(BUSINESS_FILE, bizs)
    await update.message.reply_text(
        f"✅ Task added: <b>{title}</b>",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💼 Business", callback_data="business"),
                                            InlineKeyboardButton("🏠 Menu",     callback_data="menu")]]),
    )
    return MAIN


async def biz_task_done_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    bid = update.callback_query.data.replace("biz_td_", "")
    context.user_data["cur_bid"] = bid
    b = next((x for x in rj(BUSINESS_FILE) if x["id"] == bid), None)
    pending = [t for t in b.get("tasks", []) if not t.get("done")] if b else []
    if not pending:
        await send(update, "No pending tasks! 🎉",
                   InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data=f"biz_v_{bid}")]]))
        return MAIN
    # callback_data: "biz_tm_{task_id}" — task UUID is 36 chars, prefix 7 → 43 total, safe
    buttons = [[InlineKeyboardButton(f"✅ {t['title'][:40]}", callback_data=f"biz_tm_{t['id']}")] for t in pending[:8]]
    buttons.append([InlineKeyboardButton("◀️ Back", callback_data=f"biz_v_{bid}")])
    await send(update, "Mark task as done:", InlineKeyboardMarkup(buttons))
    return MAIN


async def biz_task_mark(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("✅ Done!")
    tid = update.callback_query.data.replace("biz_tm_", "")
    bid = context.user_data.get("cur_bid")
    bizs = rj(BUSINESS_FILE)
    for b in bizs:
        if b["id"] == bid:
            for t in b.get("tasks", []):
                if t["id"] == tid:
                    t["done"] = True
    wj(BUSINESS_FILE, bizs)
    await send(update, "✅ Task marked complete!",
               InlineKeyboardMarkup([[InlineKeyboardButton("💼 Business", callback_data="business")]]))
    return MAIN


async def biz_delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Deleted")
    bid = update.callback_query.data.replace("biz_rm_", "")
    wj(BUSINESS_FILE, [b for b in rj(BUSINESS_FILE) if b["id"] != bid])
    await send(update, "🗑️ Project deleted.",
               InlineKeyboardMarkup([[InlineKeyboardButton("💼 Business", callback_data="business")]]))
    return MAIN


async def biz_add_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await send(update, "💼 <b>Add Project</b>\n\nProject / business name?",
               InlineKeyboardMarkup([[InlineKeyboardButton("❌ Cancel", callback_data="business")]]))
    return BIZ_NAME


async def biz_get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["new_biz"] = {"name": update.message.text.strip()}
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Project",      callback_data="bt_project"),
         InlineKeyboardButton("👤 Client",        callback_data="bt_client")],
        [InlineKeyboardButton("🏢 Venture",       callback_data="bt_venture"),
         InlineKeyboardButton("💡 Side Hustle",   callback_data="bt_side_hustle")],
    ])
    await update.message.reply_text("Type?", reply_markup=kb)
    return BIZ_TYPE


async def biz_get_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data["new_biz"]["type"] = update.callback_query.data.replace("bt_", "").replace("_", " ")
    await send(update, "💰 Revenue goal? (number or <code>0</code> to skip)")
    return BIZ_GOAL


async def biz_get_goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    b = context.user_data["new_biz"]
    try:
        b["revenue_goal"] = float(update.message.text.strip().replace(",", "").replace("$", ""))
    except ValueError:
        b["revenue_goal"] = 0.0
    bizs = rj(BUSINESS_FILE)
    bizs.append({
        "id": str(uuid.uuid4()), "name": b["name"], "type": b.get("type", "project"),
        "status": "active", "revenue": 0.0, "revenue_goal": b.get("revenue_goal", 0),
        "description": "", "tasks": [], "notes": "", "created_at": now_iso(),
    })
    wj(BUSINESS_FILE, bizs)
    await update.message.reply_text(
        f"✅ <b>{b['name']}</b> added! 💰 Goal: ${b.get('revenue_goal',0):,.0f}",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💼 Business", callback_data="business"),
                                            InlineKeyboardButton("🏠 Menu",     callback_data="menu")]]),
    )
    context.user_data.pop("new_biz", None)
    return MAIN


# ── Mentor ─────────────────────────────────────────────────────────────────────

async def show_mentor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
    history = rj(CHAT_FILE, default=[])
    last = next((m["content"][:180] for m in reversed(history) if m["role"] == "assistant"), None)
    snippet = f"\n\n<i>Last:</i> {last}…" if last else ""
    txt = (
        "🤖 <b>AI Mentor</b> — Claude\n\n"
        "Talk to me about anything:\n"
        "• Goals & how to achieve them\n"
        "• Business strategy\n"
        "• Health & habits\n"
        "• Life challenges & decisions\n\n"
        "<b>Just type your message below.</b>"
        + snippet
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🧹 Clear History", callback_data="mentor_clear"),
         InlineKeyboardButton("🏠 Menu",          callback_data="menu")],
    ])
    await send(update, txt, kb)
    return MENTOR_MODE


async def mentor_clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("History cleared!")
    wj(CHAT_FILE, [])
    await show_mentor(update, context)
    return MENTOR_MODE


async def mentor_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    thinking = await update.message.reply_text("🤖 Thinking…")

    profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    history = rj(CHAT_FILE, default=[])

    lines = [f"- {k}: {v}" for k, v in profile.get("answers", {}).items() if v]
    ctx = ("\n\nWhat I know about you:\n" + "\n".join(lines)) if lines else ""

    system = (
        "You are a world-class life mentor, executive coach, and trusted advisor.\n"
        "You blend the strategic brilliance of Tim Ferriss, the emotional depth of Brené Brown, "
        "and the motivational fire of Tony Robbins.\n\n"
        "Rules:\n"
        "- Give specific, actionable advice tailored to this person\n"
        "- Challenge limiting beliefs with compassion\n"
        "- Ask 1–2 sharp follow-up questions when helpful\n"
        "- Be direct, warm, and occasionally witty\n"
        "- Keep responses to 2–4 paragraphs max\n"
        + ctx
        + f"\n\nToday: {date.today().strftime('%B %d, %Y')}"
    )

    messages = [{"role": m["role"], "content": m["content"]} for m in history[-20:]]
    messages.append({"role": "user", "content": user_text})

    try:
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
        resp = client.messages.create(
            model="claude-sonnet-4-6", max_tokens=1024, system=system, messages=messages
        )
        reply = resp.content[0].text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    history.append({"role": "user",      "content": user_text, "timestamp": now_iso()})
    history.append({"role": "assistant", "content": reply,     "timestamp": now_iso()})
    wj(CHAT_FILE, history)

    await thinking.delete()
    await update.message.reply_text(
        f"🤖 <b>Mentor:</b>\n\n{reply}",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 Main Menu", callback_data="menu")]]),
    )
    return MENTOR_MODE


# ── Onboarding ─────────────────────────────────────────────────────────────────

async def show_onboarding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
    profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    answered = len(profile.get("answers", {}))

    if profile.get("completed_onboarding"):
        txt = f"📋 <b>Your Profile</b>\n\n✅ Complete! ({answered}/{TOTAL_QUESTIONS} answered)\n\n"
        for k in list(profile.get("answers", {}).keys())[:10]:
            v = profile["answers"][k]
            if v:
                txt += f"• <b>{k.replace('_',' ').title()}:</b> {str(v)[:70]}\n"
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔄 Redo Onboarding", callback_data="ob_restart")],
            [InlineKeyboardButton("🏠 Menu", callback_data="menu")],
        ])
    else:
        pct = int(answered / TOTAL_QUESTIONS * 100)
        txt = (
            f"📋 <b>100-Question Profile</b>\n\n"
            f"{bar(pct, 10)} {pct}% ({answered}/{TOTAL_QUESTIONS})\n\n"
            "Answer 100 questions across 10 life areas so your AI mentor can give "
            "you deeply personalized coaching.\n\n"
            "Takes ~15–20 min. You can stop and resume anytime."
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🚀 Start / Continue", callback_data="ob_start")],
            [InlineKeyboardButton("🏠 Menu",             callback_data="menu")],
        ])
    await send(update, txt, kb)
    return MAIN


async def ob_restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    profile["completed_onboarding"] = False
    wj(PROFILE_FILE, profile)
    await show_onboarding(update, context)
    return MAIN


def _next_question_idx(answered_keys: set) -> int | None:
    """Return index of first unanswered question, or None if all done."""
    for i, item in enumerate(ONBOARDING):
        if item["type"] == "q" and item["id"] not in answered_keys:
            return i
    return None


async def ob_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    answered_keys = set(profile.get("answers", {}).keys())
    idx = _next_question_idx(answered_keys)
    if idx is None:
        profile["completed_onboarding"] = True
        wj(PROFILE_FILE, profile)
        await send(update,
                   "🎉 <b>All 100 questions answered!</b>\n\nYour mentor knows you deeply. Let's go!",
                   InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Mentor", callback_data="mentor"),
                                          InlineKeyboardButton("🏠 Menu",   callback_data="menu")]]))
        return MAIN
    context.user_data["ob_idx"] = idx
    await _ask_q(update.callback_query, context, idx)
    return OB_ANSWER


async def _ask_q(query_or_cb, context: ContextTypes.DEFAULT_TYPE, idx: int):
    """Send the question at ONBOARDING[idx], preceded by section header if needed."""
    profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
    answered = len(profile.get("answers", {}))
    pct = int(answered / TOTAL_QUESTIONS * 100)
    q_num = sum(1 for i in ONBOARDING[:idx + 1] if i["type"] == "q")

    # If this question is preceded by a header (idx-1 is header), prepend it
    header = ""
    if idx > 0 and ONBOARDING[idx - 1]["type"] == "header":
        header = f"\n<b>{ONBOARDING[idx - 1]['title']}</b>\n\n"

    item = ONBOARDING[idx]
    txt = (
        f"📋 {bar(pct, 10)} {pct}%  Q{q_num}/{TOTAL_QUESTIONS}"
        + header
        + f"\n\n<b>{item['text']}</b>"
    )
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("⏭️ Skip", callback_data="ob_skip"),
        InlineKeyboardButton("⏹️ Stop", callback_data="ob_stop"),
    ]])
    if hasattr(query_or_cb, "edit_message_text"):
        try:
            await query_or_cb.edit_message_text(txt, parse_mode="HTML", reply_markup=kb)
            return
        except Exception:
            msg = query_or_cb.message
    else:
        msg = query_or_cb
    await msg.reply_text(txt, parse_mode="HTML", reply_markup=kb)


async def ob_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        await update.callback_query.answer()
        action = update.callback_query.data

        if action == "ob_stop":
            await send(update,
                       "⏸️ Paused. Progress saved!\nResume via <b>Profile / Onboarding</b>.",
                       InlineKeyboardMarkup([[InlineKeyboardButton("🏠 Menu", callback_data="menu")]]))
            return MAIN

        if action == "ob_skip":
            idx = context.user_data.get("ob_idx", 0) + 1
        else:
            return OB_ANSWER  # unknown cb, ignore

    else:
        # Text answer
        ans = update.message.text.strip()
        idx = context.user_data.get("ob_idx", 0)
        item = ONBOARDING[idx] if idx < len(ONBOARDING) else None
        if item and item["type"] == "q":
            profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
            profile.setdefault("answers", {})[item["id"]] = ans
            wj(PROFILE_FILE, profile)
        idx += 1

    # Advance past any headers
    while idx < len(ONBOARDING) and ONBOARDING[idx]["type"] == "header":
        idx += 1

    if idx >= len(ONBOARDING):
        profile = rj(PROFILE_FILE, default={"answers": {}, "completed_onboarding": False})
        profile["completed_onboarding"] = True
        wj(PROFILE_FILE, profile)
        finish_kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🤖 Talk to Mentor", callback_data="mentor")],
            [InlineKeyboardButton("🏠 Main Menu",      callback_data="menu")],
        ])
        txt = (
            "🎉 <b>Profile complete! All 100 questions answered!</b>\n\n"
            "Your AI mentor now knows you deeply and will give you truly personalized coaching. "
            "Let's crush your goals!"
        )
        if update.callback_query:
            await update.callback_query.edit_message_text(txt, parse_mode="HTML", reply_markup=finish_kb)
        else:
            await update.message.reply_text(txt, parse_mode="HTML", reply_markup=finish_kb)
        return MAIN

    context.user_data["ob_idx"] = idx
    source = update.callback_query if update.callback_query else update.message
    await _ask_q(source, context, idx)
    return OB_ANSWER


# ── Bot setup ──────────────────────────────────────────────────────────────────

def build_app() -> Application:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN not set in environment")

    application = Application.builder().token(token).build()

    # All navigation callbacks allowed in MAIN state
    main_nav = [
        CallbackQueryHandler(show_overview,      pattern="^overview$"),
        CallbackQueryHandler(show_goals,         pattern="^goals$"),
        CallbackQueryHandler(goal_manage,        pattern="^goal_manage$"),
        CallbackQueryHandler(goal_view,          pattern="^goal_view_"),
        CallbackQueryHandler(goal_prog_start,    pattern="^goal_prog_"),
        CallbackQueryHandler(goal_complete,      pattern="^goal_done_"),
        CallbackQueryHandler(goal_delete,        pattern="^goal_del_"),
        CallbackQueryHandler(goal_add_start,     pattern="^goal_add$"),
        CallbackQueryHandler(show_habits,        pattern="^habits$"),
        CallbackQueryHandler(habit_toggle,       pattern="^habit_(ck|un)_"),
        CallbackQueryHandler(habit_del_menu,     pattern="^habit_del_menu$"),
        CallbackQueryHandler(habit_remove,       pattern="^habit_rm_"),
        CallbackQueryHandler(habit_add_start,    pattern="^habit_add$"),
        CallbackQueryHandler(show_notes,         pattern="^notes$"),
        CallbackQueryHandler(note_list,          pattern="^note_list$"),
        CallbackQueryHandler(note_view,          pattern="^note_v_"),
        CallbackQueryHandler(note_pin,           pattern="^note_pin_"),
        CallbackQueryHandler(note_delete,        pattern="^note_rm_"),
        CallbackQueryHandler(note_add_start,     pattern="^note_add$"),
        CallbackQueryHandler(show_business,      pattern="^business$"),
        CallbackQueryHandler(biz_manage,         pattern="^biz_manage$"),
        CallbackQueryHandler(biz_view,           pattern="^biz_v_"),
        CallbackQueryHandler(biz_rev_start,      pattern="^biz_rev_"),
        CallbackQueryHandler(biz_task_start,     pattern="^biz_task_"),
        CallbackQueryHandler(biz_task_done_menu, pattern="^biz_td_"),
        CallbackQueryHandler(biz_task_mark,      pattern="^biz_tm_"),
        CallbackQueryHandler(biz_delete,         pattern="^biz_rm_"),
        CallbackQueryHandler(biz_add_start,      pattern="^biz_add$"),
        CallbackQueryHandler(show_mentor,        pattern="^mentor$"),
        CallbackQueryHandler(show_onboarding,    pattern="^onboarding$"),
        CallbackQueryHandler(ob_restart,         pattern="^ob_restart$"),
        CallbackQueryHandler(ob_start,           pattern="^ob_start$"),
        CallbackQueryHandler(cb_menu,            pattern="^menu$"),
    ]

    conv = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            CommandHandler("menu",  cmd_menu),
        ],
        states={
            MAIN: main_nav,

            GOAL_TITLE:    [MessageHandler(filters.TEXT & ~filters.COMMAND, goal_get_title),
                            *main_nav],
            GOAL_CATEGORY: [CallbackQueryHandler(goal_get_category, pattern="^gc_"), *main_nav],
            GOAL_PRIORITY: [CallbackQueryHandler(goal_get_priority, pattern="^gp_"), *main_nav],
            GOAL_DATE:     [MessageHandler(filters.TEXT & ~filters.COMMAND, goal_get_date),
                            *main_nav],
            GOAL_PROGRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, goal_prog_save),
                            *main_nav],

            HABIT_NAME:     [MessageHandler(filters.TEXT & ~filters.COMMAND, habit_get_name),
                             *main_nav],
            HABIT_CATEGORY: [CallbackQueryHandler(habit_get_category, pattern="^hc_"), *main_nav],
            HABIT_ICON:     [MessageHandler(filters.TEXT & ~filters.COMMAND, habit_get_icon),
                             *main_nav],

            NOTE_TITLE:   [MessageHandler(filters.TEXT & ~filters.COMMAND, note_get_title),
                           *main_nav],
            NOTE_CONTENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, note_get_content),
                           *main_nav],

            BIZ_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, biz_get_name), *main_nav],
            BIZ_TYPE: [CallbackQueryHandler(biz_get_type, pattern="^bt_"), *main_nav],
            BIZ_GOAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, biz_get_goal), *main_nav],
            BIZ_REVENUE: [MessageHandler(filters.TEXT & ~filters.COMMAND, biz_rev_save),
                          *main_nav],
            BIZ_TASK: [MessageHandler(filters.TEXT & ~filters.COMMAND, biz_task_save),
                       *main_nav],

            MENTOR_MODE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, mentor_msg),
                CallbackQueryHandler(mentor_clear, pattern="^mentor_clear$"),
                *main_nav,
            ],

            OB_ANSWER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, ob_answer),
                CallbackQueryHandler(ob_answer, pattern="^ob_(skip|stop)$"),
                *main_nav,
            ],
        },
        fallbacks=[
            CommandHandler("start", start),
            CommandHandler("menu",  cmd_menu),
        ],
        allow_reentry=True,
    )

    application.add_handler(conv)
    return application


def main():
    app = build_app()
    logger.info("🤖 Personal Dashboard Bot is running…")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
