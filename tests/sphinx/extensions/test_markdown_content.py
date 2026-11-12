from hypernode.sphinx.extensions.markdown_content import _resolve_target, convert
from tests.testcase import HypernodeTestCase

IMAGES = {
    "about-hypernode/billing/_res/cancel.png": "https://docs.hypernode.com/_images/cancel.png",
}

TITLES = {
    "hypernode-platform/ftp/how-to-configure-ftp-sftp-on-hypernode": "How to Configure FTP/SFTP on Hypernode",
    "index": "Welcome to Hypernode Docs",
}

LINKS = {
    "hypernode-platform/ftp/how-to-configure-ftp-sftp-on-hypernode": "https://docs.hypernode.com/hypernode-platform/ftp/how-to-configure-ftp-sftp-on-hypernode.html",
    "index": "https://docs.hypernode.com/",
}


class TestConvert(HypernodeTestCase):
    def test_strips_frontmatter(self):
        source = "---\ntitle: foo\n---\n\n# Hello\n\nBody text."

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertNotIn("title: foo", result)
        self.assertIn("# Hello", result)

    def test_strips_source_comment(self):
        source = "<!-- source: https://example.com/page/ -->\n\n# Hello"

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertNotIn("source:", result)
        self.assertIn("# Hello", result)

    def test_drops_toctree_directive(self):
        source = "# PHP\n\n```{toctree}\n---\ncaption: x\n---\nphp/*\n```\n\nBody"

        result = convert(source, "php", IMAGES, TITLES, LINKS)

        self.assertNotIn("toctree", result)
        self.assertIn("# PHP", result)
        self.assertIn("Body", result)

    def test_converts_note_directive_to_blockquote(self):
        source = "Intro\n\n```{note}\nSome note text.\n```\n\nOutro"

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertIn("**Note:**", result)
        self.assertIn("> Some note text.", result)
        self.assertNotIn("```{note}", result)

    def test_converts_tip_directive_with_custom_label(self):
        source = "```{tip}\nHandy tip.\n```"

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertIn("**Tip:**", result)

    def test_converts_unknown_directive_with_title_argument(self):
        source = "```{admonition} Watch Out\nBody text.\n```"

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertIn("**Watch Out:**", result)
        self.assertIn("> Body text.", result)

    def test_converts_nested_directive_with_inner_code_fence(self):
        source = "````{note}\nText with code:\n```yaml\nkey: value\n```\n````"

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertIn("**Note:**", result)
        self.assertIn("```yaml", result)
        self.assertIn("key: value", result)
        self.assertNotIn("````", result)

    def test_keeps_fenced_code_block_verbatim(self):
        source = 'Before\n\n```bash\necho "[link](relative.md)"\n```\n\nAfter'

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertIn('echo "[link](relative.md)"', result)
        self.assertIn("```bash", result)

    def test_rewrites_internal_md_link_to_absolute_url(self):
        source = "See [the FTP article](../../hypernode-platform/ftp/how-to-configure-ftp-sftp-on-hypernode.md)."

        result = convert(
            source, "about-hypernode/billing/how-to-cancel", IMAGES, TITLES, LINKS
        )

        self.assertIn(
            "]({})".format(
                "https://docs.hypernode.com/hypernode-platform/ftp/how-to-configure-ftp-sftp-on-hypernode.html"
            ),
            result,
        )
        self.assertNotIn(".md)", result)

    def test_rewrites_index_link_to_site_root(self):
        source = "Check [our docs](../../index.md)."

        result = convert(
            source, "getting-started/how-to-order/some-article", IMAGES, TITLES, LINKS
        )

        self.assertIn("](https://docs.hypernode.com/)", result)

    def test_keeps_external_links(self):
        source = "[Hypernode](https://www.hypernode.com/)"

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertEqual("[Hypernode](https://www.hypernode.com/)", result.strip())

    def test_rewrites_image_to_published_url(self):
        source = "![Cancellation date](_res/cancel.png)"

        result = convert(
            source, "about-hypernode/billing/how-to-cancel", IMAGES, TITLES, LINKS
        )

        self.assertEqual(
            "![Cancellation date](https://docs.hypernode.com/_images/cancel.png)",
            result.strip(),
        )

    def test_does_not_touch_code_blocks_containing_directive_like_text(self):
        source = "Example:\n\n```text\n```{note}\n```\n\nDone"

        result = convert(source, "foo", IMAGES, TITLES, LINKS)

        self.assertIn("```{note}", result)


class TestResolveTarget(HypernodeTestCase):
    def test_resolves_relative_path_against_docname_directory(self):
        result = _resolve_target(
            "about-hypernode/billing/how-to-cancel",
            "../../hypernode-platform/ftp/article.md",
        )

        self.assertEqual("hypernode-platform/ftp/article.md", result)

    def test_resolves_sibling_path(self):
        result = _resolve_target("hypernode-platform/php/article", "other-article.md")

        self.assertEqual("hypernode-platform/php/other-article.md", result)

    def test_resolves_absolute_path(self):
        result = _resolve_target("any/page", "/hypernode-platform/ssh/article.md")

        self.assertEqual("hypernode-platform/ssh/article.md", result)

    def test_resolves_path_in_root(self):
        result = _resolve_target("hypernode-platform/php/article", "index.md")

        self.assertEqual("hypernode-platform/php/index.md", result)
