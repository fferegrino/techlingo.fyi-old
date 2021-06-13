from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Lingo:
    term: str
    text: str
    tags: List[str] = field(default_factory=list)
    twitter: Optional[str] = None