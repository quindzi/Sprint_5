import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver import get_driver
from data import Credentials
from locators import Main_Locators, Login_Locators
from url import MAIN_URL

@pytest.fixture
def driver():
    driver=get_driver()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    wait = WebDriverWait(driver, 15)
    driver.get(MAIN_URL)

    wait.until(EC.element_to_be_clickable(Main_Locators.LOGIN_ON_MAIN_BUTTON)).click()
    wait.until(EC.url_contains("/login"))
    wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))

    email_input = wait.until(EC.element_to_be_clickable(Login_Locators.EMAIL_FIELD))
    email_input.send_keys(Credentials.email)
    password_input = wait.until(EC.element_to_be_clickable(Login_Locators.PASSWORD_FIELD))
    password_input.send_keys(Credentials.password)

    wait.until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON)).click()

    wait.until(EC.url_to_be(MAIN_URL))
    wait.until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

    return driver