"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single line a hopeless tech support agent says to a
desperate customer, twisting the classic "turn it off and on again".
Stdlib only, no network, deterministic.

The twist: the customer has obviously already restarted it — the agent
knows, and still prescribes the same cure, only this time with feeling.
Cheerful uselessness, not blame: the customer is never the butt of it.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? "
    "Great \u2014 now do it again, but this time, mean it."
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 199):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-199: {ENTRY!r}")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
