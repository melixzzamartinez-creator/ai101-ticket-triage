"""Load the AI101 support tickets."""
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
FILES = {"train": "tickets.csv", "test": "test_tickets.csv"}


def load_tickets(split="train"):
    """Return a list of tickets. Each ticket is a dict with the keys id, channel, text, category.

    split="train" -> the 240 tickets you build and tune with (data/tickets.csv)
    split="test"  -> the 60 held-out tickets you only measure with (data/test_tickets.csv)
    """
    if split not in FILES:
        raise ValueError(f'split must be "train" or "test", not {split!r}')
    with open(DATA_DIR / FILES[split], newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    for split in FILES:
        tickets = load_tickets(split)
        print(f"{split}: {len(tickets)} tickets")
    first = load_tickets("train")[0]
    print("first training ticket:", first)
