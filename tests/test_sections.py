from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import Main_Locators
from url import MAIN_URL

class TestSections:

    def test_sections_tab(self, driver):
        wait=WebDriverWait(driver, 15)
        driver.get(MAIN_URL)

        wait.until(EC.visibility_of_element_located(Main_Locators.HEADING))

        for tab_locator, heading_text in (Main_Locators.TAB_BUNS, "Булки"), (Main_Locators.TAB_SAUCES, "Соусы"), (Main_Locators.TAB_FILLINGS,"Начинки"):
            tab = wait.until(EC.element_to_be_clickable(tab_locator))
            driver.execute_script("arguments[0].click();", tab)
            
            wait.until(EC.text_to_be_present_in_element_attribute(tab_locator, "class", "tab_tab_type_current"),f"Вкладка «{heading_text}» не стала активной после клика",)
            active_tab = driver.find_element(*tab_locator)
            assert "tab_tab_type_current" in active_tab.get_attribute("class"), (f"Вкладка «{heading_text}» не стала активной после клика")

            section = wait.until(EC.visibility_of_element_located((By.XPATH, f'//h2[normalize-space()="{heading_text}"]')))
            assert section.is_displayed(), (f"Заголовок раздела «{heading_text}» не отобразился")

