Version 1.1.4
=============

Released 2019-01-28

-   Store a page's canonical URL in
    ``html_context["page_canonical_url"]`` rather than overwriting
    ``canonical_url``, for compatibility with Read the Docs. (`#21`_)

.. _#21: https://github.com/pallets/pallets-sphinx-themes/pull/21


Version 1.1.3
=============

Released 2019-01-28

-   Move the Read the Docs search flag to the ``footer`` block to ensure
    it executes after Read the Docs injects its data. (`#20`_)

.. _#20: https://github.com/pallets/pallets-sphinx-themes/pull/20


Version 1.1.2
=============

Released 2018-09-24

-   Strip ".x" placeholder when parsing versions for sidebar.
    (`#7`_, `#17`_)

.. _#7: https://github.com/pallets/pallets-sphinx-themes/issues/7
.. _#17: https://github.com/pallets/pallets-sphinx-themes/pull/17


Version 1.1.1
=============

Released 2018-09-16

-   Add configurable ".x" placholder to versions, producing strings like
    "1.2.x". (`#6`_, `#12`_)
-   Add dependency on "packaging" to support older Sphinx versions.
    (`#9`_, `#11`_)
-   Backport ``shlex.quote`` for Python 2. (`#13`_, `#14`_)

.. _#6: https://github.com/pallets/pallets-sphinx-themes/issues/6
.. _#9: https://github.com/pallets/pallets-sphinx-themes/issues/9
.. _#11: https://github.com/pallets/pallets-sphinx-themes/pull/11
.. _#12: https://github.com/pallets/pallets-sphinx-themes/pull/12
.. _#13: https://github.com/pallets/pallets-sphinx-themes/issues/13
.. _#14: https://github.com/pallets/pallets-sphinx-themes/pull/14


Version 1.1.0
=============

Released 2018-08-28

-   Modernize ``click`` theme. The ``.. click:example::`` and
    ``.. click:run::`` directives used by Click are available and ported
    to Python 3.
-   Modernize ``werkzeug`` theme. (`#4`_)
-   Modernize ``jinja`` theme. Local extensions used by Jinja are not
    available yet.
-   Remove theme entry points to make late configuration consistent. The
    themes are available when ``"pallets_sphinx_themes"`` is added to
    ``extensions``.
-   Only run event callbacks added by theme when the theme is actually
    in use. This allows the package to be installed without interfering
    with other themes.
-   Support ``html_context["versions"]`` in the format injected by
    Read the Docs.
-   Set ``html_context["readthedocs_docsearch"]`` to opt in to replacing
    Sphinx's built-in search with Read the Docs' new implementation.
-   Make version handling more robust for various configurations.
-   Autodoc skips docstrings that contain the line ``:internal:``.
-   Autodoc removes lines that start with ``:copyright:`` or
    ``:license:`` from module docstrings.
-   Add ``singlehtml_sidebars`` config for Sphinx < 1.8.
-   Add ``hide-header`` CSS class to hide the page header with
    ``.. rst-class:: hide-header``. The header is still useable by
    assistive technology. This is useful for replacing the header with a
    large logo image.
-   Disable the sidebar logo on the index page with
    ``html_theme_options["index_sidebar_logo"] = False``.

.. _#4: https://github.com/pallets/pallets-sphinx-themes/pull/4


Version 1.0.1
=============

Released 2018-04-29

-   Work around an issues with search when using the ``dirhtml``
    builder. (`#3`_)

.. _#3: https://github.com/pallets/pallets-sphinx-themes/pull/3


Version 1.0.0
=============

Released 2018-04-18

-   Major rewrite of CSS and HTML templates to clean up and reduce
    complexity. Widen columns, improve responsive breakpoints. Currently
    all themes are available, but only ``pocoo`` and ``flask`` themes
    are modernized.
-   Parse ``html_context["versions"]``. These will be rendered in the
    ``versions.html`` sidebar. When viewing an old version, or the
    development version, a warning is displayed at the top of each page.
-   Add a ``ProjectLink`` named tuple. A list of these in
    ``html_context["project_links"]`` will be rendered in the
    ``project.html`` sidebar.
-   Add a ``get_version`` function to ensure a project is installed and
    get its version information.
-   Use ``html_context["canonical_url"]`` as a base URL to build a
    canonical URL link on each page.
-   Add Sphinx entry points for themes.
-   Rename from "pocoo-sphinx-themes". See commit `f675bfc`_ for the old
    themes from the docbuilder.

.. _f675bfc: https://github.com/pallets/pallets-sphinx-themes/tree/f675bfc
