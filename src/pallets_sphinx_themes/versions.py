import json
import os
from collections import namedtuple

from jinja2 import pass_context
from packaging import version as pv

from .theme_check import only_pallets_theme


@only_pallets_theme()
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
            with open(config_versions, encoding="utf8") as f:
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
    dev = "dev" in app.config.release
    seen_latest = False

    for i, version in enumerate(versions):
        if version.slug == "dev":
            versions[i] = version._replace(dev=True, current=dev)

        if version.slug == slug:
            versions[i] = version._replace(current=True)

        if not seen_latest and version.version is not None:
            seen_latest = True
            versions[i] = version._replace(latest=True)

    return versions


def readthedocs_versions(app):
    config_versions = app.config.html_context["versions"]
    current_slug = app.config.html_context["current_version"]
    number_versions = []
    name_versions = []

    for slug, _ in config_versions:
        dev = slug in {"main", "master", "default", "latest"}
        version = _parse_version(slug)

        if version is not None:
            name = slug
            append_to = number_versions
        else:
            name = "Development" if dev else slug.title()
            append_to = name_versions

        append_to.append(
            DocVersion(name=name, slug=slug, dev=dev, current=slug == current_slug)
        )

    # put the newest numbered version first
    number_versions.sort(key=lambda x: x.version, reverse=True)
    # put non-dev named versions first
    name_versions.sort(key=lambda x: x.dev, reverse=True)
    versions = number_versions + name_versions

    # if there are non-dev versions, mark the newest one as the latest
    if versions and not versions[0].dev:
        versions[0] = versions[0]._replace(latest=True)

    return versions


def _parse_version(value: str, placeholder: str = "x"):
    if value.endswith(f".{placeholder}"):
        value = value[: -(len(placeholder) + 1)]

    try:
        return pv.Version(value)
    except pv.InvalidVersion:
        return None


class DocVersion(
    namedtuple("DocVersion", ("name", "slug", "version", "latest", "dev", "current"))
):
    __slots__ = ()

    def __new__(cls, name, slug=None, latest=False, dev=False, current=False):
        slug = slug or name
        version = _parse_version(slug)

        if version is not None:
            name = "Version " + name

        return super().__new__(cls, name, slug, version, latest, dev, current)

    @pass_context
    def href(self, context):
        pathto = context["pathto"]
        master_doc = context["master_doc"]
        pagename = context["pagename"]

        builder = pathto.__closure__[0].cell_contents
        master = pathto(master_doc).rstrip("#/") or "."
        path = builder.get_target_uri(pagename)
        return "/".join((master, "..", self.slug, path))

    @pass_context
    def banner(self, context):
        if self.latest:
            return

        latest = context["latest_version"]

        # Don't show a banner if the latest version couldn't be determined, or if this
        # is the "stable" version.
        if latest is None or self.name == "stable":
            return

        if self.dev:
            return (
                "This is the development version. The latest stable"
                f' version is <a href="{latest.href(context)}">{latest.name}</a>.'
            )

        return (
            "This is an old version. The latest stable version is"
            f' <a href="{latest.href(context)}">{latest.name}</a>.'
        )
