import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls, TestValues


@allure.feature('Проверки процесса оформления заказа')
class TestCreateOrder:

    @allure.title('Кнопка заказать в теле главной страницы')
    @allure.description('Проверяем, что кнопка заказа в теле страницы открывает страницу с оформлением заказа')
    def test_order_button_body(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_main_site()
        main_page.click_order_button_body()
        assert order_page.find_text_header_info() == 'Для кого самокат', 'Заголовок страницы не найден'
        assert main_page.current_url_page() == Urls.WHO_ORDER_URL, 'Открыта некорректная страница'

    @allure.title('Полный позитивный цикл заказа самоката с первым набором данных')
    @allure.description('Открываем форму нового заказа, заполняем все поля и проверяем, что заказ успешно оформлен')
    def test_create_order_full_flow_1(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_site()
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.set_user_info(TestValues.FIRST_NAME,
                                 TestValues.SURNAME,
                                 TestValues.ADRESS,
                                 TestValues.METRO,
                                 TestValues.PHONE)
        order_page.set_pay_info_1(TestValues.DATE_ORDER,
                                  TestValues.COMMENTS)
        order_page.click_yes_button()
        assert order_page.find_element_success_order(), 'Сообщение об успешном заказе не найдено'

    @allure.title('Полный позитивный цикл заказа самоката со вторым набором данных')
    @allure.description('Открываем форму нового заказа, заполняем все поля и проверяем, что заказ успешно оформлен')
    def test_create_order_full_flow_2(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_site()
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        order_page.set_user_info(TestValues.FIRST_NAME_2,
                                 TestValues.SURNAME_2,
                                 TestValues.ADRESS_2,
                                 TestValues.METRO_2,
                                 TestValues.PHONE_2)
        order_page.set_pay_info_2(TestValues.DATE_ORDER_2,
                                  TestValues.COMMENTS_2)
        order_page.click_yes_button()
        assert order_page.find_element_success_order(), 'Сообщение об успешном заказе не найдено'
