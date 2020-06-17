from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_about_empty_basket(self):
        text_en = "Your basket is empty."
        assert text_en in self.browser.find_element(
            *BasketPageLocators.TEXT_EMPTY_BASKET).text, 'In basket page no text "Your basket is empty.", but should be'

    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_BASKET), 'Basket is not empty, but should be'
