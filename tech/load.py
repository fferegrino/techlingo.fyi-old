import json
from pathlib import Path
from typing import Any, Dict, Generator

import tomli

from tech.entities.author import Author
from tech.entities.lingo import Lingo

lingos_path = Path("lingos")


def load_authors() -> Dict[str, Author]:
    authors = dict()
    with open(lingos_path / "_authors.txt", "rb") as rb:
        authors_toml = tomli.load(rb)
        for username, data in authors_toml.items():
            authors[username] = Author(username=username, **data)
    return authors


def load_lingos() -> Generator[Lingo, Any, None]:
    for file in sorted(lingos_path.glob("*.txt")):
        if file.name.startswith("_"):
            continue
        with open(file, "rb") as rb:
            data = tomli.load(rb)
            data["language"] = "en"
            data["category"] = "general"
            different_languages = data.pop("lang", dict())

            yield Lingo(**data)

            for language, tch in different_languages.items():
                yield Lingo(id=data["id"], language=language, category="general", **tch)
