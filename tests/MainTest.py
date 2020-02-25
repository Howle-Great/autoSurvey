# -*- coding: utf-8 -*-
from .BasicTest import BasicTest
from .pages.MainPage import MainPage

import time

class MainTest(BasicTest):

  def setUp(self):
    super(MainTest, self).setUp()
    self.main_page = MainPage(self.driver)
    self.main_page.open()

  def test_main(self):
    time.sleep(500)