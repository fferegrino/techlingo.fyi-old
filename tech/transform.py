from pathlib import Path
from datetime import datetime
from slugify import slugify
from tech.load import load_lingos


def convert():
    """
    Converts the files under lingos/ into posts that can be processed by pelican
    :return:
    """
    generated_content_path = Path("content", "generated")

    generated_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("tech/template.html") as readable:
        template = readable.read()

    for lingo in load_lingos():
        term_slug = slugify(lingo.term)
        path = Path(lingo.category, term_slug, lingo.language)

        end_content = str(template)

        replacements = [
            ("TITLE", lingo.term),
            ("INITIAL", term_slug[0]),
            ("BODY", lingo.text),
            ("AUTHOR", lingo.twitter),
            ("TAGS", ", ".join(lingo.tags)),
            ("CATEGORY", lingo.category),
            ("LANGUAGE", lingo.language),
            ("SLUG", str(path)),
            ("DATE", generated_date),
         ]

        for tag, value in replacements:
            end_content = end_content.replace(tag, value)

        (generated_content_path/path).mkdir(parents=True, exist_ok=True)
        with open(generated_content_path/path/"post.html", "w") as writeable:
            writeable.write(end_content)


if __name__ == '__main__':
    convert()
