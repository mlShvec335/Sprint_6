from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):
    @allure.step('Клик на кнопку "Заказать" в шапке главной')
    def click_header_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_HEADER)

    @allure.step('Клик на кнопку "Заказать" в середине главной страницы')
    def click_main_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_PAGE)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбор станции метро')
    def set_metro(self, station):
        self.find_element(OrderPageLocators.METRO_FIELD)
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.click_to_element(station)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.set_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        self.click_to_element(OrderPageLocators.NEXT_BTN)

    @allure.step('Выбор даты доставки')
    def set_date(self, date):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.find_element(date)
        self.click_to_element(date)

    @allure.step('Выбор срока аренды')
    def set_term(self, term):
        self.click_to_element(OrderPageLocators.RENT_FIELD)
        self.find_element(term)
        self.click_to_element(term)

    @allure.step('Выбор цвета')
    def set_color(self, color):
        self.click_to_element(color)

    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self, comments):
        self.set_text(OrderPageLocators.COMMENTS, comments)

    @allure.step('Появление модального окна "Заказ оформлен"')
    def check_success_order(self):
        return self.find_element(OrderPageLocators.ORDER_SUCCESS_WINDOW).text

    def create_order(self,
                     name,
                     last_name,
                     address,
                     station,
                     phone,
                     date,
                     term,
                     color,
                     comments):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station)
        self.set_phone(phone)
        self.click_next_btn()
        self.set_date(date)
        self.set_term(term)
        self.set_color(color)
        self.set_comments(comments)
        self.click_to_element(OrderPageLocators.ORDER_BTN)
        self.click_to_element(OrderPageLocators.YES_BTN)
