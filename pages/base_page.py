import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проскролить до нужного элемента')
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    @allure.step('Ожидать пока элемент станет кликабельным')
    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Добавить значение в поле')
    def add_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Переключиться на открывшуюся вкладку и дождаться её открытия по заголовку')
    def switch_page(self, title):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        WebDriverWait(self.driver, 3).until(EC.title_is(title))

    @allure.step('Открыть нужную страницу')
    def go_to_site(self, url):
        self.driver.get(url)

    @allure.step('Найти текст элемента')
    def find_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Проверить адрес страницы')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Найти нужный элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)
