from selenium.webdriver.common.by import By
import allure

class WhoOrderPage:
    HEADER_INFO = [By.XPATH, ".//div[contains(@class,'Order_Header__BZXOb')]"]  # заголовок страницы
    FIRST_NAME_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Имя')]"]  # поле имя
    SURNAME_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Фамилия')]"]  # поле фамилия
    ADRESS_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Адрес')]"]  # поле адреса
    METRO_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Станция метро')]"]  # поле станции метро
    METRO_DROP_DOWN = [By.XPATH, ".//div[contains(@class,'select-search__select')]"]  # список найденных станций метро
    PHONE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Телефон')]"]  # поле номера телефона
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]  # кнопка далее

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вставить значение в поле имя')
    def set_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)

    @allure.step('Вставить значение в поле фамилия')
    def set_surname(self, surname):
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)

    @allure.step('Вставить значение в поле адрес')
    def set_adress(self, adress):
        self.driver.find_element(*self.ADRESS_FIELD).send_keys(adress)

    @allure.step('Найти и выбрать станцию метро')
    def set_metro(self, metro):
        self.driver.find_element(*self.METRO_FIELD).send_keys(metro)
        self.driver.find_element(*self.METRO_DROP_DOWN).click()

    @allure.step('Вставить значение в поле номер телефона')
    def set_phone(self, phone):
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    @allure.step('Нажать кнопку далее')
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step('Заполнить все поля с данными и нажать далее')
    def set_user_info(self, first_name, surname, adress, metro, phone):
        self.set_first_name(first_name)
        self.set_surname(surname)
        self.set_adress(adress)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next_button()
