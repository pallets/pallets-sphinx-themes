from pallets_sphinx_themes import get_version

# Project --------------------------------------------------------------

project = "Pallets-Sphinx-Themes"
copyright = "2007 Pallets"
author = "Pallets"
release, version = get_version("pallets-sphinx-themes")

# General --------------------------------------------------------------

default_role = "code"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "myst_parser",
    "pallets_sphinx_themes",
]
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_preserve_defaults = True
extlinks = {
    "issue": ("https://github.com/pallets/pallets-sphinx-themes/issues/%s", "#%s"),
    "pr": ("https://github.com/pallets/pallets-sphinx-themes/pull/%s", "#%s"),
}
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}
myst_enable_extensions = [
    "fieldlist",
]
myst_heading_anchors = 2

# HTML -----------------------------------------------------------------

html_theme = "flask"
html_theme_options = {"index_sidebar_logo": False}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html", "ethicalads.html"]}
html_title = f"{project} Documentation ({version})"
html_copy_source = False
html_show_sourcelink = False
html_show_copyright = False
html_use_index = False
html_domain_indices = False
