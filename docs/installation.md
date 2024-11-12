# Installation

## As a `pip` package

The themes need to be installed as a `pip` package. This can be done by running the command:

``` console
pip install pallets-sphinx-themes
```

You will need to enable to extension for the theme to work properly:

``` python
extensions = [
    "pallets_sphinx_themes",
    ...
]
```

Afterwards, enable the themes by setting these lines in your `conf.py` file:

``` python
html_theme = "flask"
```

As mentioned earlier, you can choose from one of 4 availabale themes. Edit `html_theme` to one of th 4 to choose your theme.

```{tip}
If you distribute your documentation via [Read The Docs](https://readthedocs.org/dashboard/), be sure to add this package to your `requirements.txt` file.
```

Now, go move onto [setting up the theme](setup.md).
