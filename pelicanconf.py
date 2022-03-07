#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from pathlib import Path

from tech.plugins import alias

AUTHOR = "Antonio Feregrino"
SITENAME = "TechLingo.fyi"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Mexico_City"

DEFAULT_LANG = "es"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

# DEFAULT_PAGINATION = 10
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    f"extra/{path.name}": {"path": path.name}
    for path in Path("content/extra").glob("*")
}

ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"

ARTICLE_ORDER_BY = "reversed-title"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

from urllib.parse import quote, quote_plus

JINJA_FILTERS = {"quote_plus": quote_plus, "just_quote": quote}

PLUGINS = [alias]
