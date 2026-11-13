from selenium.webdriver.common.by import By

class Registration_Locators:
    HEADING = (By.XPATH, '//h2[normalize-space()="Регистрация"]')
    NAME_FIELD=(By.XPATH, '//label[normalize-space()="Имя"]/following-sibling::input')
    EMAIL_FIELD=(By.XPATH, '//label[normalize-space()="Email"]/following-sibling::input')
    PASSWORD_FIELD=(By.XPATH, '//label[normalize-space()="Пароль"]/following-sibling::input')
    REGISTER_BUTTON=(By.XPATH, '//button[normalize-space()="Зарегистрироваться"]')
    LOGIN_LINK = (By.XPATH, '//a[normalize-space()="Войти" and @href="/login"]')
    ERROR_MESSAGE = (By.XPATH, '//p[contains(@class,"input__error")]')

class Login_Locators:
    HEADING = (By.XPATH, '//h2[normalize-space()="Вход"]')
    EMAIL_FIELD=(By.XPATH, '//label[normalize-space()="Email"]/following-sibling::input')
    PASSWORD_FIELD=(By.XPATH, '//label[normalize-space()="Пароль"]/following-sibling::input')
    LOGIN_BUTTON = (By.XPATH, '//button[normalize-space()="Войти"]')

class Main_Locators:
    CONSTRUCTOR_LINK =(By.XPATH, '//p[normalize-space()="Конструктор"]/parent::a')
    HEADING = (By.XPATH, '//h1[normalize-space()="Соберите бургер"]')
    LOGIN_ON_MAIN_BUTTON = (By.XPATH, '//button[normalize-space()="Войти в аккаунт"]')
    ACCOUNT_BUTTON = (By.XPATH, '//p[normalize-space()="Личный Кабинет"]/parent::a')
    FEED_LINK = (By.XPATH, '//p[normalize-space()="Лента Заказов"]/parent::a')
    ORDER_BUTTON = (By.XPATH, '//button[normalize-space()="Оформить заказ"]')
    LOGO = (By.XPATH, '//div[contains(@class,"AppHeader_header__logo")]//a')
    TAB_BUNS = (By.XPATH, '//div[contains(@class,"tab_tab__")][.//span[normalize-space()="Булки"]]')
    TAB_SAUCES = (By.XPATH, '//div[contains(@class,"tab_tab__")][.//span[normalize-space()="Соусы"]]')
    TAB_FILLINGS = (By.XPATH, '//div[contains(@class,"tab_tab__")][.//span[normalize-space()="Начинки"]]')


class Password_Recovery_Locators:
    HEADING = (By.XPATH, '//h2[normalize-space()="Восстановление пароля"]')
    EMAIL_FIELD = (By.XPATH, '//label[normalize-space()="Email"]/following-sibling::input')
    RECOVER_BUTTON = (By.XPATH, '//button[normalize-space()="Восстановить"]')
    LOGIN_LINK = (By.XPATH, '//a[normalize-space()="Войти" and @href="/login"]')

class Account_Locators:
    PROFILE_LINK = (By.XPATH, '//a[normalize-space()="Профиль"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[normalize-space()="Выход"]')