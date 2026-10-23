import math, os

OUT = os.path.dirname(os.path.abspath(__file__))

BG = "#0c1018"
PANEL = "#141a26"
LINE = "#2a3446"
TEXT = "#e8ecf3"
MUTED = "#8d97a8"
GOLD = "#f2c14e"

# Clockwise from the top, as in the sketch.
TYPES = [
    ("Fire", "#e0443a"),
    ("Frost", "#3b9bf0"),
    ("Nature", "#8fd13a"),
    ("Lightning", "#a35ee0"),
    ("Physical", "#a0703f"),
    ("Air", "#bfc5cf"),
]
MIN, MAX = -30, 30
RINGS = [-20, -10, 0, 10, 20, 30]


def angle(i):
    return math.radians(-90 + 60 * i)


def pt(cx, cy, r, i):
    a = angle(i)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def radius(value, R):
    return R * (value - MIN) / (MAX - MIN)


def poly(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def hexagon(cx, cy, R, profile=None, fill=GOLD, labels=True, scale_labels=True, dot=16, font=22, sub=None):
    """The affinity chart: rings, spokes, colored type dots, and an optional profile shape."""
    s = []
    for v in RINGS:
        r = radius(v, R)
        pts = [pt(cx, cy, r, i) for i in range(6)]
        if v == 0:
            s.append(f'<polygon points="{poly(pts)}" fill="none" stroke="{GOLD}" stroke-width="2" '
                     f'stroke-dasharray="7 6" opacity="0.85"/>')
        elif v == MAX:
            s.append(f'<polygon points="{poly(pts)}" fill="#111725" stroke="#5b6880" stroke-width="3"/>')
        else:
            s.append(f'<polygon points="{poly(pts)}" fill="none" stroke="{LINE}" stroke-width="1.5"/>')
    # Outer ring drawn first so the fill sits under the inner rings: redraw inner rings on top.
    s.insert(0, s.pop(len(RINGS) - 1))
    for i in range(6):
        x, y = pt(cx, cy, R, i)
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1.5"/>')

    if scale_labels:
        # Ring values along the spoke between Air and Fire (upper left), out of the profile's way.
        for v in RINGS:
            r = radius(v, R)
            a = math.radians(-120)
            x, y = cx + r * math.cos(a), cy + r * math.sin(a)
            color = GOLD if v == 0 else MUTED
            label = "0%" if v == 0 else f"{v:+d}%"
            s.append(f'<text x="{x - 8:.1f}" y="{y + 5:.1f}" font-size="{font - 7}" fill="{color}" '
                     f'text-anchor="end" font-weight="600">{label}</text>')
        s.append(f'<text x="{cx - 10}" y="{cy + 5}" font-size="{font - 7}" fill="{MUTED}" text-anchor="end">−30%</text>')

    if profile:
        pts = [pt(cx, cy, radius(profile[name], R), i) for i, (name, _) in enumerate(TYPES)]
        s.append(f'<polygon points="{poly(pts)}" fill="{fill}" fill-opacity="0.22" stroke="{fill}" '
                 f'stroke-width="3.5" stroke-linejoin="round"/>')
        for (x, y), (name, color) in zip(pts, TYPES):
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{fill}" stroke="{BG}" stroke-width="2"/>')

    for i, (name, color) in enumerate(TYPES):
        x, y = pt(cx, cy, R + dot + 14, i)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{dot + 7}" fill="{color}" opacity="0.18"/>')
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{dot}" fill="{color}"/>')
        if labels:
            lx, ly = pt(cx, cy, R + dot * 2 + 34, i)
            anchor = "middle"
            if i in (1, 2):
                anchor = "start"
                lx -= 10
            if i in (4, 5):
                anchor = "end"
                lx += 10
            if i == 0:
                ly -= 4
            if i == 3:
                ly += 12
            text = name if not profile or not sub else f"{name} {profile[name]:+d}%" if profile[name] else f"{name} 0%"
            s.append(f'<text x="{lx:.1f}" y="{ly + font * 0.35:.1f}" font-size="{font}" fill="{color}" '
                     f'text-anchor="{anchor}" font-weight="700">{text}</text>')
    return "\n".join(s)


def page(w, h, body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;background:{BG};}}
svg{{display:block;font-family:'Segoe UI',system-ui,sans-serif;}}
</style></head><body><svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="{BG}"/>
{body}
</svg></body></html>"""


def wrap(x, y, lines, size, color=TEXT, weight=400, gap=1.4, anchor="start"):
    out = []
    for k, line in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + k * size * gap:.1f}" font-size="{size}" fill="{color}" '
                   f'font-weight="{weight}" text-anchor="{anchor}">{line}</text>')
    return "\n".join(out)


def panel(x, y, w, h, accent=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>'
    if accent:
        s += f'<rect x="{x}" y="{y + 14}" width="4" height="{h - 28}" rx="2" fill="{accent}"/>'
    return s


def color_of(name):
    return dict(TYPES)[name]


# ---------------------------------------------------------------- Image 1: the system

def image_system():
    W, H = 1600, 1000
    example = {"Fire": 25, "Frost": -30, "Nature": -15, "Lightning": 15, "Physical": -5, "Air": 5}
    cx, cy, R = 600, 575, 280
    b = []
    b.append(wrap(70, 92, ["SPELL AFFINITY"], 46, GOLD, 800))
    b.append(wrap(72, 132, ["Each hero leans toward some damage types and away from others. "
                            "Spells of a type deal more or less damage by that hero's affinity."], 20, MUTED))

    b.append(hexagon(cx, cy, R, example, fill=GOLD))
    b.append(f'<text x="{cx}" y="{cy + R + 118}" font-size="17" fill="{MUTED}" text-anchor="middle">'
             f'Example profile (gold shape): strong with Fire and Lightning, weak with Frost and Nature</text>')

    # Conversion arrow: Physical -> Fire, a circular arc around the outside of the Air corner.
    b.append('<defs><marker id="head" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" '
             'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#e0443a"/></marker>'
             '<linearGradient id="conv" x1="0" y1="1" x2="0.3" y2="0"><stop offset="0" stop-color="#a0703f"/>'
             '<stop offset="1" stop-color="#e0443a"/></linearGradient></defs>')
    ra = R + 125
    a0, a1 = math.radians(150 + 7), math.radians(242)
    x0, y0 = cx + ra * math.cos(a0), cy + ra * math.sin(a0)
    x1, y1 = cx + ra * math.cos(a1), cy + ra * math.sin(a1)
    # Then bend in to the Fire dot, arriving from the left.
    fx, fy = pt(cx, cy, R + 30, 0)
    tx, ty = fx - 34, fy
    qx, qy = cx + ra * math.cos(math.radians(262)), cy + ra * math.sin(math.radians(262))
    b.append(f'<path d="M{x0:.1f},{y0:.1f} A{ra},{ra} 0 0 1 {x1:.1f},{y1:.1f} Q{qx:.1f},{qy:.1f} {tx:.1f},{ty:.1f}" '
             f'fill="none" stroke="url(#conv)" stroke-width="5" stroke-dasharray="14 9" stroke-linecap="round" '
             f'marker-end="url(#head)"/>')
    lx, ly = cx + (ra + 100) * math.cos(math.radians(205)), cy + (ra + 100) * math.sin(math.radians(205))
    b.append(wrap(lx, ly - 6, ["Conversion mod"], 16, MUTED, 600, anchor="middle"))
    b.append(f'<text x="{lx:.1f}" y="{ly + 18:.1f}" font-size="19" font-weight="800" text-anchor="middle">'
             f'<tspan fill="#c08850">Physical</tspan><tspan fill="{TEXT}"> → </tspan><tspan fill="#ff6a5e">Fire</tspan></text>')

    # Right column
    X, Wp = 1010, 530
    b.append(panel(X, 190, Wp, 250, GOLD))
    b.append(wrap(X + 30, 232, ["HOW TO READ IT"], 18, GOLD, 800))
    b.append(wrap(X + 30, 272, [
        "Six damage types, one per corner.",
        "Rings are the damage bonus for that type:",
        "centre −30%, edge +30%.",
        f'<tspan fill="{GOLD}" font-weight="700">Gold dashed ring = 0%</tspan> (neutral).',
        "Outside it: stronger. Inside it: weaker.",
    ], 19, TEXT, 400, 1.45))

    b.append(panel(X, 465, Wp, 420, "#e0443a"))
    b.append(wrap(X + 30, 507, ["DAMAGE CONVERSION (MOD EXAMPLE)"], 18, GOLD, 800))
    # Mod card
    b.append(f'<rect x="{X + 30}" y="527" width="{Wp - 60}" height="72" rx="10" fill="#0f1420" stroke="#3a2a22"/>')
    b.append(f'<rect x="{X + 46}" y="541" width="44" height="44" rx="8" fill="#2d1a14" stroke="#e0443a" stroke-width="2"/>')
    b.append(f'<circle cx="{X + 57}" cy="563" r="7" fill="#a0703f"/><circle cx="{X + 79}" cy="563" r="7" fill="#e0443a"/>'
             f'<path d="M{X + 63},563 L{X + 70},563" stroke="{TEXT}" stroke-width="2"/>'
             f'<path d="M{X + 68},559 L{X + 72},563 L{X + 68},567" stroke="{TEXT}" stroke-width="2" fill="none"/>')
    b.append(wrap(X + 106, 557, ["Kindling (mod)"], 20, TEXT, 700))
    b.append(wrap(X + 106, 584, ["Converts 50% of Physical damage to Fire"], 17, MUTED))

    # Bars: before / after
    bx, bw = X + 30, Wp - 60
    phys, fire = color_of("Physical"), color_of("Fire")
    b.append(wrap(bx, 633, ["Projectile, 100 damage, without the mod"], 16, MUTED))
    b.append(f'<rect x="{bx}" y="643" width="{bw}" height="34" rx="6" fill="{phys}"/>')
    b.append(f'<text x="{bx + bw / 2}" y="666" font-size="17" fill="#fff" text-anchor="middle" font-weight="700">100 Physical</text>')
    b.append(wrap(bx, 711, ["with Kindling"], 16, MUTED))
    b.append(f'<rect x="{bx}" y="721" width="{bw / 2 - 3}" height="34" rx="6" fill="{phys}"/>')
    b.append(f'<rect x="{bx + bw / 2 + 3}" y="721" width="{bw / 2 - 3}" height="34" rx="6" fill="{fire}"/>')
    b.append(f'<text x="{bx + bw / 4}" y="744" font-size="17" fill="#fff" text-anchor="middle" font-weight="700">50 Physical</text>')
    b.append(f'<text x="{bx + bw * 3 / 4}" y="744" font-size="17" fill="#fff" text-anchor="middle" font-weight="700">50 Fire</text>')
    b.append(wrap(bx, 795, [
        "Each part then uses the hero's affinity for its type.",
        f'With the example profile: 50 × 95% + 50 × 125% = <tspan fill="{GOLD}" font-weight="700">110</tspan>',
        f'instead of 100 × 95% = 95. Builds can chase a hero\'s strong types.',
    ], 16, TEXT, 400, 1.5))
    return page(W, H, "\n".join(b))


# ---------------------------------------------------------------- Image 2: heroes

def fireball(x, y):
    return f"""<defs><radialGradient id="fb" cx="0.6" cy="0.5" r="0.6"><stop offset="0" stop-color="#fff3b0"/>
<stop offset="0.35" stop-color="#ffd23f"/><stop offset="0.7" stop-color="#ff8c1a"/><stop offset="1" stop-color="#e0443a"/></radialGradient>
<linearGradient id="fbt" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#ff8c1a" stop-opacity="0.9"/>
<stop offset="1" stop-color="#e0443a" stop-opacity="0"/></linearGradient></defs>
<path d="M{x - 95},{y - 6} Q{x - 40},{y - 30} {x + 6},{y - 22} L{x + 6},{y + 22} Q{x - 40},{y + 30} {x - 95},{y + 6} Z" fill="url(#fbt)"/>
<path d="M{x - 70},{y - 16} Q{x - 30},{y - 12} {x},{y - 8}" stroke="#ffd23f" stroke-width="4" fill="none" opacity="0.7"/>
<circle cx="{x + 14}" cy="{y}" r="27" fill="url(#fb)"/>"""


def ice_shard(x, y):
    return f"""<defs><linearGradient id="ice" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f2f8ff"/>
<stop offset="0.5" stop-color="#6cc4ff"/><stop offset="1" stop-color="#1f6feb"/></linearGradient>
<linearGradient id="icet" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#6cc4ff" stop-opacity="0.8"/>
<stop offset="1" stop-color="#6cc4ff" stop-opacity="0"/></linearGradient></defs>
<path d="M{x - 95},{y - 3} L{x - 10},{y - 14} L{x - 10},{y + 14} L{x - 95},{y + 3} Z" fill="url(#icet)"/>
<circle cx="{x - 60}" cy="{y - 20}" r="3" fill="#f2f8ff"/><circle cx="{x - 35}" cy="{y + 21}" r="2.5" fill="#f2f8ff"/>
<circle cx="{x - 80}" cy="{y + 14}" r="2" fill="#bfe6ff"/>
<polygon points="{x + 48},{y} {x + 4},{y - 20} {x - 18},{y} {x + 4},{y + 20}" fill="url(#ice)" stroke="#f2f8ff" stroke-width="2"/>
<line x1="{x - 18}" y1="{y}" x2="{x + 48}" y2="{y}" stroke="#f2f8ff" stroke-width="1.5" opacity="0.7"/>"""


def arrow(x, y):
    return f"""<line x1="{x - 92}" y1="{y}" x2="{x + 30}" y2="{y}" stroke="#8a6a45" stroke-width="5" stroke-linecap="round"/>
<polygon points="{x + 52},{y} {x + 26},{y - 13} {x + 32},{y} {x + 26},{y + 13}" fill="#9aa3ad" stroke="#d7dde4" stroke-width="1.5"/>
<path d="M{x - 92},{y} L{x - 70},{y} L{x - 82},{y - 17} L{x - 102},{y - 17} Z" fill="#5aa02c"/>
<path d="M{x - 92},{y} L{x - 70},{y} L{x - 82},{y + 17} L{x - 102},{y + 17} Z" fill="#9ccc65"/>
<line x1="{x - 130}" y1="{y - 9}" x2="{x - 108}" y2="{y - 9}" stroke="#9ccc65" stroke-width="2" opacity="0.5"/>
<line x1="{x - 140}" y1="{y + 8}" x2="{x - 110}" y2="{y + 8}" stroke="#9aa3ad" stroke-width="2" opacity="0.5"/>"""


def image_heroes():
    W, H = 1800, 1120
    heroes = [
        ("Fire Mage", "Ranged mage", "Fire", ["#e0443a", "#ff8c1a", "#ffd23f"], "#ff7a2f",
         {"Fire": 25, "Frost": -20, "Nature": 0, "Lightning": 10, "Physical": -10, "Air": 5},
         fireball, "Fireball", "125 Fire damage"),
        ("Frost Mage", "Ranged mage", "Frost", ["#1f6feb", "#6cc4ff", "#f2f8ff"], "#5bb4ff",
         {"Fire": -20, "Frost": 25, "Nature": 5, "Lightning": 0, "Physical": -10, "Air": 10},
         ice_shard, "Ice Shard", "125 Frost damage"),
        ("Ranger", "Ranged archer", "Physical", ["#5aa02c", "#9ccc65", "#9aa3ad"], "#8fd13a",
         {"Fire": -5, "Frost": -5, "Nature": 15, "Lightning": -10, "Physical": 25, "Air": 5},
         arrow, "Arrow", "125 Physical damage"),
    ]
    b = []
    b.append(wrap(70, 92, ["ONE SPELL, THREE HEROES"], 46, GOLD, 800))
    b.append(wrap(72, 132, ["Shop spells are generic. The hero decides their damage type, their colours and how they look; "
                            "their affinities decide how hard they hit."], 20, MUTED))

    # Generic shop card
    sx, sy, sw = 600, 165, 600
    b.append(panel(sx, sy, sw, 104))
    b.append(f'<rect x="{sx + 20}" y="{sy + 20}" width="64" height="64" rx="10" fill="#1d2433" stroke="#5b6880" stroke-width="2"/>')
    b.append(f'<circle cx="{sx + 52}" cy="{sy + 52}" r="13" fill="#c9d1dd"/>'
             f'<path d="M{sx + 26},{sy + 52} L{sx + 38},{sy + 52}" stroke="#c9d1dd" stroke-width="4" stroke-linecap="round"/>')
    b.append(wrap(sx + 104, sy + 44, [f'Projectile <tspan fill="{MUTED}" font-size="15" font-weight="400">· shop spell</tspan>'], 24, TEXT, 700))
    b.append(wrap(sx + 104, sy + 76, ["Fires a projectile in front of the caster. 100 damage · Range 1500"], 16, MUTED))

    col_w, gap, top = 540, 30, 320
    left = (W - (3 * col_w + 2 * gap)) / 2
    for k, (name, role, base, palette, accent, profile, art, spell, dmg) in enumerate(heroes):
        x = left + k * (col_w + gap)
        # connector from the shop card
        b.append(f'<path d="M{sx + sw / 2},{sy + 104} C{sx + sw / 2},{top - 20} {x + col_w / 2},{top - 40} {x + col_w / 2},{top}" '
                 f'stroke="{accent}" stroke-width="2.5" fill="none" stroke-dasharray="6 6" opacity="0.7"/>')
        b.append(panel(x, top, col_w, 750))
        b.append(f'<rect x="{x}" y="{top}" width="{col_w}" height="6" rx="3" fill="{accent}"/>')
        b.append(wrap(x + 30, top + 52, [name.upper()], 28, TEXT, 800))
        b.append(wrap(x + 30, top + 80, [role], 17, MUTED))
        b.append(hexagon(x + col_w / 2, top + 285, 120, profile, fill=accent, scale_labels=False, dot=11, font=16, sub=True))

        y0 = top + 540
        b.append(f'<line x1="{x + 30}" y1="{y0 - 22}" x2="{x + col_w - 30}" y2="{y0 - 22}" stroke="{LINE}"/>')
        b.append(wrap(x + 30, y0, ["BASE DAMAGE TYPE"], 14, MUTED, 700))
        b.append(f'<circle cx="{x + 40}" cy="{y0 + 26}" r="9" fill="{color_of(base)}"/>')
        b.append(wrap(x + 56, y0 + 33, [base], 20, TEXT, 700))
        b.append(wrap(x + 290, y0, ["SPELL COLOURS"], 14, MUTED, 700))
        for j, c in enumerate(palette):
            b.append(f'<rect x="{x + 290 + j * 44}" y="{y0 + 12}" width="34" height="28" rx="6" fill="{c}" stroke="#ffffff22"/>')

        y1 = y0 + 78
        b.append(wrap(x + 30, y1, ["PROJECTILE BECOMES"], 14, MUTED, 700))
        b.append(f'<rect x="{x + 30}" y="{y1 + 14}" width="{col_w - 60}" height="96" rx="10" fill="#0f1420" stroke="{LINE}"/>')
        b.append(art(x + 165, y1 + 62))
        b.append(wrap(x + 290, y1 + 56, [spell], 22, TEXT, 700))
        b.append(wrap(x + 290, y1 + 82, [dmg], 16, accent, 700))
        b.append(wrap(x + 290, y1 + 102, [f"100 × {100 + profile[base]}% affinity"], 13, MUTED))

    b.append(wrap(W / 2, H - 22, ["Heroes with more than one base damage type (e.g. Fire + Lightning) are a separate case, to be designed."],
                  15, MUTED, 400, anchor="middle"))
    return page(W, H, "\n".join(b))


for name, (html, w, h) in {
    "spell-affinity-system": (image_system(), 1600, 1000),
    "spell-affinity-heroes": (image_heroes(), 1800, 1120),
}.items():
    with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(name, w, h)
