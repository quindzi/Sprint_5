
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import (Login_Locators, Main_Locators, Registration_Locators, Password_Recovery_Locators, Account_Locators)
from url import LOGIN_URL, MAIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL

class TestLogin:

    def test_login_main_button(self, driver): #вход по кнопке «Войти в аккаунт» на главной
        wait=WebDriverWait(driver, 15)
        driver.get(MAIN_URL)

        login_on_main_btn = wait.until(EC.element_to_be_clickable(Main_Locators.LOGIN_ON_MAIN_BUTTON))
        login_on_main_btn.click()

        wait.until(EC.url_contains("/login"))
        heading_login = wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))
        assert heading_login.is_displayed(), "Заголовок формы входа не отобразился после клика по кнопке"

        email_input = wait.until(EC.element_to_be_clickable(Login_Locators.EMAIL_FIELD))
        email_input.click()
        email_input.send_keys(Credentials.email)

        password_input = wait.until(EC.element_to_be_clickable(Login_Locators.PASSWORD_FIELD))
        password_input.click()
        password_input.send_keys(Credentials.password)

        login_btn = wait.until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON))
        login_btn.click()

        wait.until(EC.url_to_be(MAIN_URL))
        order_button = wait.until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отобразилась после успешного входа"

    
    def test_login_account_button(self, driver): #вход через кнопку «Личный кабинет»
        wait=WebDriverWait(driver, 15)
        driver.get(MAIN_URL)

        login_on_main_btn=wait.until(EC.element_to_be_clickable(Main_Locators.LOGIN_ON_MAIN_BUTTON))
        login_on_main_btn.click()

        wait.until(EC.url_contains("/login"))
        heading=wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))
        assert heading.is_displayed(), "Заголовок формы не отобразился"

        email_input=wait.until(EC.element_to_be_clickable(Login_Locators.EMAIL_FIELD))
        email_input.click()
        email_input.send_keys(Credentials.email)

        password_input=wait.until(EC.element_to_be_clickable(Login_Locators.PASSWORD_FIELD))
        password_input.click()
        password_input.send_keys(Credentials.password)

        login_btn=wait.until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON))
        login_btn.click()

        wait.until(EC.url_to_be(MAIN_URL))
        order_button=wait.until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отобразилась после успешного входа"

    def test_login_link_from_registration(self, driver): #вход через кнопку в форме регистрации
        wait=WebDriverWait(driver, 15)
        driver.get(REGISTER_URL)

        heading = wait.until(EC.visibility_of_element_located(Registration_Locators.HEADING))
        assert heading.is_displayed(), "Страница регистрации не загрузилась"

        login_link = wait.until(EC.element_to_be_clickable(Registration_Locators.LOGIN_LINK))
        login_link.click()

        wait.until(EC.url_contains("/login"))
        heading_login = wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))
        assert heading_login.is_displayed(), "Форма входа не отобразилась после перехода по ссылке"

        email_input = wait.until(EC.element_to_be_clickable(Login_Locators.EMAIL_FIELD))
        email_input.click()
        email_input.send_keys(Credentials.email)

        password_input = wait.until(EC.element_to_be_clickable(Login_Locators.PASSWORD_FIELD))
        password_input.click()
        password_input.send_keys(Credentials.password)

        login_btn = wait.until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON))
        login_btn.click()

        wait.until(EC.url_to_be(MAIN_URL))
        order_button = wait.until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отобразилась после входа"

    def test_login_link_form_forgot_password(self, driver): #вход через кнопку в форме восстановления пароля
        wait=WebDriverWait(driver, 15)
        driver.get(FORGOT_PASSWORD_URL)

        heading = wait.until(EC.visibility_of_element_located(Password_Recovery_Locators.HEADING))
        assert heading.is_displayed(), "Страница восстановления пароля не загрузилась"

        login_link = wait.until(EC.element_to_be_clickable(Password_Recovery_Locators.LOGIN_LINK))
        login_link.click()

        wait.until(EC.url_contains("/login"))
        heading_login = wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))
        assert heading_login.is_displayed(), "Форма входа не отобразилась после перехода"

        email_input = wait.until(EC.element_to_be_clickable(Login_Locators.EMAIL_FIELD))
        email_input.click()
        email_input.send_keys(Credentials.email)

        password_input = wait.until(EC.element_to_be_clickable(Login_Locators.PASSWORD_FIELD))
        password_input.click()
        password_input.send_keys(Credentials.password)

        login_btn = wait.until(EC.element_to_be_clickable(Login_Locators.LOGIN_BUTTON))
        login_btn.click()

        wait.until(EC.url_to_be(MAIN_URL))
        order_button = wait.until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Кнопка «Оформить заказ» не отобразилась после входа"
