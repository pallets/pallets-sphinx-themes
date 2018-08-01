import sys
from collections import namedtuple

import os
import pkg_resources
import textwrap
from sphinx.builders._epub_base import EpubBuilder
from sphinx.builders.html import SingleFileHTMLBuilder

from .theme_check import only_pallets_theme, set_is_pallets_theme
from .versions import load_versions


def setup(app):
    base = os.path.dirname(__file__)

    for name in (
        "pocoo",
        "flask",
        "jinja",
        "werkzeug",
        "click",
        "babel",
        "platter",
        "flask-sqlalchemy",
    ):
        app.add_html_theme(name, os.path.join(base, name))

    app.add_config_value("is_pallets_theme", None, "html")
    app.add_config_value("singlehtml_sidebars", None, "html")

    app.connect("builder-inited", set_is_pallets_theme)
    app.connect("builder-inited", load_versions)
    app.connect("builder-inited", singlehtml_sidebars)
    app.connect("html-collect-pages", html_collect_pages)
    app.connect("html-page-context", canonical_url)

    own_release, _ = get_version(__name__)
    return {"version": own_release, "parallel_read_safe": True}


@only_pallets_theme(default=())
def html_collect_pages(app):
    is_epub = isinstance(app.builder, EpubBuilder)
    config_pages = app.config.html_additional_pages

    if not is_epub and "404" not in config_pages:
        yield ("404", {}, "404.html")


@only_pallets_theme()
def canonical_url(app, pagename, templatename, context, doctree):
    base = context.get("canonical_url")

    if not base:
        return

    target = app.builder.get_target_uri(pagename)
    context["canonical_url"] = base + target


@only_pallets_theme()
def singlehtml_sidebars(app):
    if (
        app.config.singlehtml_sidebars is not None
        and isinstance(app.builder, SingleFileHTMLBuilder)
    ):
        app.config.html_sidebars["index"] = app.config.singlehtml_sidebars


def get_version(name):
    try:
        release = pkg_resources.get_distribution(name).version
    except ImportError:
        print(
            textwrap.fill(
                "'{name}' must be installed to build the documentation."
                " Install from source using `pip install -e .` in a"
                " virtualenv.".format(name=name)
            )
        )
        sys.exit(1)

    version = ".".join(release.split(".", 2)[:2])
    return release, version


ProjectLink = namedtuple("ProjectLink", ("title", "url"))
