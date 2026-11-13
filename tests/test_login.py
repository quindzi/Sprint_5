
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import (Login_Locators, Main_Locators, Registration_Locators, Password_Recovery_Locators, Account_Locators)
from url import LOGIN_URL, MAIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL

class Test_Login():

    def _open_login_page(self, driver, wait):
        wait.until(EC.url_contains("/login"))
        wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))

    def _fill_login_form(self, driver, wait):
        email_input=wait.until(EC.element_to_be_clickable(Login_Locators.EMAIL_FIELD))
        email_input.click()
        email_input.send_keys(Credentials.email)

        password_input=wait.until(EC.element_to_be_clickable(Login_Locators.PASSWORD_FIELD))
        password_input.click()
        password_input.send_keys(Credentials.password)

        login_button=wait.until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON))
        login_button.click()

    def _assert_logged_in(self, driver, wait):
        wait.until(EC.url_to_be(MAIN_URL))
        order_button=wait.until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

        assert order_button.is_displayed()

    def test_login_main_button(self, driver): #вход по кнопке «Войти в аккаунт» на главной
        wait=WebDriverWait(driver, 15)
        driver.get(MAIN_URL)

        wait.until(EC.element_to_be_clickable(Main_Locators.LOGIN_ON_MAIN_BUTTON)).click()

        self._open_login_page(driver, wait)
        self._fill_login_form(driver, wait)
        self._assert_logged_in(driver,wait)

    
    def test_login_account_button(self, driver): #вход через кнопку «Личный кабинет»
        wait=WebDriverWait(driver, 15)
        driver.get(MAIN_URL)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()

        self._open_login_page(driver, wait)
        self._fill_login_form(driver, wait)
        self._assert_logged_in(driver, wait)

    def test_login_link_from_registration(self, driver): #вход через кнопку в форме регистрации
        wait=WebDriverWait(driver, 15)
        driver.get(REGISTER_URL)

        wait.until(EC.visibility_of_element_located(Registration_Locators.HEADING))
        wait.until(EC.element_to_be_clickable(Registration_Locators.LOGIN_LINK)).click()

        self._open_login_page(driver, wait)
        self._fill_login_form(driver, wait)
        self._assert_logged_in(driver, wait)

    def test_login_link_form_forgot_password(self, driver): #вход через кнопку в форме восстановления пароля
        wait=WebDriverWait(driver, 15)
        driver.get(FORGOT_PASSWORD_URL)

        wait.until(EC.visibility_of_element_located(Password_Recovery_Locators.HEADING))
        wait.until(EC.element_to_be_clickable(Password_Recovery_Locators.LOGIN_LINK)).click()

        self._open_login_page(driver, wait)
        self._fill_login_form(driver, wait)
        self._assert_logged_in(driver, wait)
