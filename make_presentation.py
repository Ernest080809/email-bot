from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import pptx.util as util

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

DARK_BG    = RGBColor(0x1A, 0x1A, 0x2E)
ACCENT     = RGBColor(0xC0, 0x39, 0x2B)   # deep red
GOLD       = RGBColor(0xD4, 0xA0, 0x17)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xDD, 0xDD, 0xDD)

def set_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_textbox(slide, text, left, top, width, height,
                font_size=20, bold=False, color=WHITE,
                align=PP_ALIGN.LEFT, italic=False):
    txBox = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox

def add_accent_bar(slide, top, height=0.07, color=ACCENT):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(0), Inches(top), Inches(13.33), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()

def add_bullet_box(slide, items, left, top, width, height,
                   font_size=19, color=LIGHT_GRAY, bullet="▸ "):
    txBox = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_before = Pt(6)
        run = p.add_run()
        run.text = bullet + item
        run.font.size = Pt(font_size)
        run.font.color.rgb = color

# ── SLIDE 1: Title ──────────────────────────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
set_bg(slide, DARK_BG)
add_accent_bar(slide, 0, 0.5, ACCENT)
add_accent_bar(slide, 7.0, 0.5, ACCENT)

add_textbox(slide, "ЕВРЕЙСКИЕ ПОГРОМЫ В РОССИЙСКОЙ ИМПЕРИИ",
            0.5, 1.2, 12.3, 1.5, font_size=36, bold=True,
            color=WHITE, align=PP_ALIGN.CENTER)
add_textbox(slide, "1881–1906 годы: причины, события, последствия",
            0.5, 2.9, 12.3, 0.7, font_size=22, italic=True,
            color=GOLD, align=PP_ALIGN.CENTER)
add_textbox(slide, "История • Россия • XIX–XX вв.",
            0.5, 5.8, 12.3, 0.6, font_size=16,
            color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

# ── SLIDE 2: Что такое погром ────────────────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, GOLD)
add_textbox(slide, "ЧТО ТАКОЕ ПОГРОМ?",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True,
            color=WHITE, align=PP_ALIGN.LEFT)

add_bullet_box(slide, [
    "Слово «погром» происходит от русского «громить» — разрушать, уничтожать.",
    "Массовое насилие в отношении этнической или религиозной группы, как правило организованное или попустительствуемое властями.",
    "Термин вошёл в международный оборот именно благодаря событиям в Российской империи и сегодня используется в большинстве языков мира.",
    "Включал убийства, изнасилования, поджоги домов и лавок, грабёж имущества.",
    "Жертвами становилось еврейское население черты оседлости — территорий, где евреям разрешалось проживать.",
], 0.6, 1.4, 12.0, 5.5, font_size=20)

# ── SLIDE 3: Исторический контекст ──────────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, GOLD)
add_textbox(slide, "ИСТОРИЧЕСКИЙ КОНТЕКСТ",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True, color=WHITE)

add_textbox(slide, "Черта оседлости (1791–1917)",
            0.6, 1.3, 11.5, 0.5, font_size=22, bold=True, color=GOLD)
add_bullet_box(slide, [
    "Около 5 миллионов евреев были обязаны жить в западных губерниях империи.",
    "Ограничения в образовании (процентная норма), запрет на многие профессии, принудительный воинский призыв.",
    "Экономическое и правовое бесправие создавало напряжённость между еврейским и нееврейским населением.",
], 0.6, 1.8, 12.0, 2.0, font_size=18)

add_textbox(slide, "Политическая обстановка",
            0.6, 3.9, 11.5, 0.5, font_size=22, bold=True, color=GOLD)
add_bullet_box(slide, [
    "Убийство Александра II (1881) властями использовалось для разжигания антисемитских настроений.",
    "Государственный антисемитизм: «Майские законы» 1882 года ужесточили ограничения.",
    "Православная церковь и националистическая пресса активно распространяли антисемитские мифы.",
], 0.6, 4.4, 12.0, 2.5, font_size=18)

# ── SLIDE 4: Три волны (хронология) ─────────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, GOLD)
add_textbox(slide, "ТРИ ВОЛНЫ ПОГРОМОВ",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True, color=WHITE)

waves = [
    ("I волна  1881–1884", ACCENT,
     "После убийства Александра II. Охватила более 200 городов и местечек.\n"
     "Одесса, Киев, Елисаветград. Тысячи семей разорены, сотни убиты."),
    ("II волна  1903–1906", ACCENT,
     "Кишинёвский погром 1903 г.: 49 убитых, 586 раненых — международный резонанс.\n"
     "Погром в Кишинёве организован при прямом участии полиции и властей.\n"
     "Октябрьские погромы 1905 г. — более 600 городов, свыше 3 000 убитых."),
    ("III волна  1918–1921", GOLD,
     "Гражданская война. Самая кровопролитная: ок. 50–200 тыс. погибших.\n"
     "Участники: белые армии, петлюровцы, банды атаманов, красные части."),
]

for i, (title, tc, body) in enumerate(waves):
    y = 1.3 + i * 1.9
    shape = slide.shapes.add_shape(1,
        Inches(0.4), Inches(y), Inches(12.5), Inches(1.7))
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(0x2C, 0x2C, 0x4A)
    shape.line.color.rgb = tc
    add_textbox(slide, title, 0.6, y + 0.05, 4.0, 0.5,
                font_size=20, bold=True, color=tc)
    add_textbox(slide, body, 0.6, y + 0.55, 12.0, 1.1,
                font_size=16, color=LIGHT_GRAY)

# ── SLIDE 5: Как проходили погромы ──────────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, ACCENT)
add_textbox(slide, "КАК ПРОХОДИЛИ ПОГРОМЫ",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True, color=WHITE)

add_textbox(slide, "Типичный сценарий", 0.6, 1.3, 5.5, 0.5,
            font_size=22, bold=True, color=GOLD)
add_bullet_box(slide, [
    "Провокация или ложный слух (обвинения в ритуальных убийствах, «кровавый навет»).",
    "Толпа горожан и крестьян нападала на еврейский квартал.",
    "Полиция бездействовала или сама участвовала в насилии.",
    "Дома и синагоги поджигались, имущество разграблялось.",
    "Через 2–3 дня власти «восстанавливали порядок», виновные редко наказывались.",
], 0.6, 1.8, 5.5, 4.5, font_size=17)

add_textbox(slide, "Роль государства", 7.0, 1.3, 5.7, 0.5,
            font_size=22, bold=True, color=GOLD)
add_bullet_box(slide, [
    "«Чёрная сотня» — монархические организации, организовывавшие нападения.",
    "Министерство внутренних дел нередко знало о готовящихся погромах.",
    "«Протоколы сионских мудрецов» (1903) — антисемитская фальшивка, распространявшаяся охранкой.",
    "Суды выносили мягкие приговоры погромщикам или оправдывали их.",
    "Евреев же обвиняли в «провоцировании» насилия.",
], 7.0, 1.8, 5.7, 4.5, font_size=17)

# ── SLIDE 6: Кишинёвский погром (детальный пример) ──────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, ACCENT)
add_textbox(slide, "КИШИНЁВСКИЙ ПОГРОМ 1903 ГОДА",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True, color=WHITE)

add_textbox(slide, "Крупнейший погром эпохи — поворотный момент в мировой истории",
            0.6, 1.2, 12.0, 0.5, font_size=18, italic=True, color=GOLD)

add_bullet_box(slide, [
    "Дата: 19–20 апреля 1903 г. (Пасха по православному календарю).",
    "Поводом послужили ложные обвинения в ритуальном убийстве христианского мальчика.",
    "Губернатор фон Раабен заранее знал о погроме и не принял мер.",
    "Погибли 49 человек, 586 ранены, разрушено более 700 домов и 600 лавок.",
    "Около 2 000 семей лишились крова.",
    "Международная реакция: протесты в США, Великобритании, Франции.",
    "Поэт Хаим Нахман Бялик написал поэму «В городе резни» — обвинение в пассивности жертв.",
    "Погром ускорил эмиграцию евреев в США и Палестину, стал импульсом для сионистского движения.",
], 0.6, 1.8, 12.0, 5.3, font_size=18)

# ── SLIDE 7: Последствия ─────────────────────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, GOLD)
add_textbox(slide, "ПОСЛЕДСТВИЯ И ЗНАЧЕНИЕ",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True, color=WHITE)

cols = [
    ("Демографические", [
        "1881–1914: более 2 млн евреев эмигрировали из России, прежде всего в США.",
        "Общины местечек были уничтожены или рассеяны.",
        "Рост еврейского населения в Нью-Йорке, Чикаго, Лондоне.",
    ]),
    ("Политические", [
        "Погромы дали мощный импульс сионизму (Теодор Герцль, I Сионистский конгресс 1897).",
        "Усиление еврейского самообороны — организация «Бунд».",
        "Международное осуждение царского режима.",
    ]),
    ("Исторические", [
        "Погромы стали прообразом геноцидной политики XX века.",
        "Опыт погромов учитывался при планировании Холокоста нацистской Германией.",
        "Слово «погром» вошло во все мировые языки как термин для обозначения организованного насилия.",
    ]),
]
for i, (title, items) in enumerate(cols):
    x = 0.4 + i * 4.3
    add_textbox(slide, title, x, 1.3, 4.0, 0.5,
                font_size=20, bold=True, color=GOLD)
    add_bullet_box(slide, items, x, 1.85, 4.1, 4.5, font_size=16, bullet="• ")

# ── SLIDE 8: Самооборона и сопротивление ─────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, GOLD)
add_textbox(slide, "СОПРОТИВЛЕНИЕ И САМООБОРОНА",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True, color=WHITE)

add_bullet_box(slide, [
    "После погромов 1881 г. возникли первые отряды еврейской самообороны в Одессе и Варшаве.",
    "Бунд (Всеобщий еврейский рабочий союз, осн. 1897) создавал боевые дружины.",
    "В 1903–1905 гг. самооборона действовала в десятках городов; в Гомеле в 1903 г. евреи впервые дали организованный отпор.",
    "Это изменило образ «пассивной жертвы» и заложило основы для еврейских воинских традиций.",
    "Хаим Нахман Бялик в поэме «В городе резни» призывал к отказу от пассивности.",
    "Идеи самозащиты стали частью сионистской идеологии и впоследствии — основой Хаганы в Палестине.",
], 0.6, 1.3, 12.0, 5.5, font_size=20)

# ── SLIDE 9: Память и уроки истории ─────────────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 1.1, 0.06, ACCENT)
add_textbox(slide, "ПАМЯТЬ И УРОКИ ИСТОРИИ",
            0.5, 0.2, 12.0, 0.8, font_size=30, bold=True, color=WHITE)

add_bullet_box(slide, [
    "Погромы в Российской империи — одна из первых массовых этнических чисток в Новейшей истории.",
    "Они показали, как государство может использовать или поощрять этническое насилие в политических целях.",
    "Память о погромах вошла в коллективную память еврейского народа наравне с Холокостом.",
    "Термин «погром» используется ООН и правозащитными организациями как обозначение организованного насилия.",
    "Изучение погромов помогает понять механизмы геноцида и важность защиты прав меньшинств.",
    "Страны-преемники Российской империи официально признали погромы преступлениями.",
], 0.6, 1.3, 12.0, 5.5, font_size=20)

# ── SLIDE 10: Заключение / итоговый слайд ───────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
add_accent_bar(slide, 0, 0.5, ACCENT)
add_accent_bar(slide, 7.0, 0.5, ACCENT)

add_textbox(slide, "ИТОГИ",
            0.5, 0.7, 12.3, 0.8, font_size=34, bold=True,
            color=WHITE, align=PP_ALIGN.CENTER)

add_bullet_box(slide, [
    "Погромы были не стихийными вспышками, а систематическим государственным террором.",
    "Они уничтожили тысячи жизней и общин, изменив демографию целого региона.",
    "Погромы дали импульс еврейской эмиграции, сионизму и движению за самооборону.",
    "Их наследие — в понимании того, как ненависть, укоренённая в законе и культуре, ведёт к массовому насилию.",
    "«Те, кто не помнит прошлого, обречены пережить его вновь.»  — Джордж Сантаяна",
], 0.8, 1.7, 11.8, 4.8, font_size=20)

add_textbox(slide, "Источники: Энциклопедия Холокоста (Яд Вашем) • YIVO Encyclopedia • Шаул Штампфер, Джон Д. Клир",
            0.5, 6.5, 12.3, 0.6, font_size=13, italic=True,
            color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

# ── Save ─────────────────────────────────────────────────────────────────────
out = "/home/user/email-bot/pogroms_presentation.pptx"
prs.save(out)
print(f"Saved: {out}")
