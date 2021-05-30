import logging
import random

import pytest as pytest
from selenium import webdriver
from constants import start_page as constants_start_page
from pages.base import User
from pages.start_page import StartPage


def pytest_runtest_setup(item):
    """Prepare test"""
    log = logging.getLogger(item.name)
    item.cls.logger = log
    item.cls.variety = str(random.randint(10000000, 99999999))


class BaseTest:
    """BaseTest class for inheritance. Implements test class default variables."""
    logger = logging.getLogger(__name__)
    variety = str(random.randint(10000000, 99999999))


@pytest.fixture(scope="function")
def start_page():
    driver = webdriver.Chrome(executable_path='/Users/mike/PycharmProjects/Biotus/drivers/chromedriver')
    driver.implicitly_wait(5)
    # Open start page
    driver.get(constants_start_page.START_PAGE_URL)
    start_page = StartPage(driver)
    yield start_page
    driver.close()


@pytest.fixture(scope="function")
def register_user(start_page):
    variety = str(random.randint(10000000, 99999999))
    user = User()
    user.firstname = "John"
    user.lastname = "Doe"
    user.email = f"email{variety}@mail.com"
    user.password = "UsrPwd1234"
    user.password_confirm = "UsrPwd1234"
    start_page.fill_sign_up_fields(firstname=user.firstname, lastname=user.lastname, email=user.email,
                                   password=user.password, password_confirm=user.password_confirm)
    start_page.verify_sign_up(firstname=user.firstname, lastname=user.lastname)
    start_page.sign_out()
    return user
