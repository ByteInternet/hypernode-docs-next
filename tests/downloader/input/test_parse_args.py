from pathlib import Path

from hypernode.downloader.input import parse_args
from tests.testcase import HypernodeTestCase


class TestParseArgs(HypernodeTestCase):
    def setUp(self) -> None:
        self.default_args = ["https://example.com/support-doc"]

    def test_default_parse_args(self) -> None:
        url, output_dir, force, verbose = parse_args(self.default_args)
        self.assertEqual(url, "https://example.com/support-doc")
        self.assertEqual(output_dir, None)
        self.assertEqual(force, False)
        self.assertEqual(verbose, False)

    def test_sets_ouput_dir(self) -> None:
        _, output_dir, _, _ = parse_args(
            self.default_args + ["--output-dir", "/path/to/dir"]
        )
        self.assertEqual(output_dir, Path("/path/to/dir"))

    def test_sets_force(self) -> None:
        _, _, force, _ = parse_args(self.default_args + ["--force"])
        self.assertEqual(force, True)

    def test_sets_verbose(self) -> None:
        _, _, _, verbose = parse_args(self.default_args + ["--verbose"])
        self.assertEqual(verbose, True)
