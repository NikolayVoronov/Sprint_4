import allure
import pytest

from data import Texts
from pages.main_page import MainPage


@allure.feature('Проверки списков с ответами на вопросы')
class TestDropDown:
    @allure.title('Выпадающий список Стоимость в разделе вопросы о важном')
    @allure.description('Активируем список с ответами и проверяем корректность отображаемого в них текста')
    @pytest.mark.parametrize(
        'loc_button,loc_text,text',
        [
            [MainPage.DROP_DOWN_COST, MainPage.DROP_DOWN_COST_TEXT, Texts.TEXT_COST],
            [
                MainPage.DROP_DOWN_SEVERAL_SCOOTERS,
                MainPage.DROP_DOWN_SEVERAL_SCOOTERS_TEXT,
                Texts.TEXT_SEVERAL_SCOOTERS
            ],
            [MainPage.DROP_DOWN_TIME_COST, MainPage.DROP_DOWN_TIME_COST_TEXT, Texts.TEXT_TIME_COST],
            [MainPage.DROP_DOWN_ORDER_TODAY, MainPage.DROP_DOWN_ORDER_TODAY_TEXT, Texts.TEXT_ORDER_TODAY],
            [MainPage.DROP_DOWN_CHANGE_ORDER, MainPage.DROP_DOWN_CHANGE_ORDER_TEXT, Texts.TEXT_CHANGE_ORDER],
            [MainPage.DROP_DOWN_CHARGER, MainPage.DROP_DOWN_CHARGER_TEXT, Texts.TEXT_CHARGER],
            [MainPage.DROP_DOWN_CANCEL_ORDER, MainPage.DROP_DOWN_CANCEL_ORDER_TEXT, Texts.TEXT_CANCEL_ORDER],
            [MainPage.DROP_DOWN_MKAD, MainPage.DROP_DOWN_MKAD_TEXT, Texts.TEXT_MKAD]
        ]
    )
    def test_drop_down_cost(self, driver, loc_button, loc_text, text):
        main_page = MainPage(driver)
        main_page.go_to_main_site()
        main_page.set_drop_down(loc_button)
        assert main_page.find_text_drop_down(loc_text) == text, 'Текст не найден'
