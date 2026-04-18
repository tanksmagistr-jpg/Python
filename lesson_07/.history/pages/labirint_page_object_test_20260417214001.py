from selenium import webdriver
from selenium.webdriver.common.by import By

cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome()


def test_cart_counter():
  open_labirint()  # Открываем сайт
  search("Python")  # Ищем книги по слову
  added = add_books()  # Добавляем книги и сохраняем результат в переменную
  go_to_cart()  # Идем в корзину
  cart_counter = get_cart_counter()  # Забираем значение счетчика из корзины
  close_driver()  # закрываем браузер

  assert added == cart_counter  # Сравниваем counter со счетчиком корзины