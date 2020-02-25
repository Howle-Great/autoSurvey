# -*- coding: utf-8 -*-
from .BasicTest import BasicTest
from .pages.LoginPage import LoginPage
from .pages.MainPage import MainPage

from .config import config

import time
import yaml

class MainTest(BasicTest):

	def setUp(self):
		super(MainTest, self).setUp()
		self.read_yaml_file()
		self.login_page = LoginPage(self.driver)
		self.main_page = MainPage(self.driver)
		self.login_page.open()
		self.login_page.sign_in(self.login, self.password, "")
		self.login_page.wait_enter()
		time.sleep(2)
	
	def read_yaml_file(self):
		with open(config.YAML_FILE_PATH) as file:
			documents = yaml.full_load(file)
			self.post_text = documents["post_text"]
			self.message_text = documents["message_text"]
			self.groups = documents["groups"]

	def test_main(self):
		for group in self.groups:
			self.main_page.redirect(group)
			if '404' in self.driver.title:
				continue
			time.sleep(1) 
			self.main_page.write_smart_advertising(self.post_text, self.message_text)
			time.sleep(1)

			