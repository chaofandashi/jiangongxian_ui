#-*-coding:utf-8-*- 
from selenium import webdriver
# test_url="https://insurance.chinavanda.com/"
# test_url="https://idev.bhsgd.net"

class CBase():
    def __init__(self,drive):
        self.driver=drive
        # self.base_url=test_url
        self.driver.implicitly_wait(10)
    # def open(self):
    #     self.driver.get(self.base_url)
    #     self.driver.maximize_window()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def back_browser(self):
        self.driver.back()