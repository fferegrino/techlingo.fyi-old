from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

from tech.entities import languages
from tech.entities.author import Author
from tech.entities.lingo import Lingo


@dataclass
class ProcessedLingo:
    original_title: str
    localised_title: str
    identifier: str
    content: str
    author: str
    author_url: str
    category: str
    language: str
    path: Path
    tags: List[str]

    @property
    def initial(self) -> str:
        return self.identifier[0]

    @property
    def slug(self) -> str:
        return str(self.path)

    @classmethod
    def from_thing(cls, lingo: Lingo, author: Author, original_title: str, path: Path):
        return cls(
            original_title=original_title,
            localised_title=lingo.term,
            identifier=lingo.id,
            content=lingo.text,
            author=author.display_name,
            author_url=author.main_link,
            category=lingo.category,
            language=languages[lingo.language],
            path=path,
            tags=lingo.tags or [],
        )

    def asdict(self):
        inner_dict = asdict(self)
        inner_dict.pop("path")
        inner_dict.update({"initial": self.initial, "slug": self.slug})
        return inner_dict
