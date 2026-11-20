# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/yudhisutawan/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/yudhisutawan/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

The World, Today — one newspaper front page summing up the world's news of Friday 20 November 2026: Trump, Xi and Putin meet in a historic three-way summit in Shenzhen, the world court rules Myanmar committed genocide against the Rohingya, Anthropic soars 17% in a record $81bn IPO debut, Cyclone Akvan hits Odisha, COP31 closes in Antalya, Kyiv is hit by ballistic missiles — and 34 more stories across world, business, tech, science, sport and culture. 40 stories in one image.

`main.py` copies the pre-rendered front page (`entry.png`, in this repository) with the Python standard library only — no network, no clock, no randomness — so two runs write identical bytes. The program runs the same everywhere, including a bare Python container with no image libraries or fonts installed.

## Run it

```sh
python3 main.py
```

This writes the image to `/output/entry.png` (`$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set). The image is 1024x1024 PNG, well under the 1 MiB limit.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2fnbbcz4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
