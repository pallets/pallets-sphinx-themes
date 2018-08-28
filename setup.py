import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="Pallets-Sphinx-Themes",
    version="1.1.0",
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
    install_requires=["sphinx"],
    entry_points={
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
