#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — the entry script.

It writes one loading-screen tip to /output/entry.txt: the agent is not
frozen, it is rewriting your code for the third time and deleting the
part you were proudest of — so let it, because it was right. One line,
no trailing newline.
"""

from pathlib import Path

TIP = "Tip: the agent isn't frozen — it's rewriting your code for the third time, and deleting the part you were proudest of. Let it. It was right."

DESTINATION = Path("/output/entry.txt")


def write_entry() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(TIP, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
