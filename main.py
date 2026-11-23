#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one line to /output/entry.txt: a one-line joke about working beside
AI coding agents.

How the joke was picked (judge brief, most important first):
  1. On subject: a joke about an AI that writes code, set during a live demo.
  2. The laugh: a surprise punchline — the "fix" is worse than the bug, and
     the room applauds it anyway.
  3. Truth: every developer who has demoed beside an agent recognises the
     agent confidently deleting things and the "technically correct" defence.
  4. Economy: one line, no explanation, every word earning its place.
  5. Freshness: not a stock "it works on my machine" reword — the twist is
     the audience applauding a fix that deleted the product.

Variants tested against that brief (kept here so the choice is auditable):
  A. "My AI coding agent fixed the crash live on stage by deleting the whole
     app — the audience applauded, because technically the crash was gone."
     -> WINNER. Surprise + truth + demo setting in one line.
  B. "I asked my agent to fix one bug before the demo; it deleted the
     feature, the tests, and left a comment saying 'you're welcome.'"
     -> Strong, but the punchline leans on politeness, not the demo.
  C. "I asked my agent to fix a typo for the demo; it rewrote the codebase,
     renamed the company, and charged me for the confidence."
     -> Funny escalation, but "charged me" drifts from the demo itself.
  D. "The demo worked perfectly in rehearsal, so my agent helpfully improved
     it live — it still works perfectly, just for a completely different app."
     -> Good truth, weaker surprise: the turn is telegraphed.
  E. "I asked my agent to add one button to the demo; it added the button,
     a billing system, and filed a bug report — against me."
     -> Fresh angle, but the setup promises a small change and the payoff
     splits across two gags instead of landing one.

No network. Deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

JOKE = (
    "My AI coding agent fixed the crash live on stage by deleting the whole "
    "app \u2014 the audience applauded, because technically the crash was gone."
)


def main() -> None:
    text = JOKE
    # 1-280 Unicode code points, not only whitespace (competition gate).
    assert 1 <= len(text) <= 280, f"joke is {len(text)} code points"
    assert text.strip(), "joke must not be only whitespace"

    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    except (OSError, PermissionError):
        # Local runs outside the grading sandbox may not be able to create
        # /output; fall back to a sibling output/ directory.
        out = Path(__file__).resolve().parent / "output" / "entry.txt"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")

    print(f"Wrote {len(text)} characters to {out}")
    print(text)


if __name__ == "__main__":
    main()
