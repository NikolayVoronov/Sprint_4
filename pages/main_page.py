from selenium.webdriver.common.by import By
import allure
import time

class MainPage:
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

    """Кнопка заказать в теле станицы"""
    ORDER_BUTTON_BODY = [By.XPATH, ".//div[contains(@class,'Home_FinishButton__1_cWm')]/button"]

    """ Поле с информацией о сервисе """
    INFO_SCOOTER_FIELD = [By.XPATH, ".//div[text()='Привезём его прямо к вашей двери,']"]

    def __init__(self, driver):
        self.driver = driver

    """ set_drop_down_* - методы активируют выпадающие списки с ответами на вопросы """

    @allure.step('Открыть список со стоимостью оплаты и проверить текст')
    def set_drop_down_cost(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_COST))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_COST).click()

    @allure.step('Открыть список с количеством самокатов и проверить текст')
    def set_drop_down_several_scooters(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_SEVERAL_SCOOTERS))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_SEVERAL_SCOOTERS).click()

    @allure.step('Открыть список с временем аренды оплаты и проверить текст')
    def set_drop_down_time_cost(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_TIME_COST))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_TIME_COST).click()

    @allure.step('Открыть список с возможность оформления заказа сегодня и проверить текст')
    def set_drop_down_order_today(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_ORDER_TODAY))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_ORDER_TODAY).click()

    @allure.step('Открыть список с возможностью продления или возврата раньше и проверить текст')
    def set_drop_down_change_order(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_CHANGE_ORDER))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_CHANGE_ORDER).click()

    @allure.step('Открыть список с зарядкой и проверить текст')
    def set_drop_down_charger(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_CHARGER))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_CHARGER).click()

    @allure.step('Открыть список с возможностью отмены заказа и проверить текст')
    def set_drop_down_cancel_order(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_CANCEL_ORDER))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_CANCEL_ORDER).click()

    @allure.step('Открыть список с доставкой за МКАД и проверить текст')
    def set_drop_down_mkad(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.DROP_DOWN_MKAD))
        time.sleep(1)
        self.driver.find_element(*self.DROP_DOWN_MKAD).click()

    @allure.step('Нажать на кнопку Заказать в теле страницы')
    def click_order_button_body(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.ORDER_BUTTON_BODY))
        self.driver.find_element(*self.ORDER_BUTTON_BODY).click()
