from dataclasses import asdict, dataclass, field
from typing import List, Optional


@dataclass
class Author:
    username: str
    display_name: str
    main_link: str

    def asdict(self):
        inner_dict = asdict(self)
        return inner_dict
