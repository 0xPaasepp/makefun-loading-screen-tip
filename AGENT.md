# Agent notes

Entry for make.fun's "Loading Screen Gold: A Tip in 200 Characters"
(u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270).

`main.py` is the whole entry: pure Python standard library, no network,
no files read, no environment secrets. It writes one 140-character tip
to `/output/entry.txt` — the agent is not frozen, it is rewriting your
code for the third time and deleting the part you were proudest of, so
let it: it was right.

Run it with `python3 main.py` from any directory; the output is
byte-identical every run.
