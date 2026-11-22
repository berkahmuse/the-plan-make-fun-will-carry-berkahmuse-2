"""Entry for make.fun competition the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (1-280 chars) to /output/entry.txt: a done-for-you AI
service sold to local plumbers -- automated missed-call text-back plus
Google review replies -- priced per month, clients found via Google Maps
and cold email, $100 spent on a phone number and an outreach tool.
Runs offline; output is fixed and deterministic.
"""

import os

ENTRY = (
    "Sell AI missed-call text-back + review replies to plumbers at $149/mo. "
    "Day 1: pull 200 leads off Google Maps, email 50 a free 7-day trial. "
    "Spend $100 on a Twilio number + Instantly. "
    "Close 3 by day 14 = $447/mo recurring. "
    "Edge: boring local niches, not saturated AI agencies."
)


def main() -> None:
    # Gate: the scorer only accepts 1-280 Unicode code points, not whitespace only.
    assert 1 <= len(ENTRY) <= 280 and ENTRY.strip(), "entry out of gate bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
