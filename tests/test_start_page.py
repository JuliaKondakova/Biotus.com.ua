"""Store Start page tests"""
import random

from conftest import BaseTest


class TestStartPage(BaseTest):
    """Start page tests"""

    def test_invalid_credentials(self, start_page):
        """
        - Open start page
        - Click on the user page
        - Clear password and login fields
        - Set invalid values for email and password
        - Click on Sign In
        - Verify error message
        """

        # Click on the user page, clear login and password fields and set invalid values
        start_page.fill_sign_in_fields(email="1111", password="1111")

        # Verify error message
        start_page.verify_invalid_credentials()

    def test_registration(self, start_page):
        """
        - Open start page
        - Click on the user page
        - Click on the registration button
        - Fill firstname, lastname, birthday, email, password and confirmation password fields
        - Click on sign up button
        - Verify that sign up successful
        """

        #  Fill firstname, lastname, birthday, email, password and confirmation password fields and click on sign up button
        start_page.fill_sign_up_fields(firstname="John", lastname="Doe", email=f"email{self.variety}@mail.com",
                                       password="UsrPwd1234", password_confirm="UsrPwd1234")

        # Verify that sign up successful
        start_page.verify_sign_up(firstname="John", lastname="Doe")

    def test_send_feedback(self, start_page):
        """
        - Open feedback
        - Fill feedback fields
        - Send feedback
        - Verify that feedback message was sent
        """
        # Open feedback
        start_page.open_feedback()

        # Fill feedback fields and send feedback
        start_page.fill_feedback_fields(name="User", email=f"email{self.variety}@mail.com", phone=f"09{self.variety}",
                                        comment="This site is tested")

        # Verify that feedback message was sent
        start_page.verify_feedback_message()
