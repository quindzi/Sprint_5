import random
import string
import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import Registration_Locators, Login_Locators
from url import REGISTER_URL

@pytest.fixture
def new_email():
    digits = "".join(random.choices(string.digits, k=3))
    return f"alisa_mukovnina_54_{digits}@yandex.ru"

class Test_Registration:

    def test_successful_registration(self, driver, new_email): #успешная регистрация
        wait=WebDriverWait(driver, 15)
        driver.get(REGISTER_URL)

        name_input= wait.until(EC.element_to_be_clickable(Registration_Locators.NAME_FIELD))
        name_input.send_keys("Алиса")
        email_input=wait.until(EC.element_to_be_clickable(Registration_Locators.EMAIL_FIELD))
        email_input.send_keys(new_email)
        password_input=wait.until(EC.element_to_be_clickable(Registration_Locators.PASSWORD_FIELD))
        password_input.send_keys(Credentials.password)

        wait.until(EC.element_to_be_clickable(Registration_Locators.REGISTER_BUTTON)).click()

        wait.until(EC.url_contains("/login"))
        heading = wait.until(EC.visibility_of_element_located(Login_Locators.HEADING))
        assert heading.is_displayed(), "После успешной регистрации не открылась страница входа"

    def test_short_password_error(self, driver, new_email): #Ошибку для некорректного пароля
        wait=WebDriverWait(driver, 15)
        driver.get(REGISTER_URL)

        name_input= wait.until(EC.element_to_be_clickable(Registration_Locators.NAME_FIELD))
        name_input.send_keys("Алиса")
        email_input=wait.until(EC.element_to_be_clickable(Registration_Locators.EMAIL_FIELD))
        email_input.send_keys(new_email)
        password_input=wait.until(EC.element_to_be_clickable(Registration_Locators.PASSWORD_FIELD))
        password_input.send_keys("1234")

        wait.until(EC.element_to_be_clickable(Registration_Locators.REGISTER_BUTTON)).click()

        error=wait.until(EC.element_to_be_clickable(Registration_Locators.ERROR_MESSAGE))
        assert "Некорректный пароль" in error.text, ("Сообщение об ошибке не содержит текст «Некорректный пароль»")
