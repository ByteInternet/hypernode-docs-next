from unittest.mock import mock_open

from hypernode.downloader.main import get_url_from_document
from tests.testcase import HypernodeTestCase


class TestGetUrlFromDocument(HypernodeTestCase):
    def setUp(self) -> None:
        self.mock_file = self.set_up_patch(
            "builtins.open",
            mock_open(read_data="<!-- source: http://example.com/banaan/test-page -->"),
        )
        self.file_path = "path/to/file"

    def test_it_fetches_the_url_from_document(self) -> None:
        result = get_url_from_document(self.file_path)
        self.mock_file.assert_called_once_with(
            self.file_path, encoding="utf-8", mode="r"
        )
        self.assertEqual("http://example.com/banaan/test-page", result)

    def test_it_returns_none_if_no_url_found(self) -> None:
        self.mock_file.return_value.readline.return_value = "Something we didn't expect"
        result = get_url_from_document(self.file_path)
        self.mock_file.assert_called_once_with(
            self.file_path, encoding="utf-8", mode="r"
        )
        self.assertEqual(None, result)
