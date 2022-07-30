from re import search, MULTILINE

project = 'SPWorlds API'
copyright = '2022, SPWorlds'
author = 'deesiigneer'

# The full version, including alpha/beta/rc tags.
release = '1.0'

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
html_theme = "furo"
html_title = "SPWorlds API"
language = "ru"
html_static_path = ["_static"]
html_css_files = ["pied-piper-admonition.css"]
html_logo = "./images/logo.png"
html_favicon = "./images/logo.ico"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sp-worlds/api-docs",
            "icon": "fab fa-brands fa-github",
            "type": "fontawesome"
        }
    ],
    "announcement": "API может в любой момент измениться и это ваша задача следить за его изменениями, и подстраивать под них свои приложения."
}
