import logging
import os.path
from pathlib import Path
from urllib.parse import urlparse

from pelican import signals

logger = logging.getLogger(__name__)


class AliasGenerator(object):
    TEMPLATE = """<!DOCTYPE html><html><head><meta charset="utf-8" />
<meta http-equiv="refresh" content="0;url={destination}" />
</head></html>"""

    def __init__(self, context, settings, path, theme, output_path, *args):
        self.output_path = output_path
        self.context = context
        self.alias_delimiter = settings.get("ALIAS_DELIMITER", ",")

    def create_alias(self, page, alias):
        # If path starts with a / add index.html
        if alias[-1] == "/":
            relative_alias = Path(alias, "index.html")
        else:
            relative_alias = Path(alias)

        path = Path(self.output_path, relative_alias)

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
        except OSError:
            pass

        logger.info("[alias] Writing to alias file %s" % path)
        with open(path, "w") as fd:
            destination = page.url
            # if schema is empty then we are working with a local path
            if not urlparse(destination).scheme:
                # if local path is missing a leading slash then add it
                if not destination.startswith("/"):
                    destination = "/{0}".format(destination)
            fd.write(self.TEMPLATE.format(destination=destination))

    def generate_output(self, writer):
        pages = (
            self.context["pages"]
            + self.context["articles"]
            + self.context.get("hidden_pages", [])
        )

        for page in pages:
            aliases = page.metadata.get("alias", [])
            if type(aliases) != list:
                aliases = aliases.split(self.alias_delimiter)
            for alias in aliases:
                alias = alias.strip()
                logger.info("[alias] Processing alias %s" % alias)
                self.create_alias(page, alias)


def get_generators(generators):
    return AliasGenerator


def register():
    signals.get_generators.connect(get_generators)
