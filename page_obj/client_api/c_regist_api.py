#-*-coding:utf-8-*- 
import time
from page_obj.client_api.c_login_api import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_obj.client_api.c_base_api import *
from selenium import webdriver
class CRegist(CLogin):
    regist_loc=(By.XPATH,"//span[text()='注册账户']")
    new_user=(By.XPATH,"//input[@placeholder='请输入登录账号']")
    new_pwd = (By.XPATH, "//input[@placeholder='请输入登录密码']")
    sure_pwd = (By.XPATH, "//input[@placeholder='请确认登录密码']")
    _introduce=(By.XPATH, "//input[@placeholder='请输入邀请码']")
    regist_=(By.LINK_TEXT,"注 册")
    had_btn = (By.XPATH, "//span[text()='使用已有账户登录']")
    def into_regist(self):
     self.find_element(*self.regist_loc).click()
    def input_newuser(self, username):
        self.find_element(*self.new_user).clear()
        self.find_element(*self.new_user).send_keys(username)
    def input_newpwd(self, pwd):
        self.find_element(*self.new_pwd).clear()
        self.find_element(*self.new_pwd).send_keys(pwd)
    def input_surepwd(self, pwd):
        self.find_element(*self.sure_pwd).clear()
        self.find_element(*self.sure_pwd).send_keys(pwd)
    def input_introduce(self):
        self.find_element(*self._introduce).clear()
        self.find_element(*self._introduce).send_keys(Keys.CONTROL,'v')
    def click_regist(self):
        self.find_element(*self.regist_).click()
    def back_login(self):
     self.find_element(*self.had_btn).click()
    def regist(self,newuser,pwd):
        self.into_regist()
        self.input_newuser(newuser)
        self.input_newpwd(pwd)
        self.input_surepwd(pwd)
        self.input_introduce()
        self.click_regist()
        time.sleep(3)
        try:
            
            self.back_login()
            time.sleep(1)
        except Exception as e:
            pass
if __name__=="__main__":
    driver=webdriver.Firefox()
    url="https://insurance.chinavanda.com/"
    driver.get(url)
    clogin=CLogin(driver)
    clogin.login("god","bhs@mangohm")
    clogin.get_introduce()
    regist=CRegist(driver)
    regist.regist("a12310012","123456")
    regist.regist("a12310013", "123456")












