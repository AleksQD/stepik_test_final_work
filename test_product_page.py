import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'Qwdsa12345'
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page_prod = ProductPage(browser, link)
        page_prod.open()
        # добавляем товар в корзину
        page_prod.add_to_basket()
        # сравниваем имя книги с именем товара добавленного в корзину
        page_prod.name_book_equal_name_in_basket()
        # сравниваем цену кники с ценой товара добавленного в корзину
        page_prod.price_book_equal_basket()

    # @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page_prod = ProductPage(browser, link)
        page_prod.open()
        page_prod.should_not_be_success_message()


@pytest.mark.need_review
#@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                 pytest.param(7, marks=pytest.mark.xfail),
#                                  8, 9])
@pytest.mark.parametrize('link', [0])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    # добавляем товар в корзину
    page.add_to_basket()
    # расчитываем уравнение с переменной Х
    page.solve_quiz_and_get_code()
    # сравниваем имя кники с именем товара добавленного в корзину
    page.name_book_equal_name_in_basket()
    # сравниваем цену кники с ценой товара добавленного в корзину
    page.price_book_equal_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


# @pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_no_products_in_basket()
    basket_page.should_massege_basket_is_empty()


# @pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.disappeared_success_message()
