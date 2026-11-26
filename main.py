"""news-image-20261126 entry: copy the front-page image to /output/entry.png.

The image is a newspaper front page summing up Thursday 26 November 2026:
a Houthi drone strike on a Saudi refinery (Brent crude tops $94), Trump's
new tariffs on 14 partners, Russian jets near South Korea, Pakistan's first
astronaut aboard China's space station, NATO's boosted air watch, plus a
ticker (Cairo tanker fire, Colombia hostage rescue, US Thanksgiving travel).

Deterministic by construction: a plain byte copy, so every run writes
identical bytes. Standard library only, no network. The file is named
entry.png either way; the gate tells PNG from JPEG by its first bytes,
and this one is JPEG.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
