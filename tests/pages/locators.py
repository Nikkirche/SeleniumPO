from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_2 = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUM_CART = (By.CLASS_NAME, "btn-cart")
    MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE = (By.CLASS_NAME, "price_color")
    NAME = (By.CSS_SELECTOR, ".product_main > h1")


class BasketPageLocators():
    LIST_OF_ITEMS_IN_BASKET = (By.CLASS_NAME, "basket-items")
    MESSAGE_ABOUT_0_ELEMENTS_IN_BASKET = (By.XPATH, "//*[@id='content_inner']")
