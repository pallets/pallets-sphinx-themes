# Pallets Sphinx Themes

The Documentation for the Pallets Sphinx Themes.

The Pallets Sphinx Themes are a series of themes that are used across multiple pallets projects, such as [Flask](https://flask.palletsprojects.com/en/stable/), [Jinja](https://jinja.palletsprojects.com/en/stable/), [Click](https://flask.palletsprojects.com/en/stable/), and [Werkzeug](https://werkzeug.palletsprojects.com/en/stable/).

## Installation

The 4 themes are available as a PyPI package, and can be installed with:

``` console
pip install Pallets-Sphinx-Themes
```

Afterwards, you need to explicitly activate the themes by adding it to your list of extensions in `conf.py`:

``` python
extensions = [
    "pallets_sphinx_themes",
    ...
]
```

And set your `html_theme` to the desired theme. For example, if you want to use the Flask theme, enable it through:

``` python
html_theme = "flask"
```

## Navigation

After completing the installation, you can move onto actually setting up the theme.

```{toctree}
setup.md
```