#-*-coding:utf-8-*- 
from selenium.webdriver.common.by import By
from page_obj.client_api.c_base_api import *
from selenium import webdriver
import time
class CLogin(CBase):
    username_loc=(By.XPATH,"//input[@placeholder='请输入账户名/手机号']")
    password_loc=(By.XPATH,"//input[@placeholder='请输入登录密码']")
    submit_loc=(By.XPATH, "//span[text()='登 录']")
    my_tab=(By.XPATH,"//div[text()='我']")
    introduce=(By.XPATH,"//div[text()='生成内推码']")
    copy_introduce = (By.XPATH,"//button[text()='复制内推码']")
    _logout=(By.XPATH,"//span[text()='退出登录']")
    out_sure = (By.LINK_TEXT, "确定")
    duanyan=(By.XPATH,"//span[text()='广州阳光']")
    def input_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    def input_password(self,pwd):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(pwd)
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
    def login(self,user,pwd):
        self.input_username(user)
        self.input_password(pwd)
        self.click_submit()
    def get_introduce(self):
        time.sleep(0.5)
        self.find_element(*self.my_tab).click()
        self.find_element(*self.introduce).click()
        self.find_element(*self.copy_introduce).click()
        self.back_browser()
        time.sleep(2)
        self.find_element(*self._logout).click()
        self.find_element(*self.out_sure).click()
    def logout(self):
        time.sleep(0.5)
        self.find_element(*self.my_tab).click()
        self.find_element(*self._logout).click()
        time.sleep(0.5)
        self.find_element(*self.out_sure).click()
    def login_sucess(self):
        return self.find_element(*self.duanyan).text
if __name__=="__main__":
    driver=webdriver.Firefox()
    url="https://insurance.chinavanda.com/"
    driver.get(url)
    clogin=CLogin(driver)
    clogin.login("god","bhs@mangohm")
    clogin.get_introduce()
    time.sleep(5)
    driver.quit()