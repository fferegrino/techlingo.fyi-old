from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from tech.entities.processed_lingo import ProcessedLingo
from tech.process.lingo_processor import LingoProcessor


class PelicanContentWriter(LingoProcessor):
    def __init__(self):
        loader = FileSystemLoader(searchpath="./tech")
        self.env = Environment(loader=loader)

        self.generated_content_path = Path("content", "generated")
        self.generated_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def process(self, processed: ProcessedLingo):
        template = self.env.get_template("article_template.html")

        output_path = self.generated_content_path / processed.path / "post.html"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        processed_dict = processed.asdict()
        processed_dict["tags"] = ", ".join(processed_dict["tags"])

        end_content = template.render(
            **processed_dict, generated_date=self.generated_date
        )
        with open(output_path, "w") as writeable:
            writeable.write(end_content)
