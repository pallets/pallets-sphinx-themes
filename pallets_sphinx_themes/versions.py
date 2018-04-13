import io
import json
import os

from jinja2 import contextfunction


class VersionManager(object):
    current = None
    stable = None

    def __init__(self, app):
        config_versions = app.config.html_context.get('versions')
        app.config.html_context['versions'] = self
        self.versions = versions = []

        if app.config.release.endswith('dev'):
            current_slug = 'dev'
        else:
            current_slug = app.config.version

        if not config_versions:
            return

        if isinstance(config_versions, str):
            if os.path.isfile(config_versions):
                with io.open(config_versions, 'rt', encoding='utf8') as f:
                    config_versions = json.load(f)
            else:
                config_versions = json.loads(config_versions)

        for version in config_versions:
            if isinstance(version, dict):
                version = DocVersion(**version)

            versions.append(version)

            if self.current is None and version.slug == current_slug:
                self.current = version

            if self.stable is None and version.note == 'stable':
                self.stable = version

    @contextfunction
    def banner(self, context):
        current = self.current
        stable = self.stable

        if current is None or stable is None:
            return

        if current.slug == 'dev':
            return (
                'This is the development version. The latest stable'
                ' version is <a href="{href}">{stable}</a>.'
            ).format(
                stable=stable.title,
                href=stable.href(context)
            )

        elif current.note != 'stable':
            return (
                'This is an old version. The latest stable version is'
                ' <a href="{href}">{stable}</a>.'
            ).format(
                stable=stable.title,
                href=stable.href(context)
            )

    def __iter__(self):
        return iter(self.versions)

    def __getitem__(self, item):
        return self.versions[item]

    def __len__(self):
        return len(self.versions)

    def __bool__(self):
        return bool(self.versions)

    __nonzero__ = __bool__


class DocVersion(object):
    def __init__(self, slug, title, note=None, **kwargs):
        self.slug = slug
        self.title = title
        self.note = note
        self.kwargs = kwargs

    @contextfunction
    def href(self, context):
        if self == context['versions'].current:
            return '.'

        pathto = context['pathto']
        master_doc = context['master_doc']
        pagename = context['pagename']

        builder = pathto.__closure__[0].cell_contents
        master = pathto(master_doc).rstrip('#/') or '.'
        path = builder.get_target_uri(pagename)
        return '/'.join((master, '..', self.slug, path))

    def __eq__(self, other):
        return self.slug == other.slug
