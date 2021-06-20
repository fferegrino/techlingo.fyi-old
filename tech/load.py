import json
from pathlib import Path
from typing import Any, Dict, Generator

from tech.author import Author
from tech.lingo import Lingo

lingos_path = Path("lingos")


def load_authors() -> Dict[str, Author]:
    authors = dict()
    with open(lingos_path / "_authors.json") as r:
        authors_json = json.load(r)
        for au in authors_json:
            authors[au["username"]] = Author(**au)
    return authors


def load_base_lingos() -> Generator[Lingo, Any, None]:
    # Read base lingos, EN language
    for file in lingos_path.glob("*.json"):
        category = file.stem
        if "-" in category or file.stem.startswith("_"):
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


def load_extra_lingos() -> Generator[Lingo, Any, None]:
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


def load_lingos() -> Generator[Lingo, Any, None]:
    yield from load_base_lingos()
    yield from load_extra_lingos()
