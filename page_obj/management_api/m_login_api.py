#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_obj.management_api.m_base_api import *
import time

class MLogin(BBase):
    username_loc = (By.XPATH,"//input[@placeholder='请输入账户名/手机号']")
    password_loc = (By.XPATH,"//input[@placeholder='请输入登录密码']")
    submit = (By.XPATH, "//button[@type='button']")
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)
    def type_submit(self):
        self.find_element(*self.submit).click()
    def login_action(self,user,psd):
        self.open()
        self.type_username(user)
        self.type_password(psd)
        self.type_submit()
    def logout_action(self):
        1
        # self.find_element(*self.my_tab).click()
        # self.find_element(*self.logout).click()
    def logout_sure(self):
        1
        # self.find_element(*self.out_sure).click()

if __name__ == '__main__':
    m_login=MLogin()
    m_login.login_action("god","123456")
