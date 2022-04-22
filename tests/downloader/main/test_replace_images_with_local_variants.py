from pathlib import Path
from textwrap import dedent
from unittest.mock import mock_open

from hypernode.downloader.main import replace_images_with_local_variants
from tests.testcase import HypernodeTestCase


class TestReplaceImagesWithLocalVariants(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.downloader.main."
        self.isfile = self.set_up_patch(module + "os.path.isfile", return_value=False)
        self.isdir = self.set_up_patch(module + "os.path.isdir", return_value=True)
        self.mkdir = self.set_up_patch(module + "os.mkdir")
        self.get = self.set_up_patch(module + "requests.get")
        self.open = self.set_up_patch(module + "open", mock_open())
        self.file = self.open.return_value
        self.output_dir = Path("/path/to/output/dir")
        self.content = dedent(
            """
            ![](https://banaan.com/banaan.jpg)
            """
        )

    def test_it_downloads_images(self) -> None:
        self.get.return_value.content = "image_contents"

        result = replace_images_with_local_variants(self.content, self.output_dir)

        self.isfile.assert_called_once_with(self.output_dir.joinpath("_res/banaan.jpg"))
        self.isdir.assert_called_once_with(self.output_dir.joinpath("_res"))
        self.mkdir.assert_not_called()
        self.get.assert_called_once_with("https://banaan.com/banaan.jpg")
        self.open.assert_called_once_with(
            self.output_dir.joinpath("_res/banaan.jpg"), mode="wb"
        )
        self.file.write.assert_called_once_with("image_contents")

        self.assertEqual(
            result,
            dedent(
                """
                ![](_res/banaan.jpg)
                """
            ),
        )

    def test_it_skips_if_image_exists(self) -> None:
        self.isfile.return_value = True

        result = replace_images_with_local_variants(self.content, self.output_dir)

        self.isfile.assert_called_once_with(self.output_dir.joinpath("_res/banaan.jpg"))
        self.isdir.assert_not_called()
        self.mkdir.assert_not_called()
        self.get.assert_not_called()
        self.open.assert_not_called()
        self.file.write.assert_not_called()

        self.assertEqual(
            result,
            dedent(
                """
                ![](_res/banaan.jpg)
                """
            ),
        )

    def test_it_creates_res_directory_if_it_does_not_exist(self) -> None:
        self.isdir.return_value = False

        replace_images_with_local_variants(self.content, self.output_dir)

        self.mkdir.assert_called_once_with(self.output_dir.joinpath("_res"))
