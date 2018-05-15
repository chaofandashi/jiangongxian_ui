#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.client_api.c_login_api import *
import unittest
class Test_Clogin(unittest.TestCase):
    '''登陆测试'''
    def setUp(self):
        1
    def tearDown(self):
        1
    def test_c_login1_normal(self):
        '''正确账号密码登陆'''
        c_login = CLogin()
        c_login.login_action("god", "123456")
        try:
            self.assertEqual(c_login.login_sucess(), "广州阳光")
            print(c_login.login_sucess())
        except Exception as e:
            print("截图")