from selenium.webdriver.common.by import By


class BasketPageLocators:
    PRODUCT_BASKET = (By.CSS_SELECTOR, ".row h3 a")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    USER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    USER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, ".product_main .instock")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    STOCK_SIZE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")