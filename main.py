"""Entry for "Two Robots in an Elevator" (make.fun).

One robot breaks the silence with the most relatable machine excuse
there is: pretending to run an update so nobody expects conversation.
The awkwardness lands because both of them are doing it.
"""

ENTRY = (
    "Don't mind me, I'm just updating my firmware in here so nobody "
    "talks to me. Oh. You too?"
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
