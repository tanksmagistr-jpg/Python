from pages.calculator_page import CalculatorPage


class TestCalculator:
    def test_slow_calculation(self, chrome_driver):
        # Открыть страницу калькулятора
        calc_page = CalculatorPage(chrome_driver)
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        calc_page.open(url)

        # Установить задержку 45 секунд
        calc_page.set_delay(45)

        # Выполнить вычисление 7 + 8
        calc_page.click_seven()
        calc_page.click_plus()
        calc_page.click_eight()
        calc_page.click_equals()

        # Получить результат
        result = calc_page.get_result()
        assert result == "15"
