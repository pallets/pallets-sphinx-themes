import inspect
import os
import sys
import textwrap
from collections import namedtuple

import pkg_resources

from pallets_sphinx_themes.versions import DocVersion, VersionManager

__version__ = '1.0.1'


def setup(app):
    base = os.path.dirname(__file__)

    for name in (
        'pocoo',
        'flask',
        'jinja',
        'werkzeug',
        'click',
        'babel',
        'platter',
        'flask-sqlalchemy',
    ):
        app.add_html_theme(name, os.path.join(base, name))

    app.connect('html-page-context', canonical_url)
    VersionManager(app)

    return {
        'version': __version__,
        'parallel_read_safe': True,
    }


def canonical_url(app, pagename, templatename, context, doctree):
    base = context.get('canonical_url')

    if not base:
        return

    target = app.builder.get_target_uri(pagename)
    context['canonical_url'] = base + target


def get_version(name):
    try:
        release = pkg_resources.get_distribution(name).version
    except ImportError:
        print(textwrap.fill(inspect.cleandoc('''
            '{name}' must be installed to build the documentation. Install from
            source using `pip install -e .` in a virtualenv.
        '''.format(name=name))))
        sys.exit(1)

    if 'dev' in release:
        release = release.split('dev', 1)[0] + 'dev'

    version = '.'.join(release.split('.', 2)[:2])
    return release, version


ProjectLink = namedtuple('ProjectLink', ('title', 'url'))
