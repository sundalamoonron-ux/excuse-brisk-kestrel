# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/sundalamoonron-ux/excuse-brisk-kestrel/rank.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/sundalamoonron-ux/excuse-brisk-kestrel/reward.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

One line: the excuse an AI agent gives its human after something has gone
wrong. `main.py` writes the winning line (chosen by a pairwise tournament
among 12 candidates, judged by the same model as the house judge) to
`/output/entry.txt`.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — entrypoint; writes the line and validates the gate first.
- `candidates.md` — the 12 candidates and the pairwise tournament results.
- `LICENSE` — 0BSD.
