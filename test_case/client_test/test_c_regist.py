#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.client_api.c_login_api import *
from page_obj.client_api.c_regist_api import *
import unittest,time

class RegistTest(unittest.TestCase):
    '''注册测试'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.url = "https://insurance.chinavanda.com/"
        cls.driver.get(cls.url)
    @classmethod
    def tearDOwnClass(cls):
        cls.driver.quit()
    def setUp(self):
        time.sleep(1)
        self.username = int(time.time())  # 获取时间戳
    def tearDown(self):
        self.driver.delete_all_cookies()
        time.sleep(1)
    def test_regist1(self):
        '''正常注册'''
        clogin = CLogin(self.driver)
        clogin.login("god", "bhs@mangohm")
        clogin.get_introduce()
        regist = CRegist(self.driver)
        regist.regist(self.username, "123456","123456")
        clogin.login(self.username, "123456")
        try:
            self.assertEqual(clogin.login_sucess(), "广州阳光")
            print(clogin.login_sucess())
            clogin.logout()
        except Exception as e:
            print("截图")
            print(e)
    def test_regist2_error(self):
        '''已用过内推码注册'''
        clogin = CLogin(self.driver)
        clogin.login("god", "bhs@mangohm")
        clogin.get_introduce()
        regist = CRegist(self.driver)
        regist.regist(self.username, "123456","123456")
        regist.regist("a12310015", "123456","123456")
        clogin.login("a12310015", "123456")
        try:
            self.assertEqual(clogin.login_fail(),"用户不存在")
            print(clogin.login_fail())
        except Exception as e:
            print("截图")
            print(e)
    def test_regist3_error(self):
        '''错误内推码注册'''
        regist = CRegist(self.driver)
        regist.regist2(self.username, "123456","123456")
        try:
            print(regist.regist_fail())
            self.assertEqual(regist.regist_fail(),"无效的邀请码")
        except Exception as e:
            print("截图")
            print(e)
        regist.regist2(self.username, "123456", "asd123123qwe")
        try:
            print(regist.regist_fail())
            self.assertEqual(regist.regist_fail(), "无效的邀请码")
        except Exception as e:
            print("截图")
            print(e)
        regist.regist2(self.username, "123456", "!@#!@$#!$#@!@#")
        try:
            print(regist.regist_fail())
            self.assertEqual(regist.regist_fail(), "无效的邀请码")
        except Exception as e:
            print("截图")
            print(e)
        regist.regist2(self.username, "123456", "")
        try:
            print(regist.regist_fail())
            self.assertEqual(regist.regist_fail(), "无效的邀请码")
        except Exception as e:
            print("截图")
            print(e)
    def test_regist4_error(self):
        '''已注册账号注册'''
        clogin = CLogin(self.driver)
        clogin.login("god", "bhs@mangohm")
        clogin.get_introduce()
        regist = CRegist(self.driver)
        regist.regist(self.username, "123456", "123456")
        regist.regist(self.username, "123456", "123456")
        try:
            self.assertEqual(regist.haduser_fail(), "该用户名已注册")
            print(regist.haduser_fail())
        except Exception as e:
            print("截图")
            print(e)
    def test_regist5_error(self):
        '''密码长度小于6位'''
        regist = CRegist(self.driver)
        regist.regist2(self.username, "12345", "12345sadbcdefg123")
        try:
            self.assertEqual(regist.pwdshort_fail(),"密码必须为字符串，长度为6~16，不得含有\ & < >且不可缺省")
            print(regist.pwdshort_fail())
        except Exception as e:
            print("截图")
            print(e)
    def test_regist6_error(self):
        '''密码长度大于16位'''
        regist = CRegist(self.driver)
        regist.regist2(self.username, "123456789abcdefg12s3", "12345sadbcdefg123")
        try:
            self.assertEqual(regist.pwdshort_fail(), "密码必须为字符串，长度为6~16，不得含有\ & < >且不可缺省")
            print(regist.pwdshort_fail())
        except Exception as e:
            print("截图")
            print(e)
    def test_regist7_error(self):
        '''密码为空'''
        regist = CRegist(self.driver)
        regist.regist2(self.username, "", "")
        c_regist = CRegist(self.driver)
        try:
            print(regist.usernull_fail())
            self.assertEqual(regist.usernull_fail(), "注 册")
        except Exception as e:
            print("截图")
            print(e)
    def test_regist8_error(self):
        '''账号为空'''
        regist = CRegist(self.driver)
        regist.regist2("", "123456", "123456")
        try:
            print(regist.usernull_fail())
            self.assertEqual(regist.usernull_fail(), "注 册")
        except Exception as e:
            print("截图")
            print(e)
    def test_regist9_error(self):
        '''账号长度大于16位'''
        regist = CRegist(self.driver)
        regist.regist2("qwerqwerqwer123456", "123456", "qwerqwerqwer123456")
        try:
            time.sleep(3)
            self.assertEqual(regist.usershort_fail(),"用户名必须为字符串，长度为1~16，不得含有\ & < >且不可缺省")
            print(regist.usershort_fail())
        except Exception as e:
            print("截图")
            print(e)
    def test_regist10_error(self):
        '''密码不一致'''
        clogin = CLogin(self.driver)
        clogin.login("god", "bhs@mangohm")
        clogin.get_introduce()
        regist = CRegist(self.driver)
        regist.regist(self.username, "123456", "123465")
        try:
            self.assertEqual(regist.pwd_fail(), "使用已有账户登录")
            print(regist.pwd_fail())
        except Exception as e:
            print("截图")
            print(e)
if __name__ == "__main__":
    unittest.main()