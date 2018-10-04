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

Troubleshooting
---------------

These themes require the *autodoc* extension.

If you didn't setup *Sphinx* with *autodoc*, you need to activate it in ``conf.py``. Ensure that ``"sphinx.ext.autodoc"`` is loaded **before** ``"pallets_sphinx_themes"`` in the list assigned to the extensions config value. 

To make sure that ``sphinx-build`` properly loads ``autodoc``, uncomment the lines near the top of ``conf.py``:

.. code-block:: python

	# If extensions (or modules to document with autodoc) are in another directory,
	# add these directories to sys.path here. If the directory is relative to the
	# documentation root, use os.path.abspath to make it absolute, like shown here.
	#
	import os
	import sys
	sys.path.insert(0, os.path.abspath('..'))

If you have setup your *Sphinx* project to use separate ``build`` and ``source`` directories, the path should instead be:

.. code-block:: python

	sys.path.insert(0, os.path.abspath('../..'))