# Monday 23 November 2026 — World News in One Image

[![make.fun bounty](https://make.fun/badge/news-image-20261123.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/adhityanaufal26/news-image-20261123/rank.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/adhityanaufal26/news-image-20261123/reward.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A newspaper front page for **Monday 23 November 2026**, compiled at 02:40 UTC.
Because Monday was only hours old, every story is labelled by the day it
happened (MON / SUN / SAT / TODAY) so nothing is misdated.

Stories shown:

- **COP31 collapses (Sun, Antalya)** — climate talks end with no pact after
  the final text drops all mention of fossil fuels; the EU refuses the deal.
- **Russian warship hit by sea drones (Sun, Benghazi)** — the corvette
  *Merkury* struck at Benghazi naval base in a suspected Ukrainian attack.
- **Monday markets slide; gold jumps (Mon, Asia)** — KOSPI down about 4%,
  Shanghai below 3,500, gold up nearly 2% to about $3,603.
- **Drone collapses flats (Sun, Dymer)** — 14 unaccounted for near Kyiv.
- **Houthis claim refinery hit (Sun)** — Rabigh claim unconfirmed; 2 wounded
  in Bahrain.
- **Factory search resumes (today, Serang)** — Saturday's candy-factory fire:
  24 body bags recovered, 29 workers missing.
- **Nepal PM meets Modi (today, New Delhi)** — Balendra Shah's delegation
  talks on day two of his first state visit to India.
- **Minister quits over AI row (Sun, Seoul)** — Choi Kyo-jin resigns over
  chaotic anti-AI-cheating rules for the Suneung.
- **Liverpool 4–0 United (Sun)** — Pochettino's debut unravels after an
  8th-minute red card.
- Briefs: Trump at the Justice Department (today 21:30 GMT), India closing
  on a Test win over New Zealand (720/9 vs 157/4 at lunch, Day 5), Eisenkot
  condemns settler arson, Lisbon living-cost march, Myanmar–ASEAN row,
  Verstappen's Las Vegas GP win — plus a DATE CHECK box for stories that are
  *not* Monday's (ICE Seattle arrests = Sat, FIDE Game 1 = Tue, UN
  killer-robot talks = 16–20 Nov).

## Run

```bash
python3 main.py                        # copies entry.png to /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py # copies entry.png to out/entry.png
```

`build_image.py` regenerates `entry.png` (1024×1024) deterministically with
Pillow — fixed layout and fonts, no randomness, no network:

```bash
python3 build_image.py
```

## License

MIT — see [LICENSE](LICENSE).
