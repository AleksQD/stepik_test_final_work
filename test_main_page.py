from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # инициализируем Page Object,
    # передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()
    #  Инициализируем LoginPage 
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_no_products_in_basket()
    basket_page.should_massege_basket_is_empty()
