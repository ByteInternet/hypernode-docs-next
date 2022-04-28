from hypernode.downloader.main import remove_old_table_of_contents
from tests.testcase import HypernodeTestCase


class TestRemoveOldTableOfContents(HypernodeTestCase):
    def test_it_removes_old_table_of_contents(self) -> None:
        source = """
        Some text has been written here.

        **TABLE OF CONTENTS**
        - [First Heading](#first-heading)
            + [First sub heading](#first-sub-heading)
        - [Second Heading](#second-heading)

        # First heading
        Some text here.

        # Second heading
        Some other text here.
        """
        expected = """
        Some text has been written here.


        # First heading
        Some text here.

        # Second heading
        Some other text here.
        """

        result = remove_old_table_of_contents(source)
        self.assertEqual(expected, result)
