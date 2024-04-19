# Pallets Sphinx Themes

Themes for the Pallets projects. If you're writing an extension, use the
appropriate theme to make your documentation look consistent.

Available themes:

-   flask
-   jinja
-   werkzeug
-   click

Enable the extension and choose the theme in `docs/conf.py`:

```python
extensions = [
    "pallets_sphinx_themes",
    ...
]

html_theme = "flask"
```
