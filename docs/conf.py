from pallets_sphinx_themes import get_version
from pallets_sphinx_themes import ProjectLink

# -- Project Information --------------------------------------------------------------

project = "Pallets-Sphinx-Themes"
copyright = "2007 Pallets"
author = "Pallets"
release, version = get_version("pallets-sphinx-themes")

# -- General Configuration --------------------------------------------------------------

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

# -- HTML Theming -----------------------------------------------------------------

html_theme = "flask"
html_static_path = ['_static']
templates_path = ["_templates"]
html_logo = "_static/pallets.png"
html_context = {
    "project_links": [
        ProjectLink("Donate", "https://palletsprojects.com/donate"),
        ProjectLink("PyPI Releases", "https://pypi.org/project/Pallets-Sphinx-Themes/"),
        ProjectLink("Source Code", "https://github.com/pallets/pallets-sphinx-themes/"),
        ProjectLink("Issue Tracker", "https://github.com/pallets/pallets-sphinx-themes/issues/"),
        ProjectLink("Chat", "https://discord.gg/pallets"),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html", "octicon.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html", "octicon.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html", "ethicalads.html"]}
html_title = f"{project} Documentation ({version})"
html_copy_source = False
html_show_sourcelink = False
html_use_index = False
html_domain_indices = False