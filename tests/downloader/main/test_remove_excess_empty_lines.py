from textwrap import dedent

from hypernode.downloader.main import remove_excess_empty_lines
from tests.testcase import HypernodeTestCase


class TestRemoveExcessEmptyLines(HypernodeTestCase):
    def setUp(self) -> None:
        self.content = dedent(
            """
            # Some heading


            # Other heading
            """
        )

    def test_it_removes_excess_empty_lines(self) -> None:
        expected = dedent(
            """
            # Some heading

            # Other heading
            """
        )

        result = remove_excess_empty_lines(self.content)

        self.assertEqual(result, expected)
