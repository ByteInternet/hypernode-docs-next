from unittest.mock import Mock

from hypernode.sphinx.extensions.markdown_pages import (
    get_llms_txt_url,
    get_markdown_page_url,
    page_context_handler,
    setup,
)
from tests.testcase import HypernodeTestCase


class TestGetMarkdownPageUrl(HypernodeTestCase):
    def test_returns_sibling_markdown_url_for_nested_page(self):
        self.assertEqual(
            "how-to-flush-the-php-opcache.html.md",
            get_markdown_page_url(
                "hypernode-platform/php/how-to-flush-the-php-opcache"
            ),
        )

    def test_returns_sibling_markdown_url_for_top_level_page(self):
        self.assertEqual("foo.html.md", get_markdown_page_url("foo"))


class TestGetLlmsTxtUrl(HypernodeTestCase):
    def test_returns_llms_txt_for_root_page(self):
        self.assertEqual("llms.txt", get_llms_txt_url("index"))

    def test_returns_llms_txt_for_top_level_page(self):
        self.assertEqual("llms.txt", get_llms_txt_url("foo"))

    def test_returns_relative_path_to_root_for_nested_page(self):
        self.assertEqual(
            "../../llms.txt",
            get_llms_txt_url("hypernode-platform/php/how-to-flush-the-php-opcache"),
        )


class TestPageContextHandler(HypernodeTestCase):
    def setUp(self) -> None:
        self.context: dict = {}

    def test_sets_markdown_and_llms_txt_urls(self):
        page_context_handler(Mock(), "hypernode-platform/php", "", self.context, None)

        self.assertEqual("php.html.md", self.context["markdown_page_url"])
        self.assertEqual("../llms.txt", self.context["llms_txt_url"])

    def test_sets_urls_for_root_page(self):
        page_context_handler(Mock(), "index", "", self.context, None)

        self.assertIsNone(self.context["markdown_page_url"])
        self.assertEqual("llms.txt", self.context["llms_txt_url"])

    def test_sets_no_markdown_url_for_404_page(self):
        page_context_handler(Mock(), "404", "", self.context, None)

        self.assertIsNone(self.context["markdown_page_url"])


class TestSetup(HypernodeTestCase):
    def test_setup_connects_page_context_handler(self):
        app = Mock()

        setup(app)

        app.connect.assert_called_once_with("html-page-context", page_context_handler)
