#-*-coding:utf-8-*- 
import time
from page_obj.client_api.c_login_api import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_obj.client_api.c_base_api import *
from selenium import webdriver
class CRegist(CLogin):
    my_tab = (By.XPATH, "//div[text()='我']")
    get_introduce=(By.XPATH,"//div[text()='生成内推码']")
    copy_introduce=(By.XPATH,"//button[text()='复制内推码']")
    introduce_into = (By.XPATH, "//input[@placeholder='请输入邀请码']")
    regist_=(By.XPATH, "//span[text()='注册账户']")
    username =(By.XPATH, "//input[@placeholder='请输入登录账号']")
    password =(By.XPATH, "//input[@placeholder='请输入登录密码']")
    password2 = (By.XPATH, "//input[@placeholder='请确认登录密码']")
    regist_c=(By.XPATH, "//span[text()='注 册']")
    duanyan=(By.XPATH, "//span[text()='使用已有账户登录']")
    had_btn = (By.XPATH, "//span[text()='使用已有账户登录']")
    # back_=(By.XPATH, "//span[@class='am-navbar-left-icon']/svg")
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
        self.find_element(*self.password).clear()
        self.find_element(*self.password).send_keys(pwd)
    def type_password2(self, pwd2):
        self.find_element(*self.password2).clear()
        self.find_element(*self.password2).send_keys(pwd2)
    # def type_back(self):
    #     self.find_element(*self.back_).click()
    def ready_action(self):
        self.introduce_action()
        self.back_browser()
        time.sleep(1)
        self.logout_action()
        time.sleep(1)
        self.logout_sure()
        self.into_regist()
    def regist_action(self,username,pwd,pwd2):
        try:
            self.into_regist()
        except Exception as e:
            pass
        finally:
            self.type_username(username)
            self.type_password(pwd)
            self.type_password2(pwd2)
            self.send_introduce()
            self.click_regist()
    def error_introduce(self,username,pwd,pwd2,introduce):
        try:
            self.into_regist()
        except Exception as e:
            pass
        finally:
            self.type_username(username)
            self.type_password(pwd)
            self.type_password2(pwd2)
            self.find_element(*self.introduce_into).clear()
            self.find_element(*self.introduce_into).send_keys(introduce)
            self.click_regist()
    def send_introduce(self):
        self.find_element(*self.introduce_into).clear()
        self.find_element(*self.introduce_into).send_keys(Keys.CONTROL,'v')
    def click_regist(self):
        self.find_element(*self.regist_c).click()
    def regist_sucess(self):
        return self.find_element(*self.duanyan).text
    def back_login(self):
        self.find_element(*self.had_btn).click()
if __name__ == '__main__':
    driver = webdriver.Firefox()
    url = "https://insurance.chinavanda.com/"
    driver.get(url)
    login=CLogin(driver)
    login.login_action("god","123456")                    # 登录
    c_regist=CRegist(driver)
    c_regist.ready_action()                                 # 注册账号密码
    c_regist.regist_action("qq11001102","123456","123456")
    # time.sleep(2)
    # c_regist.regist_action("qq11001100", "123456", "123456")
    login.login_action("qq11001102","123456")                # 使用注册账号登录
    time.sleep(2)
    driver.quit()






