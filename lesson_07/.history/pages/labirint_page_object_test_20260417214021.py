from selenium import webdriver
from selenium.webdriver.common.by import By

cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome()


def test_cart_counter():
