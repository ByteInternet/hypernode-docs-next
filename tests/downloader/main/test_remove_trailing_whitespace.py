from hypernode.downloader.main import remove_trailing_whitespace
from tests.testcase import HypernodeTestCase


class TestRemoveTrailingWhitespace(HypernodeTestCase):
    def setUp(self) -> None:
        self.content = "First Line    \nSecond Line"

    def test_it_removes_trailing_whitespace(self) -> None:
        result = remove_trailing_whitespace(self.content)

        self.assertEqual(result, "First Line\nSecond Line")
