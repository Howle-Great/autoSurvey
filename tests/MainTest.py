# -*- coding: utf-8 -*-
from .BasicTest import BasicTest
from .pages.LoginPage import LoginPage
from .pages.MainPage import MainPage

import time

class MainTest(BasicTest):
  messageText = "Я думаю над новой новостью."
  groups = [
    'https://vk.com/mhkon'
  ]

  def setUp(self):
    super(MainTest, self).setUp()
    self.login_page = LoginPage(self.driver)
    self.main_page = MainPage(self.driver)
    self.login_page.open()
    self.login_page.sign_in(self.login, self.password, "")
    self.login_page.wait_enter()
    # time.sleep(2)

  def test_main(self):
    for group in self.groups:
      self.driver.get(group);
      # time.sleep(1) 
      self.main_page.write_message(self.messageText)
      # time.sleep(1) 
      