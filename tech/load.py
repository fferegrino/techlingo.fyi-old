import json
from pathlib import Path
from typing import Generator, Any

from tech.lingo import Lingo


def load_base_lingos() -> Generator[Lingo, Any, None]:
    lingos_path = Path("lingos")
    # Read base lingos, EN language
    for file in lingos_path.glob("*.json"):
        category = file.stem
        if "-" in category:
            continue
        with open(file) as readable:
            lingos = json.load(readable)
            for lingo_json in lingos:
                lingo = Lingo(
                    category=category,
                    language="en",
                    **lingo_json,
                )
                yield lingo

def load_lingos() -> Generator[Lingo, Any, None]:
    lingos_path = Path("lingos")

    yield from load_base_lingos()
    for file in lingos_path.glob("*-*.json"):
        category, _, language = file.stem.partition("-")

        with open(file) as readable:
            lingos = json.load(readable)
            for lingo_json in lingos:
                lingo = Lingo(
                    category=category,
                    language=language,
                    **lingo_json,
                )
                yield lingo
