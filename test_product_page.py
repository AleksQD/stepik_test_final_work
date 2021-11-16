
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # инициализируем Page Object,
    # передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()
    # выполняем метод страницы — добавляем товар в корзину
    page.add_to_basket()
    # расчитываем уравнение с переменной Х
    page.solve_quiz_and_get_code()
    # сравниваем имя кники с именем товара добавленного в корзину
    page.name_book_equal_name_in_basket()
    # сравниваем цену кники с ценой товара добавленного в корзину
    page.price_book_equal_basket()
