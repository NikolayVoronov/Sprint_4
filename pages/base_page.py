from selenium.webdriver.common.by import By

class InfoOrderPage:
    SCOOTER_LOGO_BUTTON = [By.XPATH, ".//a[contains(@class,'Header_LogoScooter')]"] # кнопка с логотипом сервиса самокат

    def __init__(self, driver):
        self.driver = driver

    """ Нажать на кнопку с логотипом сервиса самокат """
    def click_scooter_logo_button(self):
        self.driver.find_element(*self.SCOOTER_LOGO_BUTTON).click()
