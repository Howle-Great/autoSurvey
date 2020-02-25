from .BasicPage import BasicPage
from selenium.webdriver.common.keys import Keys

class MainPage(BasicPage):
  VK_URL = 'https://vk.com/'
  
  def open(self):
    self.driver.get(self.VK_URL)
