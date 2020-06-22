from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ""
    product_price = ""

    def add_product_to_basket(self):
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_available_in_stock()
        self.should_be_basket_button()

        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

        self.solve_quiz_and_get_code()
        self.should_be_success_message_with_product_name()
        self.should_be_success_message_with_stock_size()

    def should_be_available_in_stock(self):
        product_availability = self.is_element_present(*ProductPageLocators.PRODUCT_AVAILABILITY)
        assert product_availability, 'Product is not available in stock'

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Basket button for product is not found'

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name is not found'
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Price of product is not found'
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message_after_adding_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def should_be_success_message_with_product_name(self):
        product_name_in_success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name_in_success_message == self.product_name, 'Product name in success message is not correct'

    def should_be_success_message_with_stock_size(self):
        stock_size = self.browser.find_element(*ProductPageLocators.STOCK_SIZE).text
        assert stock_size == self.product_price, 'Stock size is not correct'

    def should_disappear_of_success_message(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is not disappeared, but ' \
                                                                          'should be '

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'
