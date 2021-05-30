import logging
from selenium.webdriver.common.by import By
from constants import menu_page, start_page
from pages.base import BasePage, wait_until_ok


class MenuPage(BasePage):
    """Store menu page tests"""

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @wait_until_ok(timeout=20)
    def open_menu_and_select_category(self):
        """Click on Menu, select category an subcategory"""
        # Click on Menu
        self.wait_until_click(locator_type=By.XPATH, locator=menu_page.MENU_BUTTON_XPATH)

        # Select category
        self.wait_until_click(locator_type=By.XPATH, locator=menu_page.CATEGORY_BUTTON_XPATH)

        # Select subcategory and click on it
        self.wait_until_click(locator_type=By.XPATH, locator=menu_page.SUBCATEGORY_BUTTON_XPATH)

    def select_item(self):
        """Select item"""
        self.wait_until_click(locator_type=By.XPATH, locator=menu_page.ITEM_XPATH)

    def add_to_cart(self):
        """Add item to cart"""
        self.wait_until_click(locator_type=By.XPATH, locator=menu_page.ADD_TO_CART_BUTTON_XPATH)

    def verify_added_item(self):
        """Verify added item"""
        added_item = self.wait_until_find(locator_type=By.XPATH, locator=menu_page.ADDED_TO_CART_XPATH).text
        assert added_item == menu_page.ADDED_TO_CART_TEXT, f"Actual: {added_item}"
        self.logger.debug("Item name was verified,'%s'", added_item)

    def add_to_wishlist(self):
        """Add item to wishlist"""
        self.wait_until_click(locator_type=By.XPATH, locator=menu_page.ADD_TO_WISHLIST_XPATH)

    @wait_until_ok(timeout=20)
    def open_wishlist(self):
        """Open wishlist"""
        # Click on my kabinet
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.MY_KABINET_XPATH)

        # Open wishlist
        self.wait_until_click(locator_type=By.XPATH, locator=menu_page.WISHLIST_BUTTON_XPATH)

    def verify_lovely_item(self):
        """Verify added item"""
        added_item = self.wait_until_find(locator_type=By.XPATH, locator=menu_page.ADDED_TO_WISHLIST_XPATH).text
        assert added_item == menu_page.ADDED_TO_CART_TEXT, f"Actual: {added_item}"
        self.logger.debug("Added item was verified,'%s'", added_item)