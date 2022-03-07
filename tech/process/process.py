from pathlib import Path

from slugify import slugify

from tech.entities.processed_lingo import ProcessedLingo
from tech.load import load_authors, load_base_lingos, load_lingos
from tech.process.lingo_processor import LingoProcessor


def process_techlingos(writer: LingoProcessor):
    """
    Converts the files under lingos/ into posts that can be processed by pelican
    :return:
    """

    authors = load_authors()
    base_lingos = {ling.id: ling.term for ling in load_base_lingos()}

    with writer as content_writer:
        for lingo in load_lingos():
            term_slug = slugify(lingo.term)
            path = Path(lingo.category, term_slug, lingo.language)
            author = authors[lingo.author]
            base_lingo_name = base_lingos[lingo.id]

            processed_lingo = ProcessedLingo.from_thing(
                lingo, author, base_lingo_name, path, term_slug
            )

            content_writer.process(processed_lingo)
