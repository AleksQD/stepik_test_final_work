from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p")
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, "#messages strong")
    BASKET_BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe div")
