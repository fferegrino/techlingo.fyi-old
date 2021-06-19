from dataclasses import asdict, dataclass, field
from typing import List, Optional


@dataclass
class Lingo:
    id: str
    term: str
    text: str
    category: str
    language: str
    tags: List[str] = field(default_factory=list)
    twitter: Optional[str] = None

    def asdict(self):
        inner_dict = asdict(self)
        skip = {"language", "category"}
        return {k: v for k, v in inner_dict.items() if k not in skip and bool(v)}
