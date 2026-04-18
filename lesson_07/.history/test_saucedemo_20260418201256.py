import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("firefox_driver")
class TestSauceDemo:
    def test_total_price(self, firefox_driver):
        # Открыть сайт магазина
        login_page = LoginPage(firefox_driver)
        login_page.open("https://www.saucedemo.com/")

        # Авторизация
        login_page.login("standard_user", "secret_sauce")

        # Добавление товаров
        inventory_page = InventoryPage(firefox_driver)
        inventory_page.add_backpack()
        inventory_page.add_bolt_tshirt()
        inventory_page.add_onesie()

        # Переход в корзину и checkout
        inventory_page.go_to_cart()
        cart_page = CartPage(firefox_driver)
        cart_page.proceed_to_checkout()

        # Заполнение формы (замените на свои данные)
        checkout_page = CheckoutPage(firefox_driver)
        checkout_page.fill_customer_info("Ivan", "Petrov", "123456")

        # Чтение итоговой суммы
        total_text = checkout_page.get_total()  # "Total: $58.29"
        # Извлечение числа из строки
        total_value = total_text.split("$")[1]
        assert total_value == "58.29"