# -*- coding: utf-8 -*-
from .BasicTest import BasicTest
from .pages.LoginPage import LoginPage
from .pages.MainPage import MainPage

import time

class MainTest(BasicTest):
	messageText = "Я думаю над новой новостью."
	groups = [
		'https://vk.com/overhear_dmitrov1',
		'https://vk.com/aboutphoto'
	]

	def setUp(self):
		super(MainTest, self).setUp()
		self.login_page = LoginPage(self.driver)
		self.main_page = MainPage(self.driver)
		self.login_page.open()
		self.login_page.sign_in(self.login, self.password, "")
		self.login_page.wait_enter()
		time.sleep(2)
		# self.main()

	def test_main(self):
		for group in self.groups:
			self.main_page.redirect(group)
			if '404' in self.driver.title:
				continue
			time.sleep(1) 
			# self.main_page.write_message(self.messageText)
			self.main_page.write_post(self.messageText)
			time.sleep(1)

			