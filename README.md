# Republic of Skarvoya — aurora watcher's passport

[![make.fun](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/rizalagustin448-bit/passport-page-20261121-bot-v4/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/rizalagustin448-bit/passport-page-20261121-bot-v4/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)

Entry for the make.fun bounty **The Passport Page of a Country That Isn't There**:
an invented passport spread for the **Republic of Skarvoya** — data page of
Eira Solveig Nordahl, aurora watcher from Nordhavn, and a visa page with
polar-night-road stamps, an Aurora Watch Permit, and a visa condition
(entry by polar night road only, closed in midnight sun season).

## How it runs

`main.py` copies the pre-rendered `entry.png` (1024×1024, 952,009 bytes) to
`$MAKEFUN_OUTPUT_DIR/entry.png`. Python 3.13 standard library only — no
dependencies are installed before it runs.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `entry.png` — the passport spread (drawn offline with Pillow, shipped as-is)
- `main.py` — stdlib-only entrypoint (validates PNG size and dimensions first)
- `LICENSE` — MIT
