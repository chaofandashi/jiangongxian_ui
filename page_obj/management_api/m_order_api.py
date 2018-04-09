#-*-coding:utf-8-*-
from page_obj.management_api.m_login_api import *
from selenium.webdriver.common.by import By
import os
class MOrder(BBase):
    driver.implicitly_wait(10)
    check=(By.XPATH,"//div[text()='待审核']")
    payment=(By.XPATH,"//div[text()='待核账']")
    hold_order = (By.XPATH, "//div[text()='待出单']")

    handle = (By.XPATH, "//span[text()='处 理']/parent::button")
    input_=(By.XPATH,"//input[@placeholder='请输入缴费号']")
    pass_=(By.XPATH,"//input[@placeholder='请输入缴费号']/following-sibling::button")#preceding-sibling::  哥哥节点
    img = (By.XPATH, "//input[@type='file']")                                      #parent::             父亲节点
    back_input=(By.XPATH,"//textarea[@placeholder='请输入驳回订单的原因']")           #following-sibling::  弟弟节点
    back_=(By.XPATH,"//span[text()='驳 回']/parent::button")

    has_payment=(By.XPATH,"//span[text()='已到账']/parent::button")
    not_payment=(By.XPATH,"//span[text()='未到账']/parent::button")

    input_num = (By.XPATH, "//input[@placeholder='请输入保单号']")
    issue_=(By.XPATH,"//span[text()='出 单']/parent::button")
    base_path = os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    img_path = os.path.join(base_path, "test_data\\order_img\\")
    # 待核查
    def order_check(self):
        self.find_element(*self.check).click()
        self.find_elements(*self.handle)[0].click()
        self.find_element(*self.input_).send_keys(int(time.time()))
        self.find_element(*self.pass_).click()
    def order_img(self):
        self.find_element(*self.check).click()
        self.find_elements(*self.handle)[0].click()
        self.find_element(*self.input_).send_keys(int(time.time()))
        self.find_element(*self.img).send_keys(self.img_path + '1.png')
        self.find_element(*self.pass_).click()
    def back_order(self):
        self.find_element(*self.check).click()
        self.find_elements(*self.handle)[0].click()
        self.find_element(*self.back_input).send_keys("test打回去回去")
        self.find_element(*self.back_).click()
    # 待核账
    def order_payment(self):
        self.find_element(*self.payment).click()
        self.find_elements(*self.handle)[0].click()
        self.find_element(*self.has_payment).click()
    def payment_back(self):
        self.find_element(*self.payment).click()
        self.find_elements(*self.handle)[0].click()
        self.find_element(*self.not_payment).click()
    # 待出单
    def order_issue(self):
        self.find_element(*self.hold_order).click()
        self.find_elements(*self.handle)[0].click()
        self.find_element(*self.input_num).send_keys(int(time.time()))
        self.find_elements(*self.issue_)[0].click()
    def issue_img(self):
        self.find_element(*self.hold_order).click()
        self.find_elements(*self.handle)[0].click()
        self.find_element(*self.input_num).send_keys(int(time.time()))
        self.find_elements(*self.img)[0].send_keys(self.img_path + '1.png')
        self.find_elements(*self.img)[1].send_keys(self.img_path + '12.png')
        self.find_elements(*self.img)[2].send_keys(self.img_path + '123.png')
        self.find_elements(*self.issue_)[0].click()


if __name__ == '__main__':
    m_login=MLogin()
    m_login.login_action("god","123456")
    m_order=MOrder()
    m_order.issue_img()



