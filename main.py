import os

# Final entry line, built from parts so each piece stays readable.
# The wording itself must not change: it is the submitted diagnosis.
PREFIX = "Diagnosis: "
CONDITION = "chronic main-character syndrome"
SEPARATOR = " \u2014 "
BEHAVIOUR = "you treat every group chat as your therapy session, and you're the villain in everyone else's."

LINE = PREFIX + CONDITION + SEPARATOR + BEHAVIOUR

# Bounty limit: entry must be 1-200 characters long.
if not 1 <= len(LINE) <= 200:
    raise ValueError(f"entry length {len(LINE)} out of range 1-200")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
