from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import (Main_Locators, Login_Locators, Account_Locators)
from url import MAIN_URL

class Test_Navigation_And_Account:

    def test_transition_to_account(self, logged_in_driver): #переход по клику на «Личный кабинет»
        wait= WebDriverWait(logged_in_driver, 15)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account"))

        profile_link=wait.until(EC.visibility_of_element_located(Account_Locators.PROFILE_LINK))

        assert profile_link.is_displayed(), "Ссылка «Профиль» не отобразилась в личном кабинете"

    def test_transition_to_constructor(self, logged_in_driver): #переход по клику на «Конструктор» и на логотип Stellar Burgers
        wait= WebDriverWait(logged_in_driver, 15)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(Main_Locators.CONSTRUCTOR_LINK)).click()
        wait.until(EC.url_to_be(MAIN_URL))

        heading = wait.until(EC.visibility_of_element_located(Main_Locators.HEADING))
        assert heading.is_displayed(), "Заголовок главной не отобразился после перехода в «Конструктор»"

    def test_transition_by_logo(self, logged_in_driver):
        wait = WebDriverWait(logged_in_driver, 15)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(Main_Locators.LOGO)).click()
        wait.until(EC.url_to_be(MAIN_URL))

        heading = wait.until(EC.visibility_of_element_located(Main_Locators.HEADING))
        assert heading.is_displayed(), "Заголовок главной не отобразился после клика по логотипу"

    def test_logout(self, logged_in_driver): #выход по кнопке «Выйти» в личном кабинете
        wait= WebDriverWait(logged_in_driver, 15)

        wait.until(EC.element_to_be_clickable(Main_Locators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account"))

        wait.until(EC.element_to_be_clickable(Account_Locators.LOGOUT_BUTTON)).click()
        wait.until(EC.url_contains("/login"))

        heading = wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))
        assert heading.is_displayed(), "Заголовок формы входа не отобразился после выхода"
        
