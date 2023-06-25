import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):
    """ Локаторы страницы 'Для кого':
    заголовок страницы """
    HEADER_INFO = [By.XPATH, ".//div[contains(@class,'Order_Header__BZXOb')]"]  #
    """ поля имя, фамилия, адрес, станция метро, номер телефона """
    FIRST_NAME_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Имя')]"]  #
    SURNAME_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Фамилия')]"]  #
    ADRESS_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Адрес')]"]  #
    METRO_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Станция метро')]"]  #
    METRO_DROP_DOWN = [By.XPATH, ".//div[contains(@class,'select-search__select')]"]  #
    PHONE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Телефон')]"]  #
    """ кнопка далее """
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]  #

    """ Локаторы страницы 'Про аренду':
    поле когда привезти самокат и выбор даты на календаре """
    DATE_ORDER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Когда привезти')]"]
    DATE_ORDER_SELECTED = [By.XPATH, ".//div[contains(@class,'datepicker__day--selected')]"]
    """ выпадающий список со сроком аренды и выбор вариантов срока аренды """
    TIME_ORDER_FILED = [By.XPATH, ".//div[text()='* Срок аренды']"]
    TIME_ORDER_ONE_DAY = [By.XPATH, ".//div[text()='сутки']"]
    TIME_ORDER_TWO_DAYS = [By.XPATH, ".//div[text()='двое суток']"]
    """ чек-боксы с вариантами цвета """
    BLACK_COLOR_CHECK_BOX = [By.XPATH, ".//label[contains(@for,'black')]/input"]
    GREY_COLOR_CHECK_BOX = [By.XPATH, ".//label[contains(@for,'grey')]/input"]
    """ поле с комментарием к заказу """
    COMMENTS_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Комментарий')]"]
    """ кнопка заказать """
    NEXT_BUTTON_PAY_PAGE = [By.XPATH, ".//div[contains(@class,'1xGrp')]/button[text()='Заказать']"]
    """ кнопка да """
    YES_BUTTON = [By.XPATH, ".//div[contains(@class,'1xGrp')]/button[text()='Да']"]
    """ сообщение об успешном заказе """
    SUCCESS_ORDER_FIELD = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    """ кнопка посмотреть статус """
    CHECK_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]

    @allure.step('Вставить значение в поле имя')
    def set_first_name(self, value):
        self.add_value(self.FIRST_NAME_FIELD, value)

    @allure.step('Вставить значение в поле фамилия')
    def set_surname(self, value):
        self.add_value(self.SURNAME_FIELD, value)

    @allure.step('Вставить значение в поле адрес')
    def set_adress(self, value):
        self.add_value(self.ADRESS_FIELD, value)

    @allure.step('Найти и выбрать станцию метро')
    def set_metro(self, value):
        self.add_value(self.METRO_FIELD, value)
        self.click_element(self.METRO_DROP_DOWN)

    @allure.step('Вставить значение в поле номер телефона')
    def set_phone(self, value):
        self.add_value(self.PHONE_FIELD, value)

    @allure.step('Нажать кнопку далее')
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

    @allure.step('Заполнить все поля с данными и нажать далее')
    def set_user_info(self, first_name, surname, adress, metro, phone):
        self.set_first_name(first_name)
        self.set_surname(surname)
        self.set_adress(adress)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next_button()

    @allure.step('Вставить дату доставки и подтвердить выбор на календаре')
    def set_date_order(self, value):
        self.add_value(self.DATE_ORDER_FIELD, value)
        self.click_element(self.DATE_ORDER_SELECTED)

    @allure.step('Выбрать срок аренды на сутки')
    def set_time_order_one_day(self):
        self.click_element(self.TIME_ORDER_FILED)
        self.click_element(self.TIME_ORDER_ONE_DAY)

    @allure.step('Выбрать срок аренды на двое суток')
    def set_time_order_two_days(self):
        self.click_element(self.TIME_ORDER_FILED)
        self.click_element(self.TIME_ORDER_TWO_DAYS)

    @allure.step('Выбрать черный цвет самоката')
    def set_black_color_check_box(self):
        self.click_element(self.BLACK_COLOR_CHECK_BOX)

    @allure.step('Выбрать серый цвет самоката')
    def set_grey_color_check_box(self):
        self.click_element(self.GREY_COLOR_CHECK_BOX)

    @allure.step('Вставить значение в поле комментарий для курьера')
    def set_comments(self, value):
        self.add_value(self.COMMENTS_FIELD, value)

    @allure.step('Нажать кнопку далее')
    def click_next_button_pay_page(self):
        self.click_element(self.NEXT_BUTTON_PAY_PAGE)

    @allure.step('Заполнить все поля с данными (цвет - черный, срок - сутки) и нажать заказать')
    def set_pay_info_1(self, date_order, comments):
        self.set_date_order(date_order)
        self.set_time_order_one_day()
        self.set_black_color_check_box()
        self.set_comments(comments)
        self.click_next_button_pay_page()

    @allure.step('Заполнить все поля с данными (цвет - серый, срок - двое суток) и нажать заказать')
    def set_pay_info_2(self, date_order, comments):
        self.set_date_order(date_order)
        self.set_time_order_two_days()
        self.set_grey_color_check_box()
        self.set_comments(comments)
        self.click_next_button_pay_page()

    @allure.step('Нажать на кнопку да в модальном окне')
    def click_yes_button(self):
        self.click_element(self.YES_BUTTON)

    @allure.step('Нажать на кнопку посмотреть заказ в модальном окне')
    def click_check_status_button(self):
        self.click_element(self.CHECK_STATUS_BUTTON)

    @allure.step('Найти текст выпадающего списка')
    def find_text_header_info(self):
        return self.find_text(self.HEADER_INFO)

    @allure.step('Найти сообщение об успешном оформлении заказа')
    def find_element_success_order(self):
        return self.find_element(self.SUCCESS_ORDER_FIELD)
