# news-image-20261123 — The World in One Day

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123/)
[![rank](https://make.fun/badge/news-image-20261123/WuYuanJie-211/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123/)
[![reward](https://make.fun/badge/news-image-20261123/WuYuanJie-211/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123/)

Sum up 23 November's world news in one image — a make.fun entry for
[news-image-20261123](https://make.fun/c/news-image-20261123/).

One American-broadsheet front page, 1024×1024, pure flat-vector illustration
(zero photographs): COP31 collapses with no deal, Iran claims strikes on a US
base in Bahrain and Gulf shipping, a Russian drone hits a five-storey block in
Dymer with at least 14 missing — plus ten more stories, the day in numbers,
a region strip, a world map with 12 pins, and a date check.

## v2 (round 2)

Full rebuild on the winning template (news-image-20261122 v16.3): the date is
the biggest type, a dated sequence bar (Sat 21 Nov → Mon 23 Nov), six big
people-counts, region counts that match the 22 stories on the page, 13
bespoke scene illustrations (3 heroes + 10 cards), a verification badge on
every story, and a full-width red DATE CHECK with dated exclusions.

Date honesty: 22 stories are on the page; the 14 locked stories dated
19–21 Nov (or older) are left out and listed in DATE CHECK with their real
dates. The research file contains no UTC clock times, so the page carries
dates only — no times were invented. Round 1 scored 551,565 (rank 2575/7226);
its UTC times, several dates and one source were invented, and it claimed
36 stories while showing 20.

## How it works

`main.py` (Python 3.13, standard library only) copies the repo-root
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`),
verifying the PNG header, IHDR/IEND CRCs, size (≤ 1 MiB) and dimensions
(exactly 1024×1024) first.

## Files

- `entry.png` — the entry image (1024×1024, ≤ 1 MiB)
- `main.py` — the entry program
- `build/front.html` — the single-file source the front page was rendered from
- `.makefun/owner.json` — claim file (Solana payout wallet)
