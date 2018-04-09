#-*-coding:utf-8-*- 
import os
import time
from page_obj.client_api.c_login_api import *
from selenium.webdriver.common.by import By
from page_obj.client_api.c_base_api import *

class COrder(CBase):
    order_product = (By.XPATH, "//span[text()='立即投保']")
    name = (By.XPATH, "//input[@placeholder='请填入投保人姓名']")
    id = (By.XPATH, "//input[@placeholder='请输入投保人身份证号码']")
    time = (By.XPATH, "//div[text()='请输入起保时间']")
    sure = (By.XPATH, "//div[text()='确定']")
    select_ = (By.XPATH, "//div[text()='请选择']")
    pro_name = (By.XPATH, "//input[@placeholder='请输入工程名称']")
    loc_name = (By.XPATH, "//input[@placeholder='请输入工程地址']")
    price_j = (By.XPATH, "//input[@placeholder='请输入计费面积']")
    price_p = (By.XPATH, "//input[@placeholder='请输入计费比例']")
    yw_123 = (By.XPATH, "//input[@placeholder='请输入保额']")
    phone = (By.XPATH, "//input[@placeholder='请填写用于发送提醒短信的手机号码']")
    agree = (By.XPATH, "//span[text()='确 定']")
    upload = (By.XPATH, "//span[text()='立即上传']")
    img = (By.XPATH, "//input[@type='file']")
    submint = (By.XPATH,"//span[text()='提交订单']")

    base_path = os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    img_path= os.path.join(base_path,"test_data\\order_img\\")

    def order_buy(self,product_id):
        self.find_elements(*self.order_product)[product_id].click()
        self.find_element(*self.name).send_keys("黄军平")
        self.find_element(*self.id).send_keys("44522419920316155X")
        self.find_element(*self.time).click()
        time.sleep(1)
        self.find_element(*self.sure).click()
        self.find_element(*self.select_).click()
        time.sleep(1)
        self.find_element(*self.sure).click()
        self.find_element(*self.pro_name).send_keys("爱情公寓5")
        self.find_element(*self.loc_name).send_keys("有米科技")
        self.find_element(*self.price_j).send_keys("3000")
        self.find_element(*self.price_p).send_keys("200")
        self.find_elements(*self.yw_123)[0].send_keys("2000")
        self.find_elements(*self.yw_123)[1].send_keys("2000")
        self.find_elements(*self.yw_123)[2].send_keys("2000")
        self.find_element(*self.phone).send_keys("13076220975")
        self.find_element(*self.agree).click()
    def upload_img(self):
        try:
            self.find_element(*self.agree).click()
        except Exception as e:
            pass
        finally:
            time.sleep(1)
            self.find_element(*self.upload).click()
            time.sleep(1)
            self.find_element(*self.img).send_keys(self.img_path + '1.png')
            self.find_element(*self.img).send_keys(self.img_path + '12.png')
            self.find_element(*self.img).send_keys(self.img_path + '123.png')
            self.find_element(*self.img).send_keys(self.img_path + '1234.png')
            self.find_element(*self.img).send_keys(self.img_path + '1235.png')
            self.find_element(*self.img).send_keys(self.img_path + '1234.png')
            time.sleep(1)
            self.find_element(*self.submint).click()

if __name__ == '__main__':
    login=CLogin()
    login.login_action("god","123456")                    # 登录
    c_order=COrder()
    # 0 广州阳光、 1广州人保、 2东莞人保
    c_order.order_buy(0)
    c_order.upload_img()

