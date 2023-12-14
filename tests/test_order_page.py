from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import DataOrderHeaderBtn, DataOrderMainBtn
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в шапке главной страницы')
    def test_create_order_header_btn(self, driver):
        MainPage(driver).get_cookies(MainPageLocators.COOKIES_BTN)
        OrderPage(driver).click_header_order_btn()
        OrderPage(driver).create_order(DataOrderHeaderBtn.name,
                                       DataOrderHeaderBtn.last_name,
                                       DataOrderHeaderBtn.address,
                                       OrderPageLocators.STATION_1,
                                       DataOrderHeaderBtn.phone,
                                       OrderPageLocators.DATE_1,
                                       OrderPageLocators.TERM_1,
                                       OrderPageLocators.BLACK_COLOR,
                                       DataOrderHeaderBtn.comment)
        text = OrderPage(driver).check_success_order()
        assert 'Заказ оформлен' in text

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине главной страницы')
    def test_create_order_main_page_btn(self, driver):
        MainPage(driver).get_cookies(MainPageLocators.COOKIES_BTN)
        OrderPage(driver).click_main_order_btn()
        OrderPage(driver).create_order(DataOrderMainBtn.name,
                                       DataOrderMainBtn.last_name,
                                       DataOrderMainBtn.address,
                                       OrderPageLocators.STATION_2,
                                       DataOrderMainBtn.phone,
                                       OrderPageLocators.DATE_2,
                                       OrderPageLocators.TERM_2,
                                       OrderPageLocators.GREY_COLOR,
                                       DataOrderMainBtn.comment)
        text = OrderPage(driver).check_success_order()
        assert 'Заказ оформлен' in text
