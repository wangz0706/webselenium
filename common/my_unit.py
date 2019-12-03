#encoding=utf-8
import unittest
from common.common_fun import Common
from selenium import webdriver

class StartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://ask.testfan.cn/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logger=Common(self.driver).setlog()
        self.logger.info('开始测试')

    def tearDown(self):
        self.logger.info('测试结束')
        self.driver.close()


