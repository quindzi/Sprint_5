from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import (Main_Locators, Login_Locators, Account_Locators)
from url import MAIN_URL

class Test_Navigation_And_Account:

    def _login(self, driver, wait):
        driver.get(MAIN_URL)
        wait.until(EC.element_to_be_clickable(Main_Locators.LOGIN_ON_MAIN_BUTTON)).click()
        wait.until(EC.url_contains("/login"))
        wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))

        email_input=wait.until(EC.element_to_be_clickable(Login_Locators.EMAIL_FIELD))
        email_input.send_keys(Credentials.email)
        password_input=wait.until(EC.element_to_be_clickable(Login_Locators.PASSWORD_FIELD))
        password_input.send_keys(Credentials.password)

        wait.until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON)).click()

        wait.until(EC.url_to_be(MAIN_URL))
        wait.until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

    def test_transition_to_account(self, driver): #переход по клику на «Личный кабинет»
        wait= WebDriverWait(driver, 15)
        self._login(driver, wait)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()

        wait.until(EC.url_contains("/account"))
        assert wait.until(EC.visibility_of_element_located(Account_Locators.PROFILE_LINK)).is_displayed

    def test_transition_to_constructor_and_logo(self, driver): #переход по клику на «Конструктор» и на логотип Stellar Burgers
        wait= WebDriverWait(driver, 15)
        self._login(driver, wait)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(Main_Locators.CONSTRUCTOR_LINK)).click()
        wait.until(EC.url_to_be(MAIN_URL))
        assert wait.until(EC.visibility_of_element_located(Main_Locators.HEADING)).is_displayed

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account"))
        wait.until(EC.element_to_be_clickable(Main_Locators.LOGO)).click()
        wait.until(EC.url_to_be(MAIN_URL))
        assert wait.until(EC.visibility_of_element_located(Main_Locators.HEADING)).is_displayed

    def test_logout(self, driver): #выход по кнопке «Выйти» в личном кабинете
        wait= WebDriverWait(driver, 15)
        self._login(driver, wait)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(Account_Locators.LOGOUT_BUTTON)).click()

        wait.until(EC.url_contains("/login"))
        assert wait.until(EC.visibility_of_element_located(Login_Locators.HEADING)).is_displayed
