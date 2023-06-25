import allure

from pages.main_page import MainPage
from data import Urls


@allure.feature('Проверки переходов по кнопкам с логотипами')
class TestLogoButtons:

    @allure.title('Переход по кнопке с логотипом сервиса')
    @allure.description('Переходим по кнопке и проверяем, что открылась главная страница сервиса')
    def test_into_logo_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_site()
        main_page.click_scooter_logo_button()
        assert main_page.find_element_info_scooter(), 'Информация о сервисе самокат не найдена'
        assert main_page.current_url_page() == Urls.MAIN, 'Открыта некорректная страница'

    @allure.title('Переход по кнопке с логотипом яндекса')
    @allure.description('Переходим по кнопке и проверяем, что открылась страница сервиса Дзен')
    def test_into_yandex_logo_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_site()
        main_page.click_yandex_logo_button_and_switch()
        assert main_page.current_url_page() == Urls.YANDEX, 'Открыта некорректная страница'
