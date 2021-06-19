from datetime import datetime
from pathlib import Path

from slugify import slugify

from tech.load import load_authors, load_base_lingos, load_lingos

languages = {"es": "Spanish", "en": "English"}


def convert():
    """
    Converts the files under lingos/ into posts that can be processed by pelican
    :return:
    """
    generated_content_path = Path("content", "generated")

    generated_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("tech/article_template.html") as readable:
        template = readable.read()

    authors = load_authors()

    base_lingos = {ling.id: ling.term for ling in load_base_lingos()}

    for lingo in load_lingos():
        term_slug = slugify(lingo.term)
        path = Path(lingo.category, term_slug, lingo.language)
        author = authors[lingo.author]
        end_content = str(template)
        replacements = [
            ("NON_LOCALISED_TITLE", base_lingos[lingo.id]),
            ("TITLE", lingo.term),
            ("INITIAL", lingo.id[0]),
            ("ID", lingo.id),
            ("CONTENT", lingo.text),
            ("AUTHOR_URL", author.main_link),
            ("AUTHOR", author.display_name),
            ("TAGS", ", ".join(lingo.tags)),
            ("CATEGORY", lingo.category),
            ("LANGUAGE", languages[lingo.language]),
            ("SLUG", str(path)),
            ("DATE", generated_date),
        ]
        for tag, value in replacements:
            end_content = end_content.replace(tag, value)

        (generated_content_path / path).mkdir(parents=True, exist_ok=True)
        with open(generated_content_path / path / "post.html", "w") as writeable:
            writeable.write(end_content)


if __name__ == "__main__":
    convert()
