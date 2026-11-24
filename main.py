"""Write the funniest toaster error message to the output directory.

The program is deterministic: it writes one fixed line to
${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt. No network, no wall clock,
no randomness, no writes anywhere else.
"""

import os

MESSAGE = "ERROR: The bread asked to be left alone. I respect that."


def main() -> None:
    if not 1 <= len(MESSAGE) <= 120 or not MESSAGE.strip():
        raise ValueError("entry must be 1-120 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()
