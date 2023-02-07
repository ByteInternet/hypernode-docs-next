from unittest.mock import Mock

from sphinx.application import Sphinx
from sphinx.config import Config

from hypernode.sphinx.extensions.meta_robots import page_context_handler, setup_sphinx
from tests.testcase import HypernodeTestCase


class TestPageContextHandler(HypernodeTestCase):
    def setUp(self) -> None:
        self.app = Mock(spec=Sphinx)
        self.app.config = Config({})
        self.app.config["html_meta_robots"] = "noindex, nofollow"
        self.context: dict = {}

    def test_page_context_handler_sets_noindex_nofollow(self):
        page_context_handler(self.app, "", "", self.context, None)

        self.assertIn("meta_robots", self.context)
        self.assertEqual("noindex, nofollow", self.context["meta_robots"])

    def test_page_context_handler_sets_index_follow(self):
        self.app.config.html_meta_robots = "index, follow"

        page_context_handler(self.app, "", "", self.context, None)

        self.assertIn("meta_robots", self.context)
        self.assertEqual("index, follow", self.context["meta_robots"])


class TestSetupSphinx(HypernodeTestCase):
    def setUp(self) -> None:
        self.app = Mock(spec=Sphinx)

    def test_setup_adds_config_value(self):
        setup_sphinx(self.app)

        self.app.add_config_value.assert_called_once_with(
            "html_meta_robots", "noindex, nofollow", "html"
        )
        self.app.connect.assert_called_once_with(
            "html-page-context", page_context_handler
        )
