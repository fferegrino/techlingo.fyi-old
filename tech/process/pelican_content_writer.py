from datetime import datetime
from pathlib import Path

from tech.entities.processed_lingo import ProcessedLingo
from tech.process.lingo_processor import LingoProcessor


class PelicanContentWriter(LingoProcessor):
    def __init__(self):
        self.generated_content_path = Path("content", "generated")
        self.generated_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("tech/article_template.html") as readable:
            self.template = readable.read()

    def process(self, processed: ProcessedLingo):
        end_content = str(self.template)

        replacements = [
            ("NON_LOCALISED_TITLE", processed.original_title),
            ("TITLE", processed.localised_title),
            ("INITIAL", processed.initial),
            ("ID", processed.identifier),
            ("CONTENT", processed.content),
            ("AUTHOR_URL", processed.author_url),
            ("AUTHOR", processed.author),
            ("TAGS", ", ".join(processed.tags)),
            ("CATEGORY", processed.category),
            ("LANGUAGE", processed.language),
            ("ACRONYM", processed.decorated_acronym),
            ("ABBREVIATION", processed.abbr),
            ("SLUG", processed.slug),
            ("DATE", self.generated_date),
        ]
        for tag, value in replacements:
            end_content = end_content.replace(tag, value)

        output_path = self.generated_content_path / processed.path / "post.html"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as writeable:
            writeable.write(end_content)
