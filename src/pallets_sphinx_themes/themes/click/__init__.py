def setup(app):
    try:
        from . import domain
    except ImportError:
        return

    domain.setup(app)
