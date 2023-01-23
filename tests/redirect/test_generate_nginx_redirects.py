import os
from pathlib import Path
from unittest.mock import call

from hypernode.common.settings import DOCS_DIR
from hypernode.redirect.generate_nginx_redirects import (
    get_path_for_doc,
    get_redirects_from_doc,
    main,
)
from tests.testcase import HypernodeTestCase


class TestMain(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.redirect.generate_nginx_redirects."
        self.print = self.set_up_patch("builtins.print")
        self.get_all_docs = self.set_up_patch(
            module + "get_all_docs", return_value=[DOCS_DIR / "index.html"]
        )
        self.get_redirects_from_doc = self.set_up_patch(
            module + "get_redirects_from_doc",
            return_value=["/old-url/", "/en/another-url"],
        )

    def test_main_prints_rewrites(self):
        main()

        self.print.assert_has_calls(
            [
                call("rewrite ^/old-url/?$ / permanent;"),
                call("rewrite ^/en/another-url/?$ / permanent;"),
            ]
        )


class TestGetPathForDoc(HypernodeTestCase):
    def test_get_path_for_doc_resolves_relative_to_docs_dir(self):
        result = get_path_for_doc(DOCS_DIR / "some/doc.md")

        self.assertEqual("/some/doc.html", result)

    def test_get_path_for_doc_replaces_md_with_html(self):
        result = get_path_for_doc(DOCS_DIR / "something.md")

        self.assertEqual("/something.html", result)

    def test_get_path_for_doc_replaces_index_html_with_slash(self):
        result = get_path_for_doc(DOCS_DIR / "index.md")

        self.assertEqual("/", result)

    def test_get_path_for_doc_prepends_docs_base_url(self):
        try:
            os.environ["DOCS_BASE_URL"] = "https://www.example.com/"

            result = get_path_for_doc(DOCS_DIR / "some/doc.html")

            self.assertEqual("https://www.example.com/some/doc.html", result)
        finally:
            del os.environ["DOCS_BASE_URL"]


class TestGetRedirectsFromDoc(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.redirect.generate_nginx_redirects."
        self.read_doc = self.set_up_patch(
            module + "read_doc",
            return_value=({"redirect_from": ["/old/path/"]}, "", ""),
        )
        self.doc = Path("/some/path.md")

    def test_get_redirects_from_doc(self):
        result = get_redirects_from_doc(self.doc)

        self.assertEqual(["/old/path/"], result)
        self.read_doc.assert_called_once_with(self.doc)

    def test_get_redirects_from_doc_defaults_to_empty_list(self):
        self.read_doc.return_value = ({}, "", "")

        result = get_redirects_from_doc(self.doc)

        self.assertEqual([], result)
        self.read_doc.assert_called_once_with(self.doc)
