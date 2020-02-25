# -*- coding: utf-8 -*-
import os
import unittest
import random
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from .config import config

class BasicTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument("user-data-dir=" + config.CHROME_PROFILE_PATH) #Path to your chrome profile
        if (config.ON_DRIVER):
            print(chrome_options.arguments)
            self.driver = webdriver.Chrome(config.DRIVER, chrome_options=chrome_options)
        else:
            nodeUrl = 'http://localhost:4444/wd/hub'
            self.driver = webdriver.Remote(
                command_executor=nodeUrl,
                desired_capabilities={
                    'browserName': config.BROWSER,
                },
                options=chrome_options
            )

    def tearDown(self):
        self.driver.quit()

    def auth(self):
      pass

    def add_random_number(self, string):
        return string + str(random.randrange(1, 1000000))
