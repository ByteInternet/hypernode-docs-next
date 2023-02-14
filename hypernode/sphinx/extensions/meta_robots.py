from sphinx.application import Sphinx


def page_context_handler(app: Sphinx, pagename: str, templatename, context, doctree):
    context["meta_robots"] = app.config.html_meta_robots


def setup_sphinx(app: Sphinx):
    app.add_config_value("html_meta_robots", "noindex, nofollow", "html")
    app.connect("html-page-context", page_context_handler)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def setup(app: Sphinx):
    return setup_sphinx(app)
