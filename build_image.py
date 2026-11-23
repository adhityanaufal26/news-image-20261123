#!/usr/bin/env python3
"""Build entry.png: a newspaper front page for Monday 23 November 2026.

Deterministic: fixed layout, fixed fonts, no randomness, no network.
Draws simple vector-style illustrations with Pillow shapes only.
Output: entry.png (1024x1024) beside this script.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"

W = H = 1024
PAPER = (250, 246, 236)
INK = (20, 33, 61)
NAVY = (18, 38, 78)
RED = (178, 34, 34)
TEAL = (13, 110, 110)
GOLD = (184, 134, 11)
GREY = (90, 90, 90)
LIGHT = (238, 231, 214)
WHITE = (255, 255, 255)
SKY = (174, 205, 232)
SEA = (70, 130, 180)
GREEN = (46, 125, 50)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=4):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


def tag(draw, x, y, label, bg):
    f = font(BOLD, 12)
    w = int(draw.textlength(label, font=f)) + 14
    draw.rounded_rectangle([x, y, x + w, y + 20], radius=4, fill=bg)
    draw.text((x + 7, y + 4), label, font=f, fill=WHITE)
    return x + w


def card(draw, box, fill=WHITE, outline=(200, 192, 170)):
    draw.rounded_rectangle(box, radius=8, fill=fill, outline=outline, width=2)


def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SKY, outline=NAVY, width=3)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=NAVY, width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=NAVY, width=2)
    # cracked "no deal" slash
    draw.line([cx - r + 6, cy + r - 8, cx + r - 6, cy - r + 8], fill=RED, width=6)
    # thermometer
    tx = cx + r + 14
    draw.rounded_rectangle([tx, cy - r, tx + 16, cy + r - 14], radius=8,
                           fill=WHITE, outline=NAVY, width=2)
    draw.rectangle([tx + 4, cy - 6, tx + 12, cy + r - 20], fill=RED)
    draw.ellipse([tx - 2, cy + r - 22, tx + 18, cy + r - 2], fill=RED, outline=NAVY, width=2)


def draw_ship(draw, x, y, s=1.0):
    # sea
    draw.rectangle([x, y + 58 * s, x + 150 * s, y + 78 * s], fill=SEA)
    # hull (listing)
    draw.polygon([(x + 10 * s, y + 58 * s), (x + 140 * s, y + 50 * s),
                  (x + 125 * s, y + 72 * s), (x + 25 * s, y + 72 * s)], fill=INK)
    draw.rectangle([x + 55 * s, y + 28 * s, x + 95 * s, y + 54 * s], fill=GREY)
    draw.rectangle([x + 68 * s, y + 10 * s, x + 82 * s, y + 30 * s], fill=INK)
    # smoke + flame
    for i, (dx, dy, r) in enumerate([(70, 0, 10), (84, -8, 8), (96, -14, 6)]):
        draw.ellipse([x + (dx - r) * s, y + (dy - r) * s,
                      x + (dx + r) * s, y + (dy + r) * s], fill=(120, 120, 120))
    draw.polygon([(x + 62 * s, y + 30 * s), (x + 78 * s, y + 8 * s),
                  (x + 92 * s, y + 30 * s)], fill=(230, 110, 20))
    # sea drone
    draw.ellipse([x + 108 * s, y + 62 * s, x + 132 * s, y + 72 * s], fill=RED)
    draw.line([x + 120 * s, y + 62 * s, x + 120 * s, y + 52 * s], fill=RED, width=3)


def draw_chart(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=WHITE, outline=NAVY, width=2)
    for i in range(1, 4):
        gy = y + h * i // 4
        draw.line([x + 6, gy, x + w - 6, gy], fill=(220, 220, 220), width=1)
    pts = [(x + 10, y + 18), (x + 40, y + 30), (x + 70, y + 26),
           (x + 100, y + 52), (x + 130, y + 62), (x + w - 12, y + h - 14)]
    draw.line(pts, fill=RED, width=4)
    for px, py in pts:
        draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED)
    # gold bar going up
    gx = x + w - 34
    draw.rectangle([gx, y + h - 30, gx + 14, y + h - 8], fill=GOLD)
    draw.polygon([(gx + 7, y + h - 40), (gx, y + h - 30), (gx + 14, y + h - 30)], fill=GOLD)


def draw_building(draw, x, y):
    draw.rectangle([x, y, x + 46, y + 62], fill=(150, 150, 150), outline=INK, width=2)
    draw.rectangle([x + 50, y + 18, x + 92, y + 62], fill=(170, 170, 170), outline=INK, width=2)
    for r in range(3):
        for c in range(2):
            draw.rectangle([x + 7 + c * 20, y + 7 + r * 18, x + 19 + c * 20, y + 17 + r * 18],
                           fill=SKY, outline=INK, width=1)
    # collapsed section
    draw.polygon([(x + 50, y + 62), (x + 92, y + 62), (x + 78, y + 34)], fill=(100, 100, 100))
    # drone
    draw.ellipse([x + 96, y - 4, x + 112, y + 6], fill=INK)
    draw.line([x + 92, y - 8, x + 116, y - 8], fill=INK, width=3)


def draw_refinery(draw, x, y):
    draw.rectangle([x, y + 44, x + 100, y + 62], fill=GREY)
    for dx, hh in [(8, 44), (34, 56), (60, 38)]:
        draw.rectangle([x + dx, y + 62 - hh, x + dx + 16, y + 62], fill=(170, 170, 170), outline=INK, width=2)
    draw.polygon([(x + 40, y + 6), (x + 48, y - 8), (x + 56, y + 6)], fill=(230, 110, 20))
    draw.ellipse([x + 76, y + 30, x + 96, y + 62], fill=SKY, outline=INK, width=2)


def draw_flame_factory(draw, x, y):
    draw.rectangle([x, y + 30, x + 96, y + 62], fill=(160, 140, 120), outline=INK, width=2)
    draw.rectangle([x + 70, y + 4, x + 84, y + 34], fill=GREY, outline=INK, width=2)
    draw.polygon([(x + 14, y + 30), (x + 30, y + 4), (x + 46, y + 30)], fill=(230, 110, 20))
    draw.polygon([(x + 22, y + 30), (x + 32, y + 14), (x + 42, y + 30)], fill=(250, 190, 40))
    draw.ellipse([x + 66, y - 8, x + 88, y + 8], fill=(120, 120, 120))


def draw_handshake(draw, x, y):
    draw.rectangle([x, y + 18, x + 44, y + 38], fill=NAVY)
    draw.rectangle([x + 58, y + 18, x + 102, y + 38], fill=RED)
    draw.ellipse([x + 38, y + 14, x + 64, y + 42], fill=(240, 200, 150), outline=INK, width=2)
    draw.ellipse([x + 12, y - 2, x + 32, y + 18], fill=(240, 200, 150), outline=INK, width=2)
    draw.ellipse([x + 70, y - 2, x + 90, y + 18], fill=(220, 170, 120), outline=INK, width=2)


def draw_exam(draw, x, y):
    draw.rectangle([x + 6, y, x + 66, y + 62], fill=WHITE, outline=INK, width=2)
    for i in range(4):
        draw.line([x + 14, y + 12 + i * 11, x + 58, y + 12 + i * 11], fill=GREY, width=2)
    draw.line([x + 12, y + 8, x + 60, y + 54], fill=RED, width=5)
    draw.line([x + 60, y + 8, x + 12, y + 54], fill=RED, width=5)
    # tiny camera
    draw.rectangle([x + 74, y + 22, x + 96, y + 38], fill=INK)
    draw.ellipse([x + 80, y + 26, x + 90, y + 36], fill=SKY)


def draw_football(draw, x, y):
    draw.ellipse([x + 18, y + 4, x + 74, y + 60], fill=WHITE, outline=INK, width=3)
    draw.polygon([(x + 46, y + 22), (x + 58, y + 32), (x + 53, y + 45),
                  (x + 39, y + 45), (x + 34, y + 32)], fill=INK)
    draw.rectangle([x + 80, y + 6, x + 96, y + 28], fill=RED, outline=INK, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- Masthead ----------
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.text((28, 10), "T H E   W O R L D   T O D A Y", font=font(BOLD, 17), fill=(160, 190, 230))
    d.text((28, 32), "Monday 23 November 2026", font=font(BOLD, 46), fill=WHITE)
    d.text((28, 88), "Early edition - compiled 02:40 UTC - every story labelled by day",
           font=font(REG, 15), fill=(200, 215, 240))
    d.text((W - 28, 88), "No. 23", font=font(BOLD, 15), fill=(200, 215, 240), anchor="ra")

    # ---------- Leads ----------
    leads = [
        dict(box=(16, 130, 340, 386), tag="SUN - ANTALYA, TURKEY", tc=RED,
             head="COP31 COLLAPSES:\nNO DEAL ON\nFOSSIL FUELS",
             body="Talks ended Sunday with no pact after the final text dropped "
                  "every mention of fossil fuels. The EU refused a deal that "
                  "\"does not even mention fossil fuels\"."),
        dict(box=(350, 130, 674, 386), tag="SUN - BENGHAZI, LIBYA", tc=RED,
             head="RUSSIAN WARSHIP\nHIT BY SEA\nDRONES",
             body="The corvette Merkury was struck at Benghazi naval base early "
                  "Sunday in a suspected Ukrainian sea-drone attack. Images "
                  "show it capsized."),
        dict(box=(684, 130, 1008, 386), tag="MON - ASIA MARKETS", tc=TEAL,
             head="MONDAY MARKETS\nSLIDE; GOLD\nJUMPS",
             body="Asia opened down: Seoul's KOSPI fell about 4%, Shanghai "
                  "slipped 1.4% below 3,500. Tokyo was shut for a holiday. "
                  "Gold rose nearly 2% to about $3,603 an ounce."),
    ]
    for i, L in enumerate(leads):
        x0, y0, x1, y1 = L["box"]
        card(d, L["box"])
        tag(d, x0 + 12, y0 + 10, L["tag"], L["tc"])
        d.multiline_text((x0 + 12, y0 + 38), L["head"], font=font(BOLD, 23),
                         fill=INK, spacing=2)
        if i == 0:
            draw_globe(d, x0 + 66, y0 + 146, 34)
        elif i == 1:
            draw_ship(d, x0 + 18, y0 + 130, s=0.75)
        else:
            draw_chart(d, x0 + 14, y0 + 114, 150, 72)
        text_block(d, x0 + 12, y0 + 188, L["body"], font(REG, 13), (40, 40, 40),
                   x1 - x0 - 24, leading=3)

    # ---------- Map strip ----------
    card(d, (16, 396, 1008, 502), fill=(232, 240, 248))
    d.text((28, 404), "WHERE IT HAPPENED", font=font(BOLD, 14), fill=NAVY)
    # crude continents as blobs (left half only; legend sits right)
    blobs = [(40, 444, 110, 484), (130, 452, 162, 492), (240, 440, 360, 482),
             (370, 446, 430, 486), (440, 438, 540, 480)]
    for b in blobs:
        d.rounded_rectangle(b, radius=14, fill=(190, 215, 175), outline=(140, 170, 130), width=1)
    pins = [(1, 300, 448), (2, 322, 468), (3, 510, 452), (4, 340, 444),
            (5, 356, 464), (6, 470, 470), (7, 440, 450), (8, 272, 446)]
    for n, px, py in pins:
        d.ellipse([px - 10, py - 10, px + 10, py + 10], fill=RED, outline=WHITE, width=2)
        d.text((px, py), str(n), font=font(BOLD, 12), fill=WHITE, anchor="mm")
    legend = ["1 Antalya COP31", "2 Benghazi", "3 Seoul / Shanghai", "4 Dymer, Kyiv",
              "5 Saudi / Bahrain", "6 Serang, Indonesia", "7 New Delhi", "8 Liverpool"]
    lx = 580
    for j, t in enumerate(legend):
        col, row = j % 2, j // 2
        d.text((lx + col * 215, 428 + row * 17), t, font=font(REG, 12.5), fill=INK)

    # ---------- Day in numbers ----------
    card(d, (16, 512, 1008, 586), fill=(255, 250, 230))
    d.text((28, 520), "THE DAY IN NUMBERS", font=font(BOLD, 15), fill=GOLD)
    nums = [("-4%", "KOSPI, Mon open"), ("3,500", "Shanghai slips below"),
            ("$3,603", "gold, +~2% Mon"), ("157/4", "NZ at lunch, Day 5"),
            ("720/9", "India's record total"), ("24", "body bags, Serang"),
            ("14", "unaccounted, Dymer"), ("4-0", "Liverpool v Man Utd")]
    for j, (big, small) in enumerate(nums):
        nx = 28 + j * 121
        d.text((nx, 542), big, font=font(BOLD, 19), fill=INK)
        d.text((nx, 566), small, font=font(REG, 10.5), fill=GREY)

    # ---------- Mid cards ----------
    mids = [
        ("SUN - DYMER, UKRAINE", RED, "Drone collapses flats",
         "Russian drone tore through a Kyiv-region block Sunday. "
         "14 unaccounted for, 9 evacuated.", draw_building),
        ("SUN - SAUDI / BAHRAIN", RED, "Houthis claim refinery hit",
         "Houthis say they hit Saudi's Rabigh refinery - unconfirmed. "
         "2 wounded in Bahrain.", draw_refinery),
        ("RESUMES TODAY - INDONESIA", TEAL, "Factory search resumes",
         "Crews return Monday to the Serang candy factory. Fire Saturday; "
         "24 body bags, 29 missing.", draw_flame_factory),
        ("TODAY - NEW DELHI", TEAL, "Nepal PM meets Modi",
         "Balendra Shah holds talks with PM Modi Monday, day two of his "
         "first state visit to India.", draw_handshake),
        ("SUN - SEOUL", RED, "Minister quits over AI row",
         "Choi Kyo-jin resigned Sunday over chaotic last-minute rules to "
         "stop AI cheating in the Suneung.", draw_exam),
        ("SUN - LIVERPOOL", RED, "Liverpool 4-0 United",
         "Pochettino's debut unravelled fast: Yoro sent off after 8 "
         "minutes, Liverpool cruised.", draw_football),
    ]
    for j, (tg, tc, head, body, art) in enumerate(mids):
        col, row = j % 3, j // 3
        x0 = 16 + col * 334
        y0 = 596 + row * 124
        card(d, (x0, y0, x0 + 324, y0 + 114))
        tag(d, x0 + 10, y0 + 8, tg, tc)
        art(d, x0 + 6, y0 + 40)
        hy = text_block(d, x0 + 124, y0 + 34, head, font(BOLD, 14), INK, 190, leading=2)
        text_block(d, x0 + 124, hy + 2, body, font(REG, 11.5), (40, 40, 40), 190, leading=2)

    # ---------- Briefs ----------
    d.text((16, 852), "ALSO TODAY / OVERNIGHT", font=font(BOLD, 14), fill=NAVY)
    briefs = [
        "TODAY: Trump due to speak at the Justice Department, 21:30 GMT.",
        "MON: Cricket - India need 6 wickets to beat NZ in Wellington.",
        "SUN: Israel's Eisenkot calls settler arson \"Jewish terrorism\".",
        "SAT: Thousands march in Lisbon over living costs and low wages.",
        "SAT: Myanmar calls ASEAN summit decision \"unfair and imbalanced\".",
        "SAT NIGHT (US): Verstappen wins Las Vegas GP, his 75th F1 victory.",
    ]
    for j, b in enumerate(briefs):
        col, row = j % 2, j // 2
        bx = 16 + col * 502
        by = 874 + row * 20
        d.ellipse([bx, by + 5, bx + 7, by + 12], fill=RED)
        d.text((bx + 13, by), b, font=font(REG, 12), fill=INK)

    # ---------- Date check + footer ----------
    d.rounded_rectangle([16, 938, 1008, 984], radius=6, fill=NAVY)
    d.text((28, 944), "DATE CHECK - NOT Monday:", font=font(BOLD, 12.5), fill=(255, 210, 90))
    d.text((28, 962),
           "ICE airport arrests = Sat 21 Nov  -  FIDE chess Game 1 = Tue 24 Nov (ceremony was Sun)  -  UN killer-robot talks = 16-20 Nov, Geneva",
           font=font(REG, 11.5), fill=WHITE)
    d.text((16, 992),
           "Sources: Reuters, AFP, AP, CNN, The Hindu, Chess.com - compiled Mon 23 Nov 2026, 02:40 UTC. SUN = Sunday 22 Nov, SAT = Saturday 21 Nov.",
           font=font(REG, 11), fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
