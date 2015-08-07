import os

__version__ = '0.1.2'

def get_html_theme_path():
    return os.path.abspath(os.path.dirname(__file__))
