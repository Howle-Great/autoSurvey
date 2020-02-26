# -*- coding: utf-8 -*-
from .BasicTest import BasicTest
from .pages.LoginPage import LoginPage
from .pages.MainPage import MainPage

from .config import config

import yaml
import time

class MainTest(BasicTest):
	blocked_group = "#content .groups_blocked_about"
		
	counter_publishers = 0
	blocked_pages = []
	error_pages = []

	def setUp(self):
		super(MainTest, self).setUp()
		self.read_yaml_file()
		self.login_page = LoginPage(self.driver)
		self.main_page = MainPage(self.driver)
		self.login_page.open()
		self.login_page.sign_in(self.login, self.password, "")
		self.login_page.wait_enter()
	
	def show_statistick(self):
		counter_blocked_pages = len(self.blocked_pages)
		counter_error_pages = len(self.error_pages)
		print(f'Statistick: \nPublished: {self.counter_publishers}\nBlocked pages: {counter_blocked_pages}\nError pages: {counter_error_pages}\n')

	def read_yaml_file(self):
		with open(config.YAML_FILE_PATH) as file:
			documents = yaml.full_load(file)
			self.post_text = documents["post_text"]
			self.message_text = documents["message_text"]
			self.groups = documents["groups"]
	 
	def rewrite_yaml_file(self):
		yaml_file = {
			'message_text': self.message_text,
			'post_text': self.post_text,
			'groups': self.groups,
			'blocked_pages': self.blocked_pages,
			'error_pages': self.error_pages
		}
		with open(config.YAML_FILE_PATH, 'w') as file:
			document = yaml.dump(yaml_file, file, allow_unicode=True, sort_keys=False)

	def test_main(self):
		UNBLOCKING_TIME = 60
		BLOCKING_TIMES_NUMBER = 20
		times_counter = 1 #counts the number of shipments
		start_time = time.time()
		for group in self.groups[:]:
			self.main_page.redirect(group)
			if self.driver.find_elements_by_css_selector(self.blocked_group):
				if self.driver.find_elements_by_css_selector(self.blocked_group)[0].is_displayed():
					self.blocked_pages.append(group)
					self.groups.remove(group)
					continue
			if '404' in self.driver.title:
				self.error_pages.append(group)
				self.groups.remove(group)
				continue
			self.main_page.write_smart_advertising(self.post_text, self.message_text)
			self.counter_publishers += 1
			times_counter += 1
			# rescue bot from blocking with google captcha
			if times_counter == BLOCKING_TIMES_NUMBER:
				times_counter = 1
				if time.time() - start_time < UNBLOCKING_TIME:
					time.sleep(UNBLOCKING_TIME - (time.time() - start_time))
					start_time = 0
	 
		self.show_statistick()
		self.rewrite_yaml_file()

			