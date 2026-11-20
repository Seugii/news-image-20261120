#!/usr/bin/env python3
"""Render the 20 November 2026 front page (1024x1024 PNG).

Fresh build for news-image-20261120. Photos fetched from Wikimedia Commons
(see README.md for credits). Illustrations drawn flat with PIL and captioned
as illustrations. No network at render time beyond the photos already on disk.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BASE = os.path.dirname(os.path.abspath(__file__))
PHOTOS = os.path.join(BASE, "photos")

PAPER = (253, 252, 246)
INK = (17, 17, 17)
GREY = (90, 90, 90)
RED = (178, 34, 34)
RULE = (30, 30, 30)
BAND = (238, 236, 228)
SEA = (38, 84, 124)

F_SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
F_SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
F_SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, x, y, text, fnt, max_w, fill=INK, lh=None):
    if lh is None:
        lh = int(fnt.size * 1.22)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def cover(im, box_w, box_h, focus_y=0.5):
    iw, ih = im.size
    scale = max(box_w / iw, box_h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    im = im.resize((nw, nh), Image.LANCZOS)
    x0 = (nw - box_w) // 2
    y0 = int((nh - box_h) * focus_y)
    y0 = max(0, min(nh - box_h, y0))
    return im.crop((x0, y0, x0 + box_w, y0 + box_h))


def paste_photo(page, name, x, y, w, h, focus_y=0.5):
    im = Image.open(os.path.join(PHOTOS, name)).convert("RGB")
    page.paste(cover(im, w, h, focus_y), (x, y))
    d = ImageDraw.Draw(page)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=(0, 0, 0), width=1)


def kicker(draw, x, y, text):
    draw.text((x, y), text, font=font(F_SANS_B, 10), fill=RED)
    return y + 13


def caption(draw, x, y, text, w):
    return draw_lines(draw, x, y, text, font(F_SANS_I, 9), w, fill=GREY, lh=11)


def headline(draw, x, y, text, size, w):
    return draw_lines(draw, x, y, text, font(F_SERIF_B, size), w,
                      lh=int(size * 1.12))


def body(draw, x, y, text, size, w):
    return draw_lines(draw, x, y, text, font(F_SERIF, size), w,
                      lh=int(size * 1.24))


def rule(draw, x, y, w, weight=1):
    draw.line([(x, y), (x + w, y)], fill=RULE, width=weight)


def illus_tanker(box_w, box_h):
    im = Image.new("RGB", (box_w, box_h), (250, 214, 165))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, box_w, int(box_h * 0.62)], fill=(248, 196, 130))
    d.ellipse([box_w - 70, 8, box_w - 14, 64], fill=(255, 236, 180))
    d.rectangle([0, int(box_h * 0.62), box_w, box_h], fill=SEA)
    for i in range(5):
        yy = int(box_h * 0.66) + i * 9
        d.line([(0, yy), (box_w, yy)], fill=(90, 140, 175), width=2)
    hy = int(box_h * 0.52)
    d.polygon([(8, hy), (box_w - 8, hy), (box_w - 34, hy + 26), (34, hy + 26)],
              fill=(150, 40, 32))
    d.rectangle([int(box_w * 0.62), hy - 34, int(box_w * 0.86), hy], fill=(240, 240, 235))
    d.rectangle([int(box_w * 0.66), hy - 30, int(box_w * 0.82), hy - 18],
                fill=(40, 70, 100))
    d.rectangle([int(box_w * 0.70), hy - 46, int(box_w * 0.78), hy - 34],
                fill=(220, 220, 215))
    d.rectangle([int(box_w * 0.20), hy - 26, int(box_w * 0.30), hy], fill=(200, 60, 40))
    d.ellipse([int(box_w * 0.22), hy - 44, int(box_w * 0.30), hy - 30], fill=(120, 120, 120))
    d.ellipse([int(box_w * 0.28), hy - 56, int(box_w * 0.38), hy - 40], fill=(150, 150, 150))
    return im


def illus_chart(box_w, box_h):
    im = Image.new("RGB", (box_w, box_h), (245, 245, 240))
    d = ImageDraw.Draw(im)
    base = box_h - 26
    d.line([(14, base), (box_w - 10, base)], fill=INK, width=2)
    bars = [("IPO", 83, (120, 120, 120)), ("OPEN", 111.5, (60, 120, 80)),
            ("CLOSE", 97.2, (40, 80, 140)), ("AFTER", 92.6, (178, 34, 34))]
    bw = (box_w - 40) // 4
    for i, (lab, val, col) in enumerate(bars):
        hgt = int((val / 120.0) * (box_h - 52))
        x0 = 20 + i * bw
        d.rectangle([x0, base - hgt, x0 + bw - 12, base], fill=col)
        d.text((x0 + 2, base - hgt - 15), "$%.0f" % val,
               font=font(F_SANS_B, 11), fill=INK)
        d.text((x0 + 2, base + 4), lab, font=font(F_SANS_B, 10), fill=GREY)
    return im


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)
    MX, CW = 20, 984

    # ---------- masthead ----------
    title = "THE WORLD IN ONE PAGE"
    tf = font(F_SERIF_B, 42)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 10), title, font=tf, fill=INK)
    rule(d, MX, 60, CW, 2)
    rule(d, MX, 64, CW, 1)
    d.text((MX, 70), "FRIDAY, 20 NOVEMBER 2026",
           font=font(F_SANS_B, 11), fill=INK)
    mid = "36 STORIES  ·  7 REGIONS"
    d.text(((W - d.textlength(mid, font=font(F_SANS_B, 11))) / 2, 70), mid,
           font=font(F_SANS_B, 11), fill=RED)
    right = "ONE PAGE, EVERYTHING"
    d.text((W - MX - d.textlength(right, font=font(F_SANS_B, 11)), 70), right,
           font=font(F_SANS_B, 11), fill=INK)

    # ---------- timeline strip ----------
    d.rectangle([MX, 90, MX + CW, 114], fill=BAND)
    d.text((MX + 8, 93), "TODAY",
           font=font(F_SANS_B, 10), fill=RED)
    d.text((MX + 82, 93),
           "Akvan landfall, Odisha  ·  Kyiv bridges hit  ·  Taiex plunges 2,200 pts  ·  Europe ready for talks",
           font=font(F_SANS, 10), fill=INK)
    d.text((MX + 8, 104), "YESTERDAY",
           font=font(F_SANS_B, 10), fill=RED)
    d.text((MX + 82, 104),
           "Trilateral summit in Shenzhen  ·  ICJ: Myanmar genocide  ·  Senate rejects war-powers vote  ·  Anthropic debut",
           font=font(F_SANS, 10), fill=INK)

    # ---------- LEAD: Cyclone Akvan ----------
    y = 122
    y = kicker(d, MX, y, "SOUTH ASIA  —  LEAD")
    y = headline(d, MX, y, "CYCLONE AKVAN SLAMS INTO INDIA'S EAST COAST",
                 29, CW)
    y += 3
    paste_photo(page, "akvan.jpg", MX, y, 400, 138, focus_y=0.45)
    by = body(d, MX + 416, y,
              "Cyclone Akvan crossed the North Andhra Pradesh and South "
              "Odisha coast near Gopalpur on Friday morning, packing winds "
              "of 70–80 kmph gusting to 90. More than 300,000 people were "
              "evacuated, 423 rescue teams deployed and 69 trains cancelled "
              "as heavy rain lashed six states.", 12.5, CW - 416)
    caption(d, MX, y + 141,
            "Cyclone Akvan over the Bay of Bengal, 18 Nov 2026. "
            "NASA / MODIS (public domain)", 400)
    lead_bottom = max(by, y + 152)

    # ---------- row 2: three photo stories ----------
    cols = [MX, 353, 686]
    colw = 318
    y = lead_bottom + 7
    rule(d, MX, y, CW, 1)
    y += 7
    row2 = [
        ("UKRAINE WAR", "Kyiv bridges hit in overnight missile blitz",
         "Russia launched a sustained overnight ballistic-missile attack on "
         "Kyiv, damaging three bridges across the Dnipro. Fires broke out "
         "in two districts and the Dutch embassy suffered minor damage.",
         "kyiv_bridge.jpg", 0.5,
         "The Podilsko-Voskresenskyi Bridge, Kyiv (file photo). CC BY-SA 4.0"),
        ("MARKETS", "Taiwan stocks plunge 2,200 points in a day",
         "The Taiex fell more than 2,200 points intraday to 35,959 — down "
         "about 6% — in its worst week since 1991, wiping roughly $1.12tn "
         "since the 6 October record.",
         "taipei101.jpg", 0.18,
         "Taipei 101 (file photo). CC BY-SA 3.0"),
        ("MIDDLE EAST", "Houthi missile hits Riyadh's tallest tower",
         "A Houthi missile struck the 80-storey PIF Tower in Riyadh's King "
         "Abdullah Financial District, blowing out windows across seven to "
         "eight floors. No injuries were reported.",
         "pif_tower.jpg", 0.12,
         "PIF Tower, Riyadh, 2024 (file photo). CC BY-SA 4.0"),
    ]
    row2_bottom = y
    for (x, (kick, head, txt, photo, foc, cap)) in zip(cols, row2):
        yy = kicker(d, x, y, kick)
        yy = headline(d, x, yy, head, 17, colw)
        yy += 2
        paste_photo(page, photo, x, yy, colw, 88, focus_y=foc)
        yy += 92
        yy = body(d, x, yy, txt, 11, colw)
        yy = caption(d, x, yy + 1, cap, colw)
        row2_bottom = max(row2_bottom, yy)

    # ---------- row 3: COP31 / Hormuz / Anthropic ----------
    y = row2_bottom + 7
    rule(d, MX, y, CW, 1)
    y += 7
    row3 = [
        ("CLIMATE", "COP31 draft drops fossil fuels — outcry",
         "The revised COP31 draft in Antalya strips out all references to "
         "fossil fuels — cut from 18 pages to nine — and drops the "
         "$120bn-a-year adaptation finance target.",
         "photo", "cop31_guterres.jpg", 0.5,
         "UN chief António Guterres at COP31, Antalya. CC BY-SA 4.0"),
        ("MIDDLE EAST", "Tankers hit by mines in the Strait of Hormuz",
         "Iran's Revolutionary Guard Navy says two supertankers carrying "
         "more than four million barrels of crude hit naval mines and caught "
         "fire in the southern Strait of Hormuz.",
         "illus", "tanker", None,
         "Illustration: an oil tanker at sea."),
        ("TECH", "Anthropic's debut fades after record IPO",
         "Anthropic debuted on the Nasdaq on Thursday at $83, opened at "
         "$111.50 and closed at $97.17 — up 17% on day one in the largest IPO "
         "on record, raising $81.3bn.",
         "illus", "chart", None,
         "Illustration: Anthropic's first day on the Nasdaq."),
    ]
    row3_bottom = y
    for (x, (kick, head, txt, kind, src, foc, cap)) in zip(cols, row3):
        yy = kicker(d, x, y, kick)
        yy = headline(d, x, yy, head, 17, colw)
        yy += 2
        if kind == "photo":
            paste_photo(page, src, x, yy, colw, 80, focus_y=foc)
        else:
            im = illus_tanker(colw, 80) if src == "tanker" else illus_chart(colw, 80)
            page.paste(im, (x, yy))
            d.rectangle([x, yy, x + colw - 1, yy + 79], outline=(0, 0, 0), width=1)
        yy += 84
        yy = body(d, x, yy, txt, 11, colw)
        yy = caption(d, x, yy + 1, cap, colw)
        row3_bottom = max(row3_bottom, yy)

    # ---------- row 4: medium stories + briefs, 4 columns ----------
    y = row3_bottom + 7
    rule(d, MX, y, CW, 1)
    y += 7
    col4 = [MX, 270, 520, 770]
    col4w = 234
    medium = [
        [("UKRAINE & EUROPE", "UK pledges 1,000+ drones for Ukraine",
          "Britain will send more than 1,000 long-range strike drones to "
          "Ukraine in a £260m package announced in Berlin, PM Andy Burnham "
          "said — some able to fly over 1,000 km."),
         ("UKRAINE & EUROPE", "Europe ready for talks with Russia",
          "European leaders at Berlin's Coalition of the Willing summit said "
          "they are ready for negotiations with Russia. Moscow's “maximalist "
          "demands are not realistic”, Chancellor Merz said.")],
        [("AMERICAS", "US Senate rejects Iran war-powers vote",
          "The Senate voted 51–48 to reject a House-passed resolution "
          "directing the president to end the Iran war or seek Congress' "
          "approval. Three Republicans voted yes."),
         ("AMERICAS", "Iran war has cost $48.3bn, Pentagon says",
          "The war with Iran has cost $48.3bn as of 13 November, the "
          "Pentagon's deputy comptroller told the Senate — covering "
          "munitions, equipment and operations.")],
        [("WORLD", "First-ever Trump–Xi–Putin summit",
          "The three leaders met in Shenzhen for about 80–90 minutes in the "
          "first-ever trilateral summit, issuing a joint declaration on UN "
          "reform, more oil output and nuclear-risk dialogue."),
         ("WORLD", "ICJ: Myanmar committed genocide",
          "The International Court of Justice ruled 9–6 that Myanmar "
          "committed genocide against the Rohingya in 2017, in a landmark "
          "judgment delivered on Thursday.")],
        [("AMERICAS", "US sanctions Comancheros and 'Ndrangheta",
          "The US Treasury sanctioned Australia's Comanchero biker gang and "
          "Italy's 'Ndrangheta for helping cartels traffic drugs, and added "
          "a Tron crypto address to its blocked list."),
         ("WORLD", "Gas blast kills six in Tbilisi",
          "A suspected gas explosion in a five-storey apartment block in "
          "Tbilisi's Ponichala district killed six people, including a "
          "child, and partly collapsed the building.")],
    ]
    briefs = [
        ["GTA VI was released on Thursday.", "Van Gogh sells for $190.4m at Sotheby's.",
         "EU agrees €45bn loan to Ukraine.", "Trump pardons Pete Rose.",
         "IAEA reports on N. Korea enrichment."],
        ["Israel delays E1 settlement plan.", "Saudi coalition hits 60 Houthi sites.",
         "US signs pact with Venezuela.", "India, Japan hold 2+2 talks.",
         "NASA's CRS-25 cargo mission launches."],
        ["Jeffries picked as Speaker candidate.", "US loses measles elimination status.",
         "Bangladesh turmoil; Yunus home torched.", "Drones halt Genoa airport for two hours.",
         "COP31: electricity 35% of energy by 2035."],
        ["Trump dials into Berlin summit.", "Putin invites Europeans to Moscow.",
         "Crimea Bridge struck a third time.", "M5.6 quake off New Caledonia.",
         "Israel strikes Hezbollah site in Lebanon.", "One dead in Paris tower-block fire."],
    ]
    bottom = y
    for ci, (x, stories) in enumerate(zip(col4, medium)):
        yy = y
        for (kick, head, txt) in stories:
            yy = kicker(d, x, yy, kick)
            yy = headline(d, x, yy, head, 13.5, col4w)
            yy = body(d, x, yy, txt, 10.5, col4w)
            yy += 5
        yy = kicker(d, x, yy, "BRIEFS")
        for b in briefs[ci]:
            yy = draw_lines(d, x, yy, "•  " + b, font(F_SANS, 10),
                            col4w, lh=12.5)
            yy += 1
        bottom = max(bottom, yy)
    print("row4 bottom:", bottom)

    # ---------- footer ----------
    fy = bottom + 4
    rule(d, MX, fy, CW, 1)
    d.text((MX, fy + 3),
           "Sources: IMD · The Hindu · Reuters · AP · GOV.UK · US Senate · Pentagon · NASA · USGS · US Treasury · OFAC · UN · IAEA · Sotheby's · Wikimedia Commons",
           font=font(F_SANS, 8.5), fill=GREY)
    d.text((MX, fy + 13),
           "Photos: NASA (public domain) · Wikimedia Commons (CC BY-SA 3.0 / 4.0, see README) · Illustrations drawn for this page. All stories verified 20 Nov 2026.",
           font=font(F_SANS, 8.5), fill=GREY)
    print("footer bottom:", fy + 23)

    out = os.path.join(BASE, "entry.png")
    page.save(out, "PNG", optimize=True)
    print("saved", out, page.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
