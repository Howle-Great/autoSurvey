from .BasicPage import BasicPage
from selenium.webdriver.common.keys import Keys

class LoginPage(BasicPage):
  login_input_elem = 'input[name="email"]'
  password_input_elem = 'input[name="pass"]'
  news_object = '#submit_post_box'

  def login_input(self, type):
    if type == "dark":
      elem = "#quick_email"
    else:
      elem = "#index_email"
    return elem
  
  def password_input(self, type):
    if type == "dark":
      elem = "#quick_pass"
    else:
      elem = "#index_pass"
    return elem
    
  def next_button(self, type):
    if type == "dark":
      elem = '#quick_login_button'
    else:
      elem = '#index_login_button'
    return elem

  def open(self):
    self.driver.get(self.VK_URL)

  def enter_login(self, login, type):
    elem = self.wait_render(self.login_input(type))
    elem.send_keys(login)

  def clear_login(self, type):
    elem = self.wait_render(self.login_input(type))
    length = len(elem.get_attribute('value'))
    for _ in range(length):
      elem.send_keys(Keys.BACKSPACE)

  def enter_password(self, login, type):
    elem = self.wait_render(self.password_input(type))
    elem.send_keys(login)

  def click_next(self, type):
    elem = self.wait_render(self.next_button(type))
    elem.click()

  def sign_in(self, login, password, type):
    self.wait_render(self.login_input(type))
    self.clear_login(type)
    self.enter_login(login, type)
    self.enter_password(password, type)
    self.click_next(type)
  
  def wait_enter(self):
    self.wait_render(self.news_object, 240)