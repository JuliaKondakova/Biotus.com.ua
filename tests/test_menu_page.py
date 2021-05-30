"""Store Menu page tests"""
from conftest import BaseTest

from pages.menu_page import MenuPage


class TestMenuPage(BaseTest):
    """Menu page tests"""

    def test_add_to_cart(self, start_page):
        """
        - Go to Menu, select category and subcategory
        - Select item and add it to cart
        - Verify item name
        """

        # Click on Menu, select category and subcategory
        menu_page = MenuPage(start_page.driver)
        menu_page.open_menu_and_select_category()

        #  Select item
        menu_page.select_item()

        # Add item to cart
        menu_page.add_to_cart()

        # Verify added item
        menu_page.verify_added_item()

    # def test_add_to_wishlist(self, start_page, register_user):
    #     """
    #     - Login as user
    #     - Go to Menu, select category and subcategory
    #     - Select item and add it to wishlist
    #     - Verify that item was added
    #     """
    #     #  Login as user
    #     start_page.fill_sign_in_fields(register_user.email, register_user.password)
    #
    #     # Click on Menu, select category and subcategory
    #     menu_page = MenuPage(start_page.driver)
    #     menu_page.open_menu_and_select_category()
    #
    #     #  Select item
    #     menu_page.select_item()
    #
    #     # Add item to wishlist
    #     menu_page.add_to_wishlist()
    #
    #     #  Open wishlist
    #     menu_page.open_wishlist()
    #
    #     # Verify added item
    #     menu_page.verify_lovely_item()









