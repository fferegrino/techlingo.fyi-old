from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List, Optional

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
    acronym: str
    abbreviation: str
    language: str
    path: Path
    tags: List[str]
    term_slug: str

    @property
    def initial(self) -> str:
        return self.identifier[0]

    @property
    def decorated_acronym(self) -> str:
        if self.acronym:
            return "".join(
                (f"<b>{char}</b>" if char.isupper() else char for char in self.acronym)
            )
        return ""

    @property
    def abbr(self) -> str:
        return self.abbreviation or ""

    @property
    def slug(self) -> str:
        return str(self.path)

    @property
    def alias(self) -> Optional[str]:
        return None if self.language != "English" else self.term_slug

    @classmethod
    def from_thing(
        cls,
        lingo: Lingo,
        author: Author,
        original_title: str,
        path: Path,
        term_slug: str,
    ):
        return cls(
            original_title=original_title,
            localised_title=lingo.term,
            identifier=lingo.id,
            content=lingo.text,
            author=author.display_name,
            author_url=author.main_link,
            category=lingo.category,
            abbreviation=lingo.abbreviation,
            acronym=lingo.acronym,
            language=languages[lingo.language],
            path=path,
            tags=lingo.tags or [],
            term_slug=term_slug,
        )

    def asdict(self):
        inner_dict = asdict(self)
        inner_dict.pop("path")
        inner_dict.update(
            {"initial": self.initial, "alias": self.alias, "slug": self.slug}
        )
        return inner_dict
