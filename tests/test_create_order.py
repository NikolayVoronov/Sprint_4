from pages.main_page import MainPage
from pages.who_order_page import WhoOrderPage
from pages.pay_order_page import PayOrderPage
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data import *
import time
import allure

class TestCreateOrder:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Кнопка заказать в теле главной страницы')
    @allure.description('Проверяем, что кнопка заказа в теле страницы открывает страницу с оформлением заказа')
    def test_order_button_body(self):
        self.driver.get(Urls.MAIN)
        main_page = MainPage(self.driver)
        main_page.click_order_button_body()
        assert self.driver.find_element(*WhoOrderPage.HEADER_INFO).text == 'Для кого самокат'\
            , 'Заголовок страницы не найден'
        assert self.driver.current_url == Urls.WHO_ORDER_URL, 'Открыта некорректная страница'

    @allure.title('Полный позитивный цикл заказа самоката с первым набором данных')
    @allure.description('Открываем форму нового заказа, заполняем все поля, проверяем, что:'
                        ' заказ успешно оформлен, по логотипу сервиса открывается главная страница, '
                        'а по логотипу яндекса открывается главная страница яндекса')
    def test_create_order_full_flow_1(self):
        self.driver.get(Urls.MAIN)
        base_page = BasePage(self.driver)
        base_page.click_order_button_header()
        who_order_page = WhoOrderPage(self.driver)
        first_name = "Жан Жак"
        surname = "Тестировалль"
        adress = "Вымышленный адрес"
        metro = "Аэропорт"
        phone = "+79999999999"
        who_order_page.set_user_info(first_name, surname, adress, metro, phone)
        pay_order_page = PayOrderPage(self.driver)
        date_order = "25.06.2023"
        comments = "Комментарий для курьера"
        pay_order_page.set_pay_info_1(date_order, comments)
        pay_order_page.click_yes_button()
        assert self.driver.find_element(*PayOrderPage.SUCCESS_ORDER_FIELD), 'Сообщение об успешном заказе не найдено'
        pay_order_page.click_check_status_button()
        WebDriverWait(self.driver, 3)
        base_page.click_scooter_logo_button()
        WebDriverWait(self.driver, 3)
        assert self.driver.find_element(*MainPage.INFO_SCOOTER_FIELD), 'Информация о сервисе самокат не найдена'
        assert self.driver.current_url == Urls.MAIN, 'Открыта некорректная страница'
        window_before = self.driver.window_handles[0]
        base_page.click_yandex_logo_button()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(3)
        assert self.driver.current_url == Urls.YANDEX, 'Открыта некорректная страница'
        self.driver.close()
        self.driver.switch_to.window(window_before)


    def test_create_order_full_flow_2(self):
        self.driver.get(Urls.MAIN)
        base_page = BasePage(self.driver)
        base_page.click_order_button_header()
        who_order_page = WhoOrderPage(self.driver)
        first_name = "Агент"
        surname = "Смит"
        adress = "г. Зеон, ул. Машинная, д.5, корп.7"
        metro = "Автозаводская"
        phone = "77776665544"
        who_order_page.set_user_info(first_name, surname, adress, metro, phone)
        pay_order_page = PayOrderPage(self.driver)
        date_order = "01.07.2023"
        comments = "Пожалуйста, не звоните утром, вы можете разбудить Нео"
        pay_order_page.set_pay_info_2(date_order, comments)
        pay_order_page.click_yes_button()
        assert self.driver.find_element(*PayOrderPage.SUCCESS_ORDER_FIELD), 'Сообщение об успешном заказе не найдено'
        pay_order_page.click_check_status_button()
        WebDriverWait(self.driver, 3)
        base_page.click_scooter_logo_button()
        WebDriverWait(self.driver, 3)
        assert self.driver.find_element(*MainPage.INFO_SCOOTER_FIELD), 'Информация о сервисе самокат не найдена'
        assert self.driver.current_url == Urls.MAIN, 'Открыта некорректная страница'
        window_before = self.driver.window_handles[0]
        base_page.click_yandex_logo_button()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(3)
        assert self.driver.current_url == Urls.YANDEX, 'Открыта некорректная страница'
        self.driver.close()
        self.driver.switch_to.window(window_before)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
