# Setting up the theme

## Setting up the sidebar

We can start by adding some project information, mainly a logo and a HTML title for our Documentation.

``` python
html_logo = "_static/your-logo.png"
# Replace your-logo with the nam of the file you wish to be logo.
html_title = f"{project} Documentation ({version})"
```

This creates a logo at the sidebar, as well as setting up a title for your documentation. Additionally, you may wish to start customizing the sidebar though, and we can do this by adding project links to the sidebar.

``` python
# Replace the values accordingly.
html_context = {
    "project_links": [
        ProjectLink("Donate", "https://palletsprojects.com/donate"),
        ProjectLink("PyPI Releases", "https://pypi.org/project/Pallets-Sphinx-Themes/"),
        ProjectLink("Source Code", "https://github.com/pallets/pallets-sphinx-themes/"),
        ProjectLink("Issue Tracker", "https://github.com/pallets/pallets-sphinx-themes/issues/"),
        ProjectLink("Chat", "https://discord.gg/pallets"),
    ]
}
```

## Customizing the sidebar

You can choose which templates to use in the sidebar. You can also choose what sidebar templates to show up based on whether you are viewing the index, or a page.

Below is an example, where the the index has `project.html`, which is the template for displaying project links, while the "**" (Which indicates the rest of the pages) does not have the project template, but rather the `relations.html` templates, which shows the previous and next pages.

```
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html"],
}
```

```{note}
Please leave `ethicalads.html` as a template, it is what allows Read The Docs to display advertisements, which is their main source of funding.
```

Further customization can be read in [customizing](customizing.md), but by now you should have a good idea of the themes, and can start documenting.
