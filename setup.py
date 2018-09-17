import io
import os

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()


def get_sphinx_html_themes():
    """Get sphinx.html_themes entry_points without importing package."""
    themes = []
    package = "pallets_sphinx_themes"
    base = os.path.join(os.path.dirname(__file__), "src", package, "themes")

    for name in os.listdir(base):
        path = os.path.join(base, name)
        if os.path.isdir(path):
            themes.append("%s = %s" % (name, package))

    return themes


setup(
    name="Pallets-Sphinx-Themes",
    version="1.1.1",
    url="https://github.com/pallets/pallets-sphinx-themes/",
    license="BSD",
    author="The Pallets Team",
    author_email="contact@palletsprojects.com",
    description="Sphinx themes for Pallets and related projects.",
    long_description=readme,
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=["sphinx", "packaging"],
    entry_points={
        "sphinx.html_themes": get_sphinx_html_themes(),
        "pygments.styles": [
            "pocoo = pallets_sphinx_themes.themes.pocoo:PocooStyle",
            "jinja = pallets_sphinx_themes.themes.jinja:JinjaStyle",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Software Development :: Documentation",
    ],
)
