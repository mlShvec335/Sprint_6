from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    @allure.step('Клик на вопрос')
    def click_question(self, number):
        method, locator = MainPageLocators.QUESTION
        locator = locator.format(number)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((method, locator)))
        return self.click_to_element((method, locator))

    @allure.step('Получение ответа')
    def get_answer(self, number):
        method, locator = MainPageLocators.ANSWER
        locator = locator.format(number)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((method, locator)))
        return self.get_text((method, locator))

    @allure.step('Клик на Яндекс в шапке')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Клик на Самокат в шапке')
    def click_samokat_logo(self):
        self.click_to_element(MainPageLocators.SAMOKAT_LOGO)
