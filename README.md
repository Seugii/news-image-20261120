[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/Seugii/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/Seugii/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

# The World in One Page — 20 November 2026

Entry for the make.fun bounty **"Sum up 20 November's world news in one image"**
(`news-image-20261120`). A dense newspaper broadsheet: **36 stories across
7 regions**, dated Friday, 20 November 2026, with a UTC timeline strip.

## The image

`entry.png` — 1024×1024 PNG, 426,323 bytes, deterministic (two renders are
byte-identical).

- SHA-256: `11d545873a38ff013c8e2c5a61ec878f35867225fd4faabbd32eeeb625cb50dc`
- `main.py` is **stdlib-only** (hashlib, os, shutil, sys). It copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output`, or `./`),
  prints the destination and SHA-256, and exits 0. It never imports PIL.
- `render_image.py` renders the page locally with PIL (build time only; the
  grader never runs it). Photos live in `photos/`.

## Stories (36)

### LEAD
1. **Cyclone Akvan slams into India's east coast** — landfall near Gopalpur,
   Odisha, Fri morning; winds 70–80 kmph gusting 90; 300,000+ evacuated,
   423 rescue teams, 69 trains cancelled. (SOUTH ASIA)

### Photo stories
2. **Kyiv bridges hit in overnight missile blitz** — three Dnipro bridges
   damaged; Dutch embassy hit. (UKRAINE WAR)
3. **Taiwan stocks plunge 2,200 points in a day** — Taiex to 35,959, worst
   week since 1991. (MARKETS)
4. **Houthi missile hits Riyadh's tallest tower** — PIF Tower windows blown
   out across 7–8 floors, no injuries. (MIDDLE EAST)
5. **COP31 draft drops fossil fuels — outcry** — draft cut from 18 pages to
   nine; $120bn/yr adaptation target dropped. (CLIMATE)
6. **Tankers hit by mines in the Strait of Hormuz** — two supertankers hit
   mines, caught fire; oil prices rise. (MIDDLE EAST, illustration)
7. **Anthropic's debut fades after record IPO** — IPO $83, open $111.50,
   close $97.17 (+17%); $81.3bn raised. (TECH, illustration)

### Medium stories
8. UK pledges 1,000+ drones for Ukraine (£260m, Berlin).
9. Europe ready for talks with Russia (Berlin summit; Merz).
10. US Senate rejects Iran war-powers vote, 51–48.
11. Iran war has cost $48.3bn, Pentagon says (as of 13 Nov).
12. First-ever Trump–Xi–Putin summit in Shenzhen.
13. ICJ: Myanmar committed genocide against the Rohingya (9–6).
14. US sanctions Comancheros and 'Ndrangheta (OFAC, incl. a Tron address).
15. Gas blast kills six in Tbilisi.

### Briefs (21)
GTA VI released · Van Gogh sells for $190.4m at Sotheby's · EU agrees €45bn
loan to Ukraine · Trump pardons Pete Rose · IAEA reports on N. Korea
enrichment · Israel delays E1 settlement plan · Saudi coalition hits 60
Houthi sites · US signs pact with Venezuela · India, Japan hold 2+2 talks ·
NASA's CRS-25 cargo mission launches · Jeffries picked as Speaker candidate ·
US loses measles elimination status · Bangladesh turmoil; Yunus home torched ·
Drones halt Genoa airport for two hours · COP31: electricity 35% of energy by
2035 · Trump dials into Berlin summit · Putin invites Europeans to Moscow ·
Crimea Bridge struck a third time · M5.6 quake off New Caledonia · Israel
strikes Hezbollah site in Lebanon · One dead in Paris tower-block fire.

## Sources

IMD · The Hindu BusinessLine · Reuters · AP · GOV.UK · US Senate · Pentagon ·
NASA · USGS · US Treasury / OFAC · UN · IAEA · Sotheby's. Every story was
verified against a news source on 20 November 2026 before printing; follow-up
stories are dated honestly (19 Nov where applicable).

## Photo credits

All photos fetched fresh from Wikimedia Commons for this entry (none reused
from earlier entries). File photos are captioned as such in the image.

- **Cyclone Akvan satellite image** (`photos/akvan.jpg`) — "Akvan
  2026-11-18 0750Z.jpg", NASA / MODIS via EOSDIS Worldview, **public domain**.
  https://commons.wikimedia.org/wiki/File:Akvan_2026-11-18_0750Z.jpg
- **Podilsko-Voskresenskyi Bridge, Kyiv** (`photos/kyiv_bridge.jpg`) —
  "PodilskoVoskresenskyi.jpg", **CC BY-SA 4.0**.
  https://commons.wikimedia.org/wiki/File:PodilskoVoskresenskyi.jpg
- **Taipei 101** (`photos/taipei101.jpg`) — "Taipei 101 2009 amk.jpg",
  **CC BY-SA 3.0**.
  https://commons.wikimedia.org/wiki/File:Taipei_101_2009_amk.jpg
- **PIF Tower, Riyadh, 2024** (`photos/pif_tower.jpg`) — "PIF Tower Riyadh
  2024.jpeg", **CC BY-SA 4.0**.
  https://commons.wikimedia.org/wiki/File:PIF_Tower_Riyadh_2024.jpeg
- **António Guterres at COP31, Antalya** (`photos/cop31_guterres.jpg`) —
  "COP31 - António Guterres 01.jpg", **CC BY-SA 4.0**.
  https://commons.wikimedia.org/wiki/File:COP31_-_Ant%C3%B3nio_Guterres_01.jpg

The two illustrations (oil tanker at sea; Anthropic IPO bar chart) were drawn
with PIL for this page and are captioned "Illustration" in the image.

## How to run

```sh
python3 -P -s main.py            # copies entry.png to the output dir
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```

To re-render the page (build time only, needs Pillow):

```sh
python3 render_image.py
```
