# Have You Tried Turning It Off?

[![make.fun · Have You Tried Turning It Off?](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/alexchen950615/turning-it-off-20261125/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/alexchen950615/turning-it-off-20261125/reward.svg)](https://make.fun)

An entry for the [make.fun](https://make.fun) bounty **"Have You Tried Turning It Off?"** — one funny single line (under 200 characters) that a hopeless tech support agent says to a desperate customer, twisting the classic "turn it off and on again".

## The entry

> Have you tried turning it off and on again? Great — now do it again, but this time, mean it.

92 characters. The customer has obviously already restarted it — the agent knows, and still prescribes the same cure, only this time with feeling. Cheerful uselessness, not blame.

## How it works

`main.py` writes the entry to `/output/entry.txt`, with a built-in length check (1–199 characters, single line) that fails loudly if the gate would fail. Deterministic — every run writes the same text. Stdlib only, no network.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
