import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import time


def wait_until_ok(timeout, period=0.25):
    """Retry function with parameters"""

    def act_decorator(target_func):
        logger = logging.getLogger(__name__)

        def wrapper(*args, **kwargs):
            must_end = time.time() + timeout
            while True:
                try:
                    return target_func(*args, **kwargs)
                except (WebDriverException, AssertionError, TimeoutException) as error:
                    error_name = error if str(error) else error.__class__.__name__
                    logger.debug("Catch '%s'. Left %s seconds", error_name, (must_end - time.time()))
                    if time.time() >= must_end:
                        logger.warning("Waiting timed out after %s", timeout)
                        raise error
                    time.sleep(period)

        return wrapper

    return act_decorator


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    def wait_for_text(self, locator_type, locator, text):
        """Wait until text appears in element"""
        self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))

    def wait_until_find(self, locator_type, locator):
        """Wait until element can be find"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    def wait_until_send_keys(self, locator_type, locator, data):
        """Wait until field enabled and send keys"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        field = self.driver.find_element(by=locator_type, value=locator)
        field.clear()
        field.send_keys(data)

    def wait_until_click(self, locator_type, locator):
        """Wait until button clickable and click"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        self.driver.find_element(by=locator_type, value=locator).click()

    def wait_until_find_elements(self, locator_type, locator):
        """Wait until elements can be find"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_elements(by=locator_type, value=locator)


class User:

    def __init__(self):
        self.__firstname = ""
        self.__lastname = ""
        self.__email = ""
        self.__password = ""
        self.__password_confirm = ""

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @firstname.deleter
    def firstname(self):
        self.__firstname = ""

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @lastname.deleter
    def lastname(self):
        self.__lastname = ""

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        self.__email = ""

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @password.deleter
    def password(self):
        self.__password = ""

    @property
    def password_confirm(self):
        return self.__password_confirm

    @password_confirm.setter
    def password_confirm(self, password_confirm):
        self.__password_confirm = password_confirm

    @password_confirm.deleter
    def password_confirm(self):
        self.__password_confirm = ""


