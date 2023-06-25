import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls, TestValues


@allure.feature('Проверки процесса оформления заказа')
class TestCreateOrder:

    @allure.title('Кнопка заказать в теле главной страницы')
    @allure.description('Проверяем, что кнопка заказа в теле страницы открывает страницу с оформлением заказа')
    def test_order_button_body(self, driver):
        driver.get(Urls.MAIN)
        main_page = MainPage(driver)
        main_page.click_order_button_body()
        assert driver.find_element(*OrderPage.HEADER_INFO).text == 'Для кого самокат', 'Заголовок страницы не найден'
        assert driver.current_url == Urls.WHO_ORDER_URL, 'Открыта некорректная страница'

    @allure.title('Полный позитивный цикл заказа самоката с первым набором данных')
    @allure.description('Открываем форму нового заказа, заполняем все поля и проверяем, что заказ успешно оформлен')
    def test_create_order_full_flow_1(self, driver):
        """ Открываем главную страницу и создаем объекты классов страниц """
        driver.get(Urls.MAIN)
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        """ Заполняем все поля в форме заказа 'Для кого' """
        order_page.set_user_info(TestValues.FIRST_NAME,
                                 TestValues.SURNAME,
                                 TestValues.ADRESS,
                                 TestValues.METRO,
                                 TestValues.PHONE)
        """ Заполняем все поля в форме заказа 'Про аренду' """
        order_page.set_pay_info_1(TestValues.DATE_ORDER,
                                  TestValues.COMMENTS)
        """ Подтверждаем оформление заказа """
        order_page.click_yes_button()
        """ Проверяем появилось ли сообщение, что заказ успешно оформлен """
        assert driver.find_element(*OrderPage.SUCCESS_ORDER_FIELD), 'Сообщение об успешном заказе не найдено'

    @allure.title('Полный позитивный цикл заказа самоката со вторым набором данных')
    @allure.description('Открываем форму нового заказа, заполняем все поля и проверяем, что заказ успешно оформлен')
    def test_create_order_full_flow_2(self, driver):
        """ Открываем главную страницу и создаем объекты классов страниц """
        driver.get(Urls.MAIN)
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        """ Заполняем все поля в форме заказа 'Для кого' """
        order_page.set_user_info(TestValues.FIRST_NAME_2,
                                 TestValues.SURNAME_2,
                                 TestValues.ADRESS_2,
                                 TestValues.METRO_2,
                                 TestValues.PHONE_2)
        """ Заполняем все поля в форме заказа 'Про аренду' """
        order_page.set_pay_info_2(TestValues.DATE_ORDER_2,
                                  TestValues.COMMENTS_2)
        """ Подтверждаем оформление заказа """
        order_page.click_yes_button()
        """ Проверяем появилось ли сообщение, что заказ успешно оформлен """
        assert driver.find_element(*OrderPage.SUCCESS_ORDER_FIELD), 'Сообщение об успешном заказе не найдено'

    @allure.title('Переход по кнопке с логотипом сервиса')
    @allure.description('Оформляем новый заказ и проверяем на странице со статусом заказа переход по кнопке')
    def test_into_logo_button(self, driver):
        """ Открываем главную страницу и создаем объекты классов страниц """
        driver.get(Urls.MAIN)
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        """ Заполняем все поля в форме заказа 'Для кого' """
        order_page.set_user_info(TestValues.FIRST_NAME,
                                 TestValues.SURNAME,
                                 TestValues.ADRESS,
                                 TestValues.METRO,
                                 TestValues.PHONE)
        """ Заполняем все поля в форме заказа 'Про аренду' """
        order_page.set_pay_info_1(TestValues.DATE_ORDER,
                                  TestValues.COMMENTS)
        """ Подтверждаем оформление заказа """
        order_page.click_yes_button()
        """ Переходим на страницу со статусом заказа """
        order_page.click_check_status_button()
        """ Нажимаем на кнопку с логотипом """
        main_page.click_scooter_logo_button()
        """ Проверяем открылась ли главная страница по URL и внутренним элементам """
        assert driver.find_element(*MainPage.INFO_SCOOTER_FIELD), 'Информация о сервисе самокат не найдена'
        assert driver.current_url == Urls.MAIN, 'Открыта некорректная страница'

    @allure.title('Переход по кнопке с логотипом яндекса')
    @allure.description('Оформляем новый заказ и проверяем на странице со статусом заказа переход по кнопке')
    def test_into_yandex_logo_button(self, driver):
        """ Открываем главную страницу и создаем объекты классов страниц """
        driver.get(Urls.MAIN)
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        order_page = OrderPage(driver)
        """ Заполняем все поля в форме заказа 'Для кого' """
        order_page.set_user_info(TestValues.FIRST_NAME,
                                 TestValues.SURNAME,
                                 TestValues.ADRESS,
                                 TestValues.METRO,
                                 TestValues.PHONE)
        """ Заполняем все поля в форме заказа 'Про аренду' """
        order_page.set_pay_info_1(TestValues.DATE_ORDER,
                                  TestValues.COMMENTS)
        """ Подтверждаем оформление заказа """
        order_page.click_yes_button()
        """ Переходим на страницу со статусом заказа """
        order_page.click_check_status_button()
        window_before = driver.window_handles[0]
        """ Нажимаем на кнопку с логотипом яндекса """
        main_page.click_yandex_logo_button()
        window_after = driver.window_handles[1]
        """ Переключаемся на открывшуюся вкладку """
        driver.switch_to.window(window_after)
        WebDriverWait(driver, 3).until(expected_conditions.title_is("Дзен"))
        """ Проверяем, что открылась страница дзена """
        assert driver.current_url == Urls.YANDEX, 'Открыта некорректная страница'
        driver.close()
        driver.switch_to.window(window_before)
