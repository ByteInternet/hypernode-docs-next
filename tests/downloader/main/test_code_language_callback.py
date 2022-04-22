from bs4 import BeautifulSoup

from hypernode.downloader.main import code_language_callback
from tests.testcase import HypernodeTestCase


class TestCodeLanguageCallback(HypernodeTestCase):
    def test_code_language_callback(self) -> None:
        document = BeautifulSoup(
            "<html><body><code class='language-bash'>...</code></body></html>",
            "html.parser",
        )
        result = code_language_callback(document.find("code"))
        self.assertEqual(result, "bash")

    def test_code_language_callback_returns_none_by_default(self) -> None:
        document = BeautifulSoup(
            "<html><body><p>...</p></body></html>",
            "html.parser",
        )
        result = code_language_callback(document.find("p"))
        self.assertEqual(result, None)
