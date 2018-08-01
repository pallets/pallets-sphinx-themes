from functools import wraps


def set_is_pallets_theme(app):
    if app.config.is_pallets_theme is not None:
        return

    theme = getattr(app.builder, "theme", None)

    while theme is not None:
        if theme.name == "pocoo":
            app.config.is_pallets_theme = True
            break

        theme = theme.base


def only_pallets_theme(default=None):
    def decorator(f):
        @wraps(f)
        def wrapped(app, *args, **kwargs):
            if not app.config.is_pallets_theme:
                return default

            return f(app, *args, **kwargs)

        return wrapped

    return decorator
