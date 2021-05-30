import logging

from selenium.webdriver.common.by import By

from constants import start_page
from pages.base import BasePage, wait_until_ok


class StartPage(BasePage):
    """Class stores actions and verification related to start page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def fill_sign_in_fields(self, email, password):
        """Fill specified fields using passed values"""
        # Click on the user page
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.USER_ICON_XPATH)

        # Fill email and password fields
        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SIGN_IN_LOGIN_FIELD_XPATH, data=email)
        self.logger.debug("Set login value: '%s'", email)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SIGN_IN_PASSWORD_FIELD_XPATH, data=password)
        self.logger.debug("Set password value: '%s'", password)

        # Click on Sign In
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SING_IN_BUTTON_XPATH)
        self.logger.debug("Clicked on sign in")

    def verify_invalid_credentials(self):
        """Verify error message"""
        error_message = self.wait_until_find(locator_type=By.XPATH, locator=start_page.SIGN_IN_LOGIN_ERROR_XPATH).text
        assert error_message == start_page.SIGN_IN_LOGIN_ERROR_TEXT, f"Actual message:{error_message}"
        self.logger.debug("Error message was verified")

    def fill_sign_up_fields(self, firstname, lastname, email, password, password_confirm):
        """Fill specified fields using passed values"""
        # Click on the user page
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.USER_ICON_XPATH)

        # Click on the registration button

        # There may be PROBLEMS with the locator
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.REGISTRATION_BUTTON_XPATH)

        # Fill firstname, lastname, email, password and password confirmation fields
        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SING_UP_FIRSTNAME_XPATH, data=firstname)
        self.logger.debug("Set login value: '%s'", firstname)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SING_UP_LASTNAME_XPATH, data=lastname)
        self.logger.debug("Set login value: '%s'", lastname)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SING_UP_EMAIL_XPATH, data=email)
        self.logger.debug("Set login value: '%s'", email)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SING_UP_PASSWORD_XPATH, data=password)
        self.logger.debug("Set login value: '%s'", password)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.SING_UP_PASSWORD_CONFIRMATION_XPATH, data=password_confirm)
        self.logger.debug("Set login value: '%s'", password_confirm)

        # Click on sign up button
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SIGN_UP_BUTTON_XPATH)
        self.logger.debug("Clicked on sign up")

    @wait_until_ok(timeout=20)
    def verify_sign_up(self, firstname, lastname):
        """Verify that sign up successful"""
        # Click on "My kabinet"
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.MY_KABINET_XPATH)

        # Click on "Control panel"
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.CONTROL_PANEL_XPATH)

        # Verify hello message
        hello_message = self.wait_until_find(locator_type=By.XPATH, locator=start_page.HELLO_MESSAGE_XPATH).text
        assert hello_message == start_page.HELLO_MESSAGE_TEXT.format(
            firstname=firstname, lastname=lastname), f"Actual message: {hello_message}, " \
                                                     f"Expected: {start_page.HELLO_MESSAGE_TEXT}"
        self.logger.debug("Hello message was verified")

    def sign_out(self):
        """Click on Sign Out button"""
        # Click on "My kabinet"
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.MY_KABINET_XPATH)
        #  Click on Sign Out button
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SIGN_OUT_BUTTON_XPATH)

    def open_feedback(self):
        """Open feedback"""
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.FEEDBACK_BUTTON_XPATH)

    def fill_feedback_fields(self, name, email, phone, comment):
        """Fill all feedback fields"""
        # Fill feedback fields
        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.FEEDBACK_NAME_XPATH, data=name)
        self.logger.debug("Set name value: '%s'", name)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.FEEDBACK_EMAIL_XPATH, data=email)
        self.logger.debug("Set email value: '%s'", email)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.FEEDBACK_PHONE_XPATH, data=phone)
        self.logger.debug("Set email value: '%s'", phone)

        self.wait_until_send_keys(locator_type=By.XPATH, locator=start_page.FEEDBACK_COMMENT_XPATH, data=comment)
        self.logger.debug("Set email value: '%s'", comment)

        # Send feedback
        self.wait_until_click(locator_type=By.XPATH, locator=start_page.SEND_FEEDBACK_BUTTON_XPATH)

    @wait_until_ok(timeout=15)
    def verify_feedback_message(self):
        """Verify that feedback message was sent"""
        feedback_message = self.wait_until_find(locator_type=By.XPATH, locator=start_page.FEEDBACK_MESSAGE_XPATH).text
        assert feedback_message == start_page.FEEDBACK_MESSAGE_TEXT, f"Actual message: {feedback_message}"
        self.logger.debug("Feedback message was verified")








