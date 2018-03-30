#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.login_api import *
from page_obj.base_api import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class Regist(Base):
    my_tab = (By.XPATH, "//div[text()='我']")
    get_introduce=(By.XPATH,"//div[text()='生成内推码']")
    copy_introduce=(By.XPATH,"//button[text()='复制内推码']")
    introduce_into = (By.XPATH, "//input[@placeholder='请输入邀请码']")
    regist_=(By.XPATH, "//span[text()='注册账户']")
    username =(By.XPATH, "//input[@placeholder='请输入登录账号']")
    password =(By.XPATH, "//input[@placeholder='请输入登录密码']")
    password2 = (By.XPATH, "//input[@placeholder='请确认登录密码']")

    def introduce_action(self):
        self.find_element(*self.my_tab).click()
        self.find_element(*self.get_introduce).click()
        self.find_element(*self.copy_introduce).click()
    def into_regist(self):
        self.find_element(*self.regist_).click()
    def type_username(self,username):
        self.find_element(*self.username).clear()
        self.find_element(*self.username).send_keys(username)
    def type_password(self, pwd):
        self.find_element(*self.password).send_keys(pwd)
    def type_password2(self, pwd2):
        self.find_element(*self.password).send_keys(pwd2)
    def regist_action(self,username,pwd,pwd2):
        self.type_username(username)
        self.type_password(pwd)
        self.type_password2(pwd2)
        self.send_introduce()
    def send_introduce(self):
        self.find_element(*self.introduce_into).send_keys(Keys.CONTROL,'v')

if __name__ == '__main__':
    login=Login()
    login.login_action("god","123456")
    regist=Regist()
    regist.introduce_action()
    time.sleep(1)
    # 后退
    regist.back_browser()
    # 退出登录
    login.logout_action()
    # 确认退出
    login.logout_sure()
    # 进入注册页面
    regist.into_regist()






