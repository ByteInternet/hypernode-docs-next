# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath("../"))


# -- Project information -----------------------------------------------------

project = "Docs"
copyright = "2023, Hypernode"
author = "Hypernode"

# The full version, including alpha/beta/rc tags
release = "dev"


# -- General configuration ---------------------------------------------------

source_suffix = {
    #'.rst': 'restructuredtext',
    ".md": "markdown",
    #'.txt': 'markdown',
}

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "notfound.extension",
    "hypernode.sphinx.extensions.updated_at",
    "sphinxcontrib.mermaid",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "titles_only": False,
    "analytics_id": "GTM-PDL826",
}
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "ByteInternet",  # Username
    "github_repo": "hypernode-docs-next",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/docs/",  # Path in the checkout to the docs root
}
html_show_sphinx = False
html_show_sourcelink = False

sitemap_url_scheme = "{link}"

if os.getenv("DOCS_BASE_URL"):
    html_baseurl = os.getenv("DOCS_BASE_URL")
    extensions.append("sphinx_sitemap")  # Only generate sitemap when we have a base url

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "https://fonts.googleapis.com/css?family=Montserrat:400,400i,500,600,700,800",
    "https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700",
    "https://static.hypernode.com/fontawesome/css/fontawesome-all.css",
    "https://static.hypernode.com/css/byteStyle.css",
    "css/main.css",
]
html_js_files = ["js/app.js"]

notfound_no_urls_prefix = True

myst_heading_anchors = 5
