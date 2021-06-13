from pathlib import Path

from slugify import slugify
import json

from tech.lingo import Lingo


def convert():
    """
    Converts the files under lingos/ into posts that can be processed by pelican
    :return:
    """
    lingos_path = Path("lingos")
    generated_content_path = Path("content", "generated")

    with open("tech/template.html") as readable:
        template = readable.read()

    for file in lingos_path.glob("*.json"):
        area, _, language = file.stem.partition("-")

        with open(file) as readable:
            lingos = json.load(readable)

            for lingo_json in lingos:
                lingo = Lingo(**lingo_json)
                term_slug = slugify(lingo.term)
                path = Path(area, term_slug, language)

                end_content = str(template)

                replacements = [
                        ("TITLE", lingo.term),
                        ("BODY", lingo.text),
                        ("AUTHOR", lingo.twitter),
                        ("TAGS", ", ".join(lingo.tags)),
                        ("CATEGORY", area),
                        ("LANGUAGE", language),
                        ("SLUG", str(path)),
                     ]

                for tag, value in replacements:
                    end_content = end_content.replace(tag, value)


                (generated_content_path/path).mkdir(parents=True, exist_ok=True)
                with open(generated_content_path/path/"post.html", "w") as writeable:
                    writeable.write(end_content)


if __name__ == '__main__':
    convert()
