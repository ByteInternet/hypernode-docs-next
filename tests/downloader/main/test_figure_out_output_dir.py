from pathlib import Path
from unittest.mock import Mock

from hypernode.downloader.main import figure_out_output_dir
from tests.testcase import HypernodeTestCase


class TestFigureOutOutputDir(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.downloader.main."
        self.find_output_dir_for_document = self.set_up_patch(
            module + "find_output_dir_for_document", return_value=None
        )
        self.makedirs = self.set_up_patch(module + "os.makedirs")
        self.isdir = self.set_up_patch(module + "os.path.isdir", return_value=False)
        self.getcwd = self.set_up_patch(
            module + "os.getcwd", return_value="/current/directory"
        )
        self.example_crumb = Mock()
        self.example_crumb.text.strip.return_value = "Some Category"
        self.sub_crumb = Mock()
        self.sub_crumb.text.strip.return_value = "Sub Category"
        self.unused_crumb = Mock()
        self.unused_crumb.text.strip.return_value = ""
        self.breadcrumb_items = [
            self.unused_crumb,
            self.unused_crumb,
            self.example_crumb,
            self.sub_crumb,
        ]
        self.breadcrumbs = Mock()
        self.breadcrumbs.findChildren.return_value = self.breadcrumb_items
        self.document = Mock(find=Mock(return_value=self.breadcrumbs))
        self.filename = "banaan.md"

    def test_that_it_returns_on_existing_output_dir_based_on_filename(self) -> None:
        self.find_output_dir_for_document.return_value = "docs/another-category"

        result = figure_out_output_dir(self.filename, self.document)

        self.find_output_dir_for_document.assert_called_once_with(self.filename)
        self.document.find.assert_not_called()

        self.assertEqual("docs/another-category", result)

    def test_that_it_generates_output_dir_based_on_breadcrumbs(self) -> None:
        expected_path = Path("docs/some-category/sub-category")
        result = figure_out_output_dir(self.filename, self.document)

        self.document.find.assert_called_once_with(class_="breadcrumb")
        self.breadcrumbs.findChildren.assert_called_once_with(recursive=False)
        self.isdir.assert_called_once_with(expected_path)
        self.makedirs.assert_called_once_with(expected_path, exist_ok=True)
        self.assertEqual(expected_path, result)

    def test_that_it_generates_output_dir_based_on_breadcrumbs_but_skips_makedirs(
        self,
    ) -> None:
        self.isdir.return_value = True
        expected_path = Path("docs/some-category/sub-category")
        result = figure_out_output_dir(self.filename, self.document)

        self.document.find.assert_called_once_with(class_="breadcrumb")
        self.breadcrumbs.findChildren.assert_called_once_with(recursive=False)
        self.isdir.assert_called_once_with(expected_path)
        self.makedirs.assert_not_called()
        self.assertEqual(expected_path, result)

    def test_that_it_returns_current_directory_as_fallback(self) -> None:
        self.breadcrumbs.findChildren.return_value = []

        result = figure_out_output_dir(self.filename, self.document)

        self.assertEqual(Path("/current/directory"), result)
