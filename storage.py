import json
from pathlib import Path

DATA_FILE = Path("items.json")


def load_items():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_items(items):
    with open(DATA_FILE, "w") as file:
        json.dump(items, file, indent=4)