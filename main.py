#!/usr/bin/env python3
"""Writes one 30-day plan for turning $100 into the most money to entry.txt."""

import os

PLAN = (
    "Day 1: pull 200 plumbers, dentists, salons with Google profiles "
    "from Maps. Offer a $99 one-time fix \u2014 hours, services, "
    "replies \u2014 done by AI in 24h, paid up front. Email and DM all. "
    "1 in 20 buys = $990. Edge: local work 1000 agents ignore; "
    "cash up front, no ads, no luck."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
