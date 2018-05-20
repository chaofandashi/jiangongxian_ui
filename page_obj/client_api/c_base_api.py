#-*-coding:utf-8-*- 
from selenium import webdriver
url="https://insurance.chinavanda.com/"
# test_url="https://idev.bhsgd.net"
class CBase():
    def __init__(self,drive):
        self.driver=drive
        self.driver.implicitly_wait(10)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def back_browser(self):
        self.driver.back()
