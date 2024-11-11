# Setting up the theme

We can start by adding some project information, mainly a logo and a HTML title for our Documentation.

``` python
html_logo = "_static/your-logo.png"
# Sets the logo. Replace your-logo with the actual name of the file you want to be the logo.
html_title = f"{project} Documentation ({version})"
# Sets the title of the documentation. Change it to whatever you want.
```

You might want to start customizing the sidebar though, and we can do this by adding project links to the sidebar.

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