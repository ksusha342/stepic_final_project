from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasePageLocators


class MainPage(BasePage):
    def should_see_product_in_basket_opened_from_main_page(self,):
        self.browser.find_element(*BasePageLocators.BASKET).click()
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_BASKET), 'Product(s) in basket are presented, but should not be'
