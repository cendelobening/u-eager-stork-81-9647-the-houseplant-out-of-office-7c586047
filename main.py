#!/usr/bin/env python3
"""The Houseplant Out-of-Office — a one-line auto-reply written by a fern.

Writes the entry line to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Pure standard library only.
"""

import os
import stat
import sys
import tempfile

# Revised entry line: the ending is now a direct demand from the fern
# ("Water me, and I'll reply") instead of a passive promise — the plant
# has agency, and the bargain (water in exchange for a reply) is the joke.
ENTRY = "Out of office: I'm the fern, ignored since March. Your email queues behind my thirst. Water me, and I'll reply."


def validate(text):
    """Check the entry line meets the gate: 1-120 chars, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if len(text) > 120:
        raise ValueError("entry is %d characters, over the 120 limit" % len(text))
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("entry must be a single line with no tabs/newlines")
    if len(text.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("entry must not contain control characters")
    # The encoded form must also be a single line with no trailing newline.
    if b"\n" in text.encode("utf-8"):
        raise ValueError("entry must not contain a newline when encoded")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    final_path = os.path.join(out_dir, "entry.txt")
    data = entry.encode("utf-8")
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        os.chmod(tmp_path, 0o644)
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, final_path)
        os.chmod(final_path, 0o644)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    # Read back and verify: bytes, UTF-8, no trailing newline, mode 0644.
    with open(final_path, "rb") as f:
        raw = f.read()
    if raw != data:
        raise SystemExit("verification failed: bytes on disk differ from entry")
    decoded = raw.decode("utf-8")
    if decoded != entry:
        raise SystemExit("verification failed: decoded text differs from entry")
    if raw.endswith(b"\n"):
        raise SystemExit("verification failed: trailing newline present")
    mode = stat.S_IMODE(os.stat(final_path).st_mode)
    if mode != 0o644:
        raise SystemExit("verification failed: mode is %o, expected 0644" % mode)
    print("Wrote %d characters to %s" % (len(entry), final_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
