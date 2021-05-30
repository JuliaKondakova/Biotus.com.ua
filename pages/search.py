import logging
from selenium.webdriver.common.by import By
from pages.base import BasePage, wait_until_ok
from constants import search
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):
    """Store search page tests"""

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def open_search_and_enter_text(self):
        """Enter search text"""
        # Click on Search
        self.wait_until_click(locator_type=By.XPATH, locator=search.SEARCH_FIELD_XPATH)

        # Enter search text
        self.wait_until_send_keys(locator_type=By.XPATH, locator=search.SEARCH_FIELD_XPATH,
                                  data=search.SEARCH_TEXT)
        self.driver.find_element(by=By.XPATH, value=search.SEARCH_FIELD_XPATH).send_keys(Keys.ENTER)

    def verify_search(self):
        """Verify search text"""
        search_text = self.wait_until_find(locator_type=By.XPATH, locator=search.SEARCH_RESULTS_XPATH).text
        assert search_text == search.SEARCH_RESULTS_TEXT, f"Actual;{search_text}"
        self.logger.debug("Search text was verified,'%s'", search_text)
