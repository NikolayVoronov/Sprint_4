import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    """ Выпадающие списки в разделе 'Вопросы о важном' """
    """ Кнопка и текст со стоимостью самокатов """
    DROP_DOWN_COST = [By.XPATH, ".//div[contains(@id,'accordion__heading-0')]/parent::div"]
    DROP_DOWN_COST_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-0')]/p"]
    """ Кнопка и текст с количеством самокатов """
    DROP_DOWN_SEVERAL_SCOOTERS = [By.XPATH, ".//div[contains(@id,'accordion__heading-1')]/parent::div"]
    DROP_DOWN_SEVERAL_SCOOTERS_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-1')]/p"]
    """ Кнопка и текст с расчетом стоимости аренды """
    DROP_DOWN_TIME_COST = [By.XPATH, ".//div[contains(@id,'accordion__heading-2')]/parent::div"]
    DROP_DOWN_TIME_COST_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-2')]/p"]
    """ Кнопка и текст с возможностью заказать самокат сегодня """
    DROP_DOWN_ORDER_TODAY = [By.XPATH, ".//div[contains(@id,'accordion__heading-3')]/parent::div"]
    DROP_DOWN_ORDER_TODAY_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-3')]/p"]
    """ Кнопка и текст с возможностью продлить или вернуть самокат """
    DROP_DOWN_CHANGE_ORDER = [By.XPATH, ".//div[contains(@id,'accordion__heading-4')]/parent::div"]
    DROP_DOWN_CHANGE_ORDER_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-4')]/p"]
    """ Кнопка и текст с зарядкой """
    DROP_DOWN_CHARGER = [By.XPATH, ".//div[contains(@id,'accordion__heading-5')]/parent::div"]
    DROP_DOWN_CHARGER_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-5')]/p"]
    """ Кнопка и текст с возможностью отменить заказ """
    DROP_DOWN_CANCEL_ORDER = [By.XPATH, ".//div[contains(@id,'accordion__heading-6')]/parent::div"]
    DROP_DOWN_CANCEL_ORDER_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-6')]/p"]
    """ Кнопка и текст с доставкой за МКАД """
    DROP_DOWN_MKAD = [By.XPATH, ".//div[contains(@id,'accordion__heading-7')]/parent::div"]
    DROP_DOWN_MKAD_TEXT = [By.XPATH, ".//div[contains(@id,'accordion__panel-7')]/p"]

    """Кнопка заказать в теле и шапке страницы"""
    ORDER_BUTTON_HEADER = [By.XPATH, ".//div[contains(@class,'Header_Nav__AGCXC')]/button[text()='Заказать']"]
    ORDER_BUTTON_BODY = [By.XPATH, ".//div[contains(@class,'Home_FinishButton__1_cWm')]/button"]

    """ Поле с информацией о сервисе """
    INFO_SCOOTER_FIELD = [By.XPATH, ".//div[text()='Привезём его прямо к вашей двери,']"]

    """Кнопка с логотипом сервиса самокат"""
    SCOOTER_LOGO_BUTTON = [By.XPATH, ".//a[contains(@class,'Header_LogoScooter')]"]

    """Кнопка с логотипом яндекса"""
    YANDEX_LOGO_BUTTON = [By.XPATH, ".//a[contains(@class,'Header_LogoYandex')]"]

    @allure.step('Открыть нужный список с ответами на вопросы')
    def set_drop_down(self, loc_button):
        self.scroll_to_element(loc_button)
        self.wait_clickable(loc_button)
        self.click_element(loc_button)

    @allure.step('Нажать на кнопку Заказать в теле страницы')
    def click_order_button_body(self):
        self.scroll_to_element(self.ORDER_BUTTON_BODY)
        self.wait_clickable(self.ORDER_BUTTON_BODY)
        self.click_element(self.ORDER_BUTTON_BODY)

    @allure.step('Нажать на кнопку заказать в шапке страницы')
    def click_order_button_header(self):
        self.click_element(self.ORDER_BUTTON_HEADER)

    @allure.step('Нажать на кнопку с логотипом сервиса самокат')
    def click_scooter_logo_button(self):
        self.click_element(self.SCOOTER_LOGO_BUTTON)

    @allure.step('Нажать на кнопку с логотипом яндекса')
    def click_yandex_logo_button(self):
        self.click_element(self.YANDEX_LOGO_BUTTON)
