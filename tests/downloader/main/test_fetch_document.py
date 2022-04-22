from hypernode.downloader.main import fetch_document
from tests.testcase import HypernodeTestCase


class TestFetchDocument(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.downloader.main."
        self.url = "https://example.com/support-doc"
        self.get = self.set_up_patch(module + "requests.get")
        self.response = self.get.return_value
        self.response.content = "<strong>Hello, World</strong>"

    def test_fetch_document_fetches_and_returns_beautifulsoup(self) -> None:
        result = fetch_document(self.url)

        self.get.assert_called_once_with(self.url)
        self.assertEqual(result.text, "Hello, World")
