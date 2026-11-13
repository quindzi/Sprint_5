from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="function")
def driver():
    options=Options() 
    options.add_argument('--window-size=1600,900')
    driver=webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    