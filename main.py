"""Till Firmware Do Us Part — make.fun entry.

A robot's wedding vow, one line: it promises to love its partner
through every update, every crash, and every low-battery warning —
and never to factory-reset us. The joke lands in the last beat:
a factory reset would erase the partner, so refusing it is both
the laugh and the vow of fidelity.
"""

TEXT = "I promise to love you through every update, every crash, and every low-battery warning \u2014 and never to factory-reset us."

# Gate bounty: 1-200 karakter, satu kalimat. TEXT 119 karakter.
MAX_LEN = 200


def check_len(text, lo=1, hi=MAX_LEN):
    """Pastikan panjang teks dalam batas bounty (1-200 karakter)."""
    assert lo <= len(text) <= hi, f"panjang {len(text)} di luar {lo}-{hi}"
    return len(text)


def save_line(text, path="/output/entry.txt"):
    """Tulis teks ke file tanpa newline tambahan."""
    from pathlib import Path

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def main():
    n = check_len(TEXT)
    save_line(TEXT)
    back = open("/output/entry.txt", encoding="utf-8").read()
    assert back == TEXT, "isi file tidak sama persis dengan TEXT"
    print(f"OK: {n} karakter -> /output/entry.txt")


if __name__ == "__main__":
    main()
