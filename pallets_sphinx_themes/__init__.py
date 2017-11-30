import os

__version__ = '1.0.0'


def setup(app):
    base = os.path.dirname(__file__)

    for name in (
        'pocoo', 'flask', 'jinja', 'werkzeug', 'click'
    ):
        app.add_html_theme(name, os.path.join(base, name))

    return {
        'version': __version__,
        'parallel_read_safe': True,
    }
