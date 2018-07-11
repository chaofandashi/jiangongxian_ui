#-*-coding:utf-8-*- 
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest,time
from common.function import *


if __name__ == '__main__':
    # 相对路径的测试用例
    base_path = os.path.realpath(os.path.dirname(__file__))
    test_dir = os.path.join(base_path, 'test_case')
    # 相对路径的测试报告
    report_dir = os.path.join(base_path, 'test_report')
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    now=time.strftime("%Y-%m-%d-%H-%M-%S")
    report_name=report_dir+"\\"+now+'report.html'

    fp=open(report_name,'wb')
    runner=HTMLTestRunner(stream=fp,title="test",description='123')
    runner.run(discover)
    fp.close()

    print ("find the report")
    report=find_new_report(report_dir)
    print ("start send email")
    send_report(report)