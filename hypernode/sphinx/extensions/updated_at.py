import os.path
from datetime import datetime
from pathlib import Path

import git
from git.exc import GitCommandError
from sphinx import errors
from sphinx.application import Sphinx


class PageContextHandler:
    def __init__(self) -> None:
        self.git = git.Git(os.path.realpath(os.path.dirname(__file__) + "../../"))

    def execute(self, app: Sphinx, pagename: str, templatename, context, doctree):
        page_path = Path(app.confdir) / (pagename + ".md")
        if not os.path.exists(page_path):
            return

        try:
            log = self.git.log(
                "--pretty=format:%aI", "--reverse", page_path
            ).splitlines()
            if not log:
                return

            created = log[0]
            updated = log[-1]
        except GitCommandError as exc:
            raise errors.ExtensionError(
                "Failed to fetch git history for {}. Exception was: {}".format(
                    page_path, exc
                )
            )

        if created:
            context["created_at"] = datetime.fromisoformat(created).strftime(
                app.config.created_at_fmt
            )

        if updated:
            context["updated_at"] = datetime.fromisoformat(updated).strftime(
                app.config.updated_at_fmt
            )


def setup(app: Sphinx):
    page_context_handler = PageContextHandler()
    app.add_config_value("updated_at_fmt", "%b %d, %Y", "html")
    app.add_config_value("created_at_fmt", "%b %d, %Y", "html")
    app.connect("html-page-context", page_context_handler.execute)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
