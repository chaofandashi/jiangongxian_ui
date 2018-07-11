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
    duanyan=(By.XPATH,"//div[text()='无效的邀请码']")
    duanyan2= (By.XPATH, "//div[text()='该用户名已注册']")
    duanyan3=(By.XPATH, "//div[text()='密码必须为字符串，长度为6~16，不得含有\ & < >且不可缺省']")
    duanyan4 = (By.XPATH, "用户名必须为字符串，长度为1~16，不得含有\ & < >且不可缺省")

    def into_regist(self):
        self.find_element(*self.regist_loc).click()
        log.info("进入注册页面")
    def input_newuser(self, username):
        self.find_element(*self.new_user).clear()
        self.find_element(*self.new_user).send_keys(username)
        log.info("输入注册账号")
    def input_newpwd(self, pwd):
        self.find_element(*self.new_pwd).clear()
        self.find_element(*self.new_pwd).send_keys(pwd)
        log.info("输入注册密码")
    def input_surepwd(self, pwd):
        self.find_element(*self.sure_pwd).clear()
        self.find_element(*self.sure_pwd).send_keys(pwd)
        log.info("确认注册密码")
    def input_introduce(self):
        self.find_element(*self._introduce).clear()
        self.find_element(*self._introduce).send_keys(Keys.CONTROL,'v')
        log.info("复制输入内推码")
    def input_introduce2(self,intro):
        self.find_element(*self._introduce).clear()
        self.find_element(*self._introduce).send_keys(intro)
        log.info("手动输入内推码")
    def click_regist(self):
        self.find_element(*self.regist_).click()
        log.info("开始注册")
    def back_login(self):
        self.find_element(*self.had_btn).click()
        log.info("返回登陆界面")
    def regist(self,newuser,pwd,pwd2):
        self.into_regist()
        self.input_newuser(newuser)
        self.input_newpwd(pwd)
        self.input_surepwd(pwd2)
        self.input_introduce()
        self.click_regist()
        time.sleep(3)
        try:
            self.back_login()
            time.sleep(1)
        except Exception as e:
            pass
        log.info("注册完成")
    def regist2(self,newuser,pwd,intro):
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
            log.info("注册完成")
    def regist_fail(self):
        log.info("注册失败断言")
        log.info("__________end____________")
        return self.find_element(*self.duanyan).text
    def usernull_fail(self):
        log.info("注册失败断言")
        log.info("__________end____________")
        return self.find_element(*self.regist_).text
    def haduser_fail(self):
        log.info("注册失败断言")
        log.info("__________end____________")
        return self.find_element(*self.duanyan2).text
    def pwdshort_fail(self):
        log.info("注册失败断言")
        log.info("__________end____________")
        return self.find_element(*self.duanyan3).text
    def usershort_fail(self):
        log.info("注册失败断言")
        log.info("__________end____________")
        return self.find_element(*self.duanyan4).text
    def pwd_fail(self):
        log.info("注册失败断言")
        log.info("__________end____________")
        return self.find_element(*self.had_btn).text
if __name__=="__main__":
    driver=webdriver.Firefox()
    url="https://insurance.chinavanda.com/"
    driver.get(url)
    clogin=CLogin(driver)
    clogin.login("god","bhs@mangohm")
    clogin.get_introduce()
    regist=CRegist(driver)
    regist.regist("a12310012","123456","123456")
    regist.regist("a12310013", "123456")












