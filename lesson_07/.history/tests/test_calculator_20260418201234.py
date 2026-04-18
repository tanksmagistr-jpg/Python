import pytest
from pages.calculator_page import CalculatorPage

@pytest.mark.usefixtures("chrome_driver")
class TestCalculator:
    def test_slow_calculation(self, chrome_driver):
        # Открыть страницу калькулятора
        calc_page = CalculatorPage(chrome_driver)
        calc_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Установить задержку 45 секунд
        calc_page.set_delay(45)

        # Выполнить вычисление 7 + 8
        calc_page.click_seven()
        calc_page.click_plus()
        calc_page.click_eight()
        calc_page.click_equals()

        # Получить результат (ожидание до 45+ сек)
        result = calc_page.get_result()
        assert result == "15"