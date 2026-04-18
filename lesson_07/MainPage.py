class MainPage:

  def __init__(self, driver): 
      self._driver = driver
      self._driver.get("https://www.labirint.ru/")
      self._driver.implicitly_wait(4)
      self._driver.maximize_window()

  def set_cookie_policy(self):
      cookie = {
      "name": "cookie_policy",
      "value": "1"
      }
      self._driver.add_cookie(cookie)