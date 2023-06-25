from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """ Проскролить до нужного элемента """
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    """ Ожидать пока элемент станет кликабельным """
    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    """ Кликнуть по элементу """
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    """ Добавить значение в поле """
    def add_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)
