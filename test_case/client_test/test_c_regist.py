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
        regist.regist(self.username, "123456")
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
        regist.regist(self.username, "123456")
        regist.regist("a12310015", "123456")
        try:
            time.sleep(3)
            self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
            print(c_regist.regist_sucess())
            c_regist.back_login()
        except Exception as e:
            print("截图")
            print(e)
    def test_regist3_error(self):
        '''错误内推码注册'''
        c_regist = CRegist(self.driver)
        c_regist.ready_action()
        c_regist.error_introduce(self.username, "123456", "123456","123456")
        try:
            time.sleep(3)
            print(c_regist.regist_sucess())
            self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
        except Exception as e:
            print("截图")
            print(e)
        c_regist.error_introduce(self.username, "123456", "123456", "asd123123qwe")
        try:
            time.sleep(3)
            c_regist.regist_sucess()
            print(c_regist.regist_sucess())
            self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
        except Exception as e:
            print("截图")
            print(e)
        c_regist.error_introduce(self.username, "123456", "123456", "!@#!@$#!$#@!@#")
        try:
            time.sleep(3)
            c_regist.regist_sucess()
            print(c_regist.regist_sucess())
            self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
        except Exception as e:
            print("截图")
            print(e)
        c_regist.error_introduce(self.username, "123456", "123456", "")
        try:
            time.sleep(3)
            c_regist.regist_sucess()
            self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
            print(c_regist.regist_sucess())
            c_regist.back_login()
        except Exception as e:
            print("截图")
            print(e)
    def test_regist4_error(self):
        '''已注册账号注册'''
        c_login = CLogin(self.driver)
        c_login.login_action("god", "123456")
        c_login = CLogin(self.driver)
        c_login.login_action("god", "123456")
        c_regist = CRegist(self.driver)
        c_regist.ready_action()
        c_regist.regist_action("god", "123456", "123456")
        try:
            time.sleep(3)
            self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
            print(c_regist.regist_sucess())
            c_regist.back_login()
        except Exception as e:
            print("截图")
            print(e)
    # def test_regist5_error(self):
    #     '''密码长度小于6位'''
    #     c_login = CLogin(self.driver)
    #     c_login.login_action("god", "123456")
    #     c_regist = CRegist(self.driver)
    #     c_regist.ready_action()
    #     c_regist.regist_action("qq275769643", "12345", "12345")
    #     try:
    #         time.sleep(3)
    #         self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
    #         print(c_regist.regist_sucess())
    #         c_regist.back_login()
    #     except Exception as e:
    #         print("截图")
    #         print(e)
#     def test_regist6_error(self):
#         '''密码长度大于16位'''
#         c_login = CLogin(self.driver)
#         c_login.login_action("god", "123456")
#         c_regist = CRegist(self.driver)
#         c_regist.ready_action()
#         c_regist.regist_action("qq275769643", "123456789abcdefg123", "123456789abcdefg123")
#         try:
#             time.sleep(3)
#             self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
#             print(c_regist.regist_sucess())
#             c_regist.back_login()
#         except Exception as e:
#             print("截图")
#             print(e)
#     def test_regist7_error(self):
#         '''密码为空'''
#         c_login = CLogin(self.driver)
#         c_login.login_action("god", "123456")
#         c_regist = CRegist(self.driver)
#         c_regist.ready_action()
#         c_regist.regist_action("qq275769643", "", "")
#         try:
#             time.sleep(3)
#             self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
#             print(c_regist.regist_sucess())
#         except Exception as e:
#             print("截图")
#             print(e)
#     def test_regist8_error(self):
#         '''账号为空'''
#         c_login = CLogin(self.driver)
#         c_login.login_action("god", "123456")
#         c_regist = CRegist(self.driver)
#         c_regist.ready_action()
#         c_regist.regist_action("", "123456", "123456")
#         try:
#             time.sleep(3)
#             self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
#             print(c_regist.regist_sucess())
#             c_regist.back_login()
#         except Exception as e:
#             print("截图")
#             print(e)
#     def test_regist9_error(self):
#         '''账号长度大于16位'''
#         c_login = CLogin(self.driver)
#         c_login.login_action("god", "123456")
#         c_regist = CRegist(self.driver)
#         c_regist.ready_action()
#         c_regist.regist_action("qwerqwerqwer123456", "123456", "123456")
#         try:
#             time.sleep(3)
#             self.assertEqual(c_regist.regist_sucess(),"使用已有账户登录")
#             print(c_regist.regist_sucess())
#             c_regist.back_login()
#         except Exception as e:
#             print("截图")
#             print(e)
#     def test_regist10_error(self):
#         '''密码不一致'''
#         c_login = CLogin(self.driver)
#         c_login.login_action("god", "123456")
#         c_regist = CRegist(self.driver)
#         c_regist.ready_action()
#         c_regist.regist_action("qwerqwerqwer123456", "123456", "abcdef")
#         try:
#             time.sleep(3)
#             self.assertEqual(c_regist.regist_sucess(), "使用已有账户登录")
#             print(c_regist.regist_sucess())
#             c_regist.back_login()
#         except Exception as e:
#             print("截图")
#             print(e)
if __name__ == "__main__":
    unittest.main()