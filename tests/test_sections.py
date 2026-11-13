from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import Main_Locators
from url import MAIN_URL

class Test_Sections:

    def test_sections_tab(self, driver):
        wait=WebDriverWait(driver, 15)
        driver.get(MAIN_URL)

        wait.until(EC.visibility_of_element_located(Main_Locators.HEADING))

        for tab, heading in (Main_Locators.TAB_BUNS, "Булки"), (Main_Locators.TAB_SAUCES, "Соусы"), (Main_Locators.TAB_FILLINGS,"Начинки"):
            tab_element=wait.until(EC.element_to_be_clickable(tab))
            driver.execute_script("arguments[0].click();", tab_element)
            
            assert "tab_tab_type_current" in tab_element.get_attribute("class")
            section=(By.XPATH, f'//h2[normalize-space()="{heading}"]')
            assert wait.until(EC.visibility_of_element_located(section)).is_displayed()

