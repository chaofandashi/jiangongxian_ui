#-*-coding:utf-8-*- 
from selenium.webdriver.common.by import By
from page_obj.client_api.c_base_api import *
from selenium import webdriver
class CLogin(CBase):
    username_loc=(By.XPATH,"//input[@placeholder='请输入账户名/手机号']")
    password_loc=(By.XPATH,"//input[@placeholder='请输入登录密码']")
    submit = (By.XPATH, "//span[text()='登 录']")
    my_tab = (By.XPATH, "//div[text()='我']")
    logout = (By.XPATH,"//span[text()='退出登录']")
    out_sure= (By.LINK_TEXT,"确定")
    pass_logo=(By.XPATH, "//span[text()='广州阳光']")

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)
    def type_submit(self):
        self.find_element(*self.submit).click()
    def login_action(self,user,psd):
        # self.open()
        self.type_username(user)
        self.type_password(psd)
        self.type_submit()
    def logout_action(self):
        self.find_element(*self.my_tab).click()
        self.find_element(*self.logout).click()
    def logout_sure(self):
        self.find_element(*self.out_sure).click()
    def login_sucess(self):
        return self.find_element(*self.pass_logo).text

if __name__ == '__main__':
    driver=webdriver.Firefox()
    url="https://insurance.chinavanda.com/"
    driver.get(url)
    c_login=CLogin(driver)
    c_login.login_action("god","123456")
