from pathlib import Path
from unittest.mock import ANY

from bs4 import BeautifulSoup

from hypernode.downloader.main import ConvertException, convert_document
from tests.testcase import HypernodeTestCase


class TestConvertDocument(HypernodeTestCase):
    def setUp(self) -> None:
        module = "hypernode.downloader.main."
        self.figure_out_output_dir = self.set_up_patch(module + "figure_out_output_dir")
        self.isdir = self.set_up_patch(module + "os.path.isdir", return_value=True)
        self.md = self.set_up_patch(module + "md", return_value="Article Content")
        self.remove_trailing_whitespace = self.set_up_patch(
            module + "remove_trailing_whitespace", return_value="Article Content"
        )
        self.remove_excess_empty_lines = self.set_up_patch(
            module + "remove_excess_empty_lines", return_value="Article Content"
        )
        self.remove_old_table_of_contents = self.set_up_patch(
            module + "remove_old_table_of_contents", return_value="Article Content"
        )
        self.replace_images_with_local_variants = self.set_up_patch(
            module + "replace_images_with_local_variants",
            return_value="Article Content",
        )
        self.html = """
        <html>
        <body>
        <section>
        <h2 class="hc-heading">Support Article</h2>
        <article id="article-body">Article Content</article>
        </section>
        </body>
        </html>
        """
        self.url = "https://example.com/support-doc"
        self.document = BeautifulSoup(self.html, "html.parser")
        self.output_dir = Path("/path/to/output/dir")

    def test_convert_document_converts_to_markdown(self) -> None:
        filepath, content = convert_document(
            self.document, self.url, output_dir=self.output_dir
        )

        self.isdir.assert_called_once_with(self.output_dir)
        self.md.assert_called_once_with(
            '<article id="article-body">Article Content</article>',
            code_language_callback=ANY,
            escape_asterisks=False,
            escape_underscores=False,
        )
        self.remove_trailing_whitespace.assert_called_once_with("Article Content")
        self.remove_excess_empty_lines.assert_called_once_with("Article Content")
        self.remove_old_table_of_contents.assert_called_once_with("Article Content")
        self.replace_images_with_local_variants.assert_called_once_with(
            "Article Content", self.output_dir
        )

        self.assertEqual(filepath, Path("/path/to/output/dir/support-article.md"))
        self.assertIn("Article Content", content)

    def test_convert_document_figures_out_root_dir_if_none(self) -> None:
        self.figure_out_output_dir.return_value = Path("/other/output/dir")

        filepath, _ = convert_document(self.document, self.url)

        self.figure_out_output_dir.assert_called_once_with(
            "support-article.md", self.document
        )

        self.assertEqual(filepath, Path("/other/output/dir/support-article.md"))

    def test_convert_document_throws_if_output_dir_does_not_exist(self) -> None:
        self.isdir.return_value = False

        with self.assertRaises(ConvertException):
            convert_document(self.document, self.url, output_dir=self.output_dir)
