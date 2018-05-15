#-*-coding:utf-8-*- 
from selenium import webdriver
import unittest
import time
class Staer_End(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.username = int(time.time())  # 获取时间戳
    def tearDown(self):
        self.driver.quit()