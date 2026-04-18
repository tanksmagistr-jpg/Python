from time import sleep
from selenium import webdriver

cookie = {"name": "cookie_policy", "value": "1"}

def test_card_counter():
  browser = webdriver.Chrome()

  # Перейти на сайт «Лабиринта»
  browser.get("https://www.labirint.ru/")
  browser.implicitly_wait(4)
  browser.maximize_window()
  browser.add_cookie(cookie)

  sleep(5)
  browser.quit()

  browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('')
  # Найти все книги по слову Python
  browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
  # Добавить все книги в корзину и посчитать
  # Перейти в корзину
  # Проверить счетчик товаров

  