from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket not empty, item in basket"

    def should_massege_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "No presented message: basket is empty"
