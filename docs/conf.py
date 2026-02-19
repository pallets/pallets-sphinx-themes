import importlib.metadata

# Project --------------------------------------------------------------

project = "Pallets-Sphinx-Themes"
version = release = importlib.metadata.version("pallets-sphinx-themes").partition(
    ".dev"
)[0]

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
    "sphinx": ("https://sphinx-doc.org", None),
}
myst_enable_extensions = [
    "fieldlist",
]
myst_heading_anchors = 2

# HTML -----------------------------------------------------------------

html_theme = "flask"
html_copy_source = False
html_show_copyright = False
html_use_index = False
html_domain_indices = False
