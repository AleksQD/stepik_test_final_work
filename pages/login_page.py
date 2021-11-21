from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверка на корректный url адрес
    def should_be_login_url(self):        
        assert 'login' in self.browser.current_url, 'inconsistent url, no "login" in url'

    # проверка что есть форма логина
    def should_be_login_form(self):        
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    
    # проверка что есть форма регистрации на странице
    def should_be_register_form(self):        
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    # регистрация нового юзера
    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        mail.send_keys(email)

        password_1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS)
        password_1.send_keys(password)

        password_2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_CONF_PASS)
        password_2.send_keys(password)

        button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        button.click()
