import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager 

@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop_total(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        add_button = driver.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
        add_button.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("101000")
    driver.find_element(By.ID, "continue").click()

    # Получение итоговой суммы
    total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text
    total_value = total_text.split("$")[1]
    assert total_value == "58.29", f"Итоговая сумма {total_value} не равна 58.29"