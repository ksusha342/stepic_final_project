from selenium.webdriver.common.by import By


class BasketPageLocators:
    PRODUCT_BASKET = (By.CSS_SELECTOR, ".row h3 a")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, ".product_main .instock")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    STOCK_SIZE = (By.CSS_SELECTOR, ".alertinner p strong")