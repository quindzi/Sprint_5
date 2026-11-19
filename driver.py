from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def get_driver():

    options=Options()
    options.add_argument('--window-size=1600,900')

    driver=webdriver.Chrome(options=options)

    driver.get('https://stellarburgers.education-services.ru/')

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(@class, "AppHeader_header__logo__")]')
        )
    )
    return driver