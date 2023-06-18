from selenium.webdriver.common.by import By
import allure

class BasePage:
    """Кнопка заказать в шапке станицы"""
    ORDER_BUTTON_HEADER = [By.XPATH, ".//div[contains(@class,'Header_Nav__AGCXC')]/button[text()='Заказать']"]
    """Кнопка с логотипом сервиса самокат"""
    SCOOTER_LOGO_BUTTON = [By.XPATH, ".//a[contains(@class,'Header_LogoScooter')]"]
    """Кнопка с логотипом яндекса"""
    YANDEX_LOGO_BUTTON = [By.XPATH, ".//a[contains(@class,'Header_LogoYandex')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на кнопку заказать в шапке страницы')
    def click_order_button_header(self):
        self.driver.find_element(*self.ORDER_BUTTON_HEADER).click()

    @allure.step('Нажать на кнопку с логотипом сервиса самокат')
    def click_scooter_logo_button(self):
        self.driver.find_element(*self.SCOOTER_LOGO_BUTTON).click()

    @allure.step('Нажать на кнопку с логотипом яндекса')
    def click_yandex_logo_button(self):
        self.driver.find_element(*self.YANDEX_LOGO_BUTTON).click()
