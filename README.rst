Pallets Sphinx Themes
=====================

Themes for the Pallets projects. If you're writing an extension, use the
appropriate theme to make your documentation look consistent.

Available themes:

-   flask
-   jinja
-   werkzeug
-   click

Install this package:

.. code-block:: text

    pip install Pallets-Sphinx-Themes

Enable the extension and choose the theme in ``docs/conf.py``:

.. code-block:: python

    extensions = [
        "pallets_sphinx_themes",
        ...
    ]

    html_theme = "flask"
