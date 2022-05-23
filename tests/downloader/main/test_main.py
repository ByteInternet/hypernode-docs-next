from os import EX_OK, EX_USAGE
from pathlib import Path
from unittest.mock import ANY, Mock, mock_open

from hypernode.downloader.main import ConvertException, main
from tests.testcase import HypernodeTestCase


class TestMain(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.downloader.main."
        self.url = "https://example.com/support-doc"
        self.document = Mock()
        self.filepath = Path("/path/to/file")
        self.contents = "# Some contents"
        self.configure_logging = self.set_up_patch(module + "configure_logging")
        self.fetch_document = self.set_up_patch(
            module + "fetch_document", return_value=self.document
        )
        self.get_url_from_document = self.set_up_patch(module + "get_url_from_document")
        self.convert_document = self.set_up_patch(module + "convert_document")
        self.convert_document.return_value = (self.filepath, self.contents)
        self.isfile = self.set_up_patch(module + "os.path.isfile", return_value=False)
        self.open = self.set_up_patch(module + "open", mock_open())
        self.file = self.open.return_value

    def test_main_fetches_converts_and_writes(self) -> None:
        return_code = main([self.url])

        self.configure_logging.assert_called_once_with(False, ANY)
        self.fetch_document.assert_called_once_with(self.url)
        self.convert_document.assert_called_once_with(
            self.document, self.url, output_dir=None
        )
        self.isfile.assert_called_once_with(self.filepath)
        self.open.assert_called_once_with(self.filepath, mode="w", encoding="utf-8")
        self.file.write.assert_called_once_with(self.contents)
        self.assertEqual(return_code, EX_OK)

    def test_main_configures_logging(self) -> None:
        main([self.url, "--verbose"])

        self.configure_logging.assert_called_once_with(True, ANY)

    def test_main_passes_input_output_dir(self) -> None:
        return_code = main([self.url, "--output-dir", "/other/output/dir"])

        self.convert_document.assert_called_once_with(
            self.document, self.url, output_dir=Path("/other/output/dir")
        )
        self.assertEqual(return_code, EX_OK)

    def test_main_does_not_write_file_without_force(self) -> None:
        self.isfile.return_value = True

        return_code = main([self.url])

        self.isfile.assert_called_once_with(self.filepath)
        self.open.assert_not_called()
        self.file.write.assert_not_called()

        self.assertEqual(return_code, EX_USAGE)

    def test_main_does_write_file_with_force(self) -> None:
        self.isfile.return_value = True

        return_code = main([self.url, "--force"])

        self.isfile.assert_called_once_with(self.filepath)
        self.open.assert_called_once_with(self.filepath, mode="w", encoding="utf-8")
        self.file.write.assert_called_once_with(self.contents)

        self.assertEqual(return_code, EX_OK)

    def test_main_fails_if_convert_exception(self) -> None:
        self.convert_document.side_effect = [ConvertException()]

        return_code = main([self.url])

        self.assertEqual(return_code, EX_USAGE)

    def test_main_converts_url_argument_if_path(self) -> None:
        self.get_url_from_document.return_value = self.url
        filepath = str(self.filepath)

        return_code = main([filepath])

        self.get_url_from_document.assert_called_once_with(filepath)
        self.fetch_document.assert_called_once_with(self.url)

        self.assertEqual(return_code, EX_OK)

    def test_main_fails_if_url_argument_is_path_but_cannot_resolve(self) -> None:
        self.get_url_from_document.return_value = None
        filepath = str(self.filepath)

        return_code = main([filepath])

        self.get_url_from_document.assert_called_once_with(filepath)
        self.fetch_document.assert_not_called()

        self.assertEqual(return_code, EX_USAGE)
