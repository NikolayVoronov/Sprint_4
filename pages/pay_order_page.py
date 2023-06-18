from selenium.webdriver.common.by import By
import allure

class PayOrderPage:

    DATE_ORDER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Когда привезти')]"]  # поле когда привезти самокат
    DATE_ORDER_SELECTED = [By.XPATH, ".//div[contains(@class,'datepicker__day--selected')]"]  # выбранная дата
    TIME_ORDER_FILED = [By.XPATH, ".//div[text()='* Срок аренды']"]  # выпадающий список со сроком аренды
    TIME_ORDER_ONE_DAY = [By.XPATH, ".//div[text()='сутки']"]  # кнопка со сроком аренды сутки
    TIME_ORDER_TWO_DAYS = [By.XPATH, ".//div[text()='двое суток']"]  # кнопка со сроком аренды двое суток
    BLACK_COLOR_CHECK_BOX = [By.XPATH, ".//label[contains(@for,'black')]/input"]  # чек-бокс с выбором черного цвета самоката
    GREY_COLOR_CHECK_BOX = [By.XPATH, ".//label[contains(@for,'grey')]/input"]  # чек-бокс с выбором серого цвета самоката
    COMMENTS_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Комментарий')]"]  # поле комментарий курьера
    NEXT_BUTTON_PAY_PAGE = [By.XPATH, ".//div[contains(@class,'1xGrp')]/button[text()='Заказать']"]  # кнопка заказать
    YES_BUTTON = [By.XPATH, ".//div[contains(@class,'1xGrp')]/button[text()='Да']"]  # кнопка да
    SUCCESS_ORDER_FIELD = [By.XPATH, ".//div[text()='Заказ оформлен']"]  # сообщение об успешном заказе
    CHECK_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]  # кнопка посмотреть статус

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вставить дату доставки и подтвердить выбор на календаре')
    def set_date_order(self, date_order):
        self.driver.find_element(*self.DATE_ORDER_FIELD).send_keys(date_order)
        self.driver.find_element(*self.DATE_ORDER_SELECTED).click()

    @allure.step('Выбрать срок аренды на сутки')
    def set_time_order_one_day(self):
        self.driver.find_element(*self.TIME_ORDER_FILED).click()
        self.driver.find_element(*self.TIME_ORDER_ONE_DAY).click()

    @allure.step('Выбрать срок аренды на двое суток')
    def set_time_order_two_days(self):
        self.driver.find_element(*self.TIME_ORDER_FILED).click()
        self.driver.find_element(*self.TIME_ORDER_TWO_DAYS).click()

    @allure.step('Выбрать черный цвет самоката')
    def set_black_color_check_box(self):
        self.driver.find_element(*self.BLACK_COLOR_CHECK_BOX).click()

    @allure.step('Выбрать серый цвет самоката')
    def set_grey_color_check_box(self):
        self.driver.find_element(*self.GREY_COLOR_CHECK_BOX).click()

    @allure.step('Вставить значение в поле комментарий для курьера')
    def set_comments(self, comments):
        self.driver.find_element(*self.COMMENTS_FIELD).send_keys(comments)

    @allure.step('Нажать кнопку далее')
    def click_next_button_pay_page(self):
        self.driver.find_element(*self.NEXT_BUTTON_PAY_PAGE).click()

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
        self.driver.find_element(*self.YES_BUTTON).click()

    @allure.step('Нажать на кнопку посмотреть заказ в модальном окне')
    def click_check_status_button(self):
        self.driver.find_element(*self.CHECK_STATUS_BUTTON).click()
