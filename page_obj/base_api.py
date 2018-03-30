#-*-coding:utf-8-*- 
from selenium import webdriver
test_url="https://insurance.chinavanda.com"
driver=webdriver.Firefox()
class Base():
    def __init__(self):
        self.driver=driver
        self.base_url=test_url

    def open(self):
        self.driver.get(self.base_url)
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def back_browser(self):
        self.driver.back()