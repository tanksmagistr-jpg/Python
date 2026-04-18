from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CalculatorPage(BasePage):
    # Локаторы
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        """Установить задержку в секундах"""
        self.input_text(self.DELAY_INPUT, str(seconds))

    def click_seven(self):
        self.click(self.BUTTON_7)

    def click_eight(self):
        self.click(self.BUTTON_8)

    def click_plus(self):
        self.click(self.BUTTON_PLUS)

    def click_equals(self):
        self.click(self.BUTTON_EQUALS)

    def get_result(self):
        from selenium.webdriver.support.ui import WebDriverWait
    wait = WebDriverWait(self.driver, 60)  # ждём до 60 секунд
    wait.until(lambda d: d.find_element(*self.RESULT_SCREEN).text.isdigit())
    return self.get_text(self.RESULT_SCREEN)