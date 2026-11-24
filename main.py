"""One Word for the Boss — entry program.

Picks a single word that describes the boss and writes it, exactly,
to entry.txt (no trailing newline, no extra text).
"""

import os

# Shortlist, best first. Each candidate is judged against the five
# criteria in order: (1) a real word people use about their boss,
# (2) funny on its own, (3) rings true about a real boss habit,
# (4) fresh, not the first word anyone thinks of, (5) works across
# industries.
CANDIDATES = [
    # Hovercraft: a boss who hovers over employees' shoulders.
    # (1) Real word people use about a boss: "he's hovering again".
    # (2) Funny on its own: the image of a boss floating, noisy,
    #     going nowhere, is instantly visual. (3) Rings true: the
    #     hover-over-the-shoulder boss is a real, everyday habit.
    # (4) Fresh: nobody's first word for a boss; it beats generic
    #     "Micromanager", which fails criterion 4 outright.
    # (5) Cross-industry: every workplace has a hoverer.
    "Hovercraft",
    # Helicopter: vivid and true, but "helicopter boss" is a known
    # phrase, so it scores lower on freshness (criterion 4).
    "Helicopter",
    # Desk-leaner: funny, true for office work, but fails (5):
    # it means little outside desk jobs.
    "Desk-leaner",
]


def validate_word(word):
    """Enforce the competition gate: 1-30 UTF-8 chars, not blank."""
    if not isinstance(word, str):
        raise ValueError("entry word must be a string")
    if not word.strip():
        raise ValueError("entry word must not be blank")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry word must be 1-30 characters")
    return word


def pick_word(candidates):
    """Return the top-ranked candidate, after gate validation."""
    return validate_word(candidates[0])


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    word = pick_word(CANDIDATES)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
