from pathlib import Path

from hypernode.downloader.main import find_output_dir_for_document
from tests.testcase import HypernodeTestCase


class TestFindOutputDirForDocument(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.downloader.main."
        self.walk = self.set_up_patch(
            module + "os.walk",
            return_value=[("/docs/subdir", [], ["banaan.md", "magento2.md"])],
        )

    def test_that_it_returns_none_by_default(self) -> None:
        result = find_output_dir_for_document("shopware6.md")

        self.assertEqual(None, result)
        self.walk.assert_called_once_with("docs")

    def test_that_it_returns_directory_on_filename_match(self) -> None:
        result = find_output_dir_for_document("banaan.md")

        self.assertEqual(Path("/docs/subdir"), result)
        self.walk.assert_called_once_with("docs")
