# -*- coding: utf-8 -*-
import ast
import re
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('pocoo_sphinx_themes/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='pocoo_sphinx_themes',
    version=version,
    url='https://github.com/pocoo/pocoo-sphinx-themes/',
    license='BSD',
    author='The Pocoo Team',
    author_email='markus@unterwaditzer.net',
    description='Sphinx themes for Pocoo projects',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['sphinx'],
)
