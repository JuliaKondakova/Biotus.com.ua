from conftest import BaseTest
from pages.search import SearchPage


class TestSearchPage(BaseTest):

    def test_search(self, start_page):
        """
        - Click on Search
        - Enter search text
        - Verify search text
        """

        # Click on Search and enter text
        search_page = SearchPage(start_page.driver)
        search_page.open_search_and_enter_text()

        # Verify search text
        search_page.verify_search()

