import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from slugify import slugify

from tech.lingo import Lingo
from tech.load import load_base_lingos, load_extra_lingos


def format():
    files: Dict[str, List[Lingo]] = defaultdict(list)
    for lingo in load_base_lingos():
        files[f"{lingo.category}"].append(lingo)
    for lingo in load_extra_lingos():
        files[f"{lingo.category}-{lingo.language}"].append(lingo)

    lingos = Path("lingos")
    for t, lists in files.items():
        jsons = []
        for _lingo in sorted(lists, key=lambda lng: slugify(lng.term)):
            __lingo = _lingo.asdict()
            __lingo["id"] = __lingo.get("id", slugify(_lingo.term))
            jsons.append(__lingo)
        with open(lingos / f"{t}.json", "wt", encoding="utf8") as w:
            json.dump(jsons, w, indent=2, ensure_ascii=False)
            w.write("\n")


if __name__ == "__main__":
    format()
