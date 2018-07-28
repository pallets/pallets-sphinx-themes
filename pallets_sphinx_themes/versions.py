from collections import namedtuple

import io
import json
import os
from jinja2 import contextfunction
from packaging import version as pv


def load_versions(app):
    if os.environ.get("READTHEDOCS"):
        versions = readthedocs_versions(app)
    else:
        versions = local_versions(app)

    context = app.config.html_context
    context["versions"] = versions
    context["current_version"] = next((v for v in versions if v.current), None)
    context["latest_version"] = next((v for v in versions if v.latest), None)


def local_versions(app):
    config_versions = app.config.html_context.get("versions")

    if isinstance(config_versions, str):
        if os.path.isfile(config_versions):
            with io.open(config_versions, "rt", encoding="utf8") as f:
                config_versions = json.load(f)
        else:
            config_versions = json.loads(config_versions)

    if not config_versions:
        return []

    versions = []

    for version in config_versions:
        if isinstance(version, dict):
            version = DocVersion(**version)

        versions.append(version)

    slug = app.config.version
    dev = 'dev' in app.config.release
    seen_latest = False

    for i, version in enumerate(versions):
        if version.slug == 'dev':
            versions[i] = version._replace(dev=True, current=dev)

        if version.slug == slug:
            versions[i] = version._replace(current=True)

        if not seen_latest and _is_version(version.slug):
            seen_latest = True
            versions[i] = version._replace(latest=True)

    return versions


def readthedocs_versions(app):
    config_versions = app.config.html_context["versions"]
    current_slug = app.config.html_context["current_version"]
    latest_slug = None

    for slug, _ in config_versions:
        if _is_version(slug):
            latest_slug = slug
            break

    return [
        DocVersion(
            name=slug,
            slug=slug,
            latest=slug == latest_slug,
            dev=slug in {"master", "default", "latest"},
            current=slug == current_slug,
        ) for slug, _ in config_versions
    ]


def _is_version(value):
    try:
        pv.Version(value)
        return True
    except pv.InvalidVersion:
        return False


class DocVersion(namedtuple("DocVersion", ("name", "slug", "latest", "dev", "current"))):
    __slots__ = ()

    def __new__(cls, name, slug=None, latest=False, dev=False, current=False):
        slug = slug or name
        return super(DocVersion, cls).__new__(cls, name, slug, latest, dev, current)

    @contextfunction
    def href(self, context):
        if self.current:
            return "."

        pathto = context["pathto"]
        master_doc = context["master_doc"]
        pagename = context["pagename"]

        builder = pathto.__closure__[0].cell_contents
        master = pathto(master_doc).rstrip("#/") or "."
        path = builder.get_target_uri(pagename)
        return "/".join((master, "..", self.slug, path))

    @contextfunction
    def banner(self, context):
        if self.latest:
            return

        latest = context["latest_version"]

        if self.dev:
            return (
                "This is the development version. The latest stable"
                ' version is <a href="{href}">{latest}</a>.'
            ).format(latest=latest.name, href=latest.href(context))

        return (
            "This is an old version. The latest stable version is"
            ' <a href="{href}">{latest}</a>.'
        ).format(latest=latest.name, href=latest.href(context))
