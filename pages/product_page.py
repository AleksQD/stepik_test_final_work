from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(
            *ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def name_book_equal_name_in_basket(self):
        assert self.is_element_equal_element_in_basket(
            *ProductPageLocators.BOOK_NAME,
            *ProductPageLocators.BASKET_BOOK_NAME), \
            "Book name no equal book name in basket"

    def price_book_equal_basket(self):
        assert self.is_element_equal_element_in_basket(
            *ProductPageLocators.BOOK_PRICE,
            *ProductPageLocators.BASKET_BOOK_PRICE), \
            "Book price no equal book price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should have disappeared"
