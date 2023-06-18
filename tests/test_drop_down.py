from pages.main_page import MainPage
from selenium import webdriver
from data import *
import allure

class TestDropDown:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Выпадающий список Стоимость в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_cost(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_cost()
        assert self.driver.find_element(*MainPage.DROP_DOWN_COST_TEXT).text == Texts.TEXT_COST\
            , 'Текст не найден'

    @allure.title('Выпадающий список Самокаты в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_several_scooters(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_several_scooters()
        assert self.driver.find_element(*MainPage.DROP_DOWN_SEVERAL_SCOOTERS_TEXT).text == Texts.TEXT_SEVERAL_SCOOTERS\
            , 'Текст не найден'

    @allure.title('Выпадающий список Время аренды в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_time_cost(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_time_cost()
        assert self.driver.find_element(*MainPage.DROP_DOWN_TIME_COST_TEXT).text == Texts.TEXT_TIME_COST\
            , 'Текст не найден'

    @allure.title('Выпадающий список Заказ сегодня в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_order_today(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_order_today()
        assert self.driver.find_element(*MainPage.DROP_DOWN_ORDER_TODAY_TEXT).text == Texts.TEXT_ORDER_TODAY\
            , 'Текст не найден'

    @allure.title('Выпадающий список Изменение заказа в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_change_order(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_change_order()
        assert self.driver.find_element(*MainPage.DROP_DOWN_CHANGE_ORDER_TEXT).text == Texts.TEXT_CHANGE_ORDER\
            , 'Текст не найден'

    @allure.title('Выпадающий список Зарядка в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_charger(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_charger()
        assert self.driver.find_element(*MainPage.DROP_DOWN_CHARGER_TEXT).text == Texts.TEXT_CHARGER\
            , 'Текст не найден'

    @allure.title('Выпадающий список Отмена заказа в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_cancel_order(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_cancel_order()
        assert self.driver.find_element(*MainPage.DROP_DOWN_CANCEL_ORDER_TEXT).text == Texts.TEXT_CANCEL_ORDER\
            , 'Текст не найден'

    @allure.title('Выпадающий список Заказа за МКАД в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    def test_drop_down_mkad(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.set_drop_down_mkad()
        assert self.driver.find_element(*MainPage.DROP_DOWN_MKAD_TEXT).text == Texts.TEXT_MKAD\
            , 'Текст не найден'
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
