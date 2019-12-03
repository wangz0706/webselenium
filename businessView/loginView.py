#encoding=utf-8
from baseView import BaseView
from common.common_fun import Common
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium import webdriver

class LoginView(Common):
    loginbutton=(By.LINK_TEXT,u"登录")
    user=(By.NAME,"email")
    password=(By.NAME,"password")
    login=(By.TAG_NAME,"button")
    # login=(By.CLASS_NAME,"btn btn-primary pull-right pl20 pr20")定位不到
    checklogin=(By.ID,"unread_messages")
    newer=(By.CSS_SELECTOR,'.dropdown.user-avatar')
    setting=(By.LINK_TEXT,u"账号设置")
    name=(By.NAME,'name')
    gender=(By.NAME,"gender")
    birthday=(By.ID,"birthday")
    province=(By.ID,"province")
    city=(By.ID,"city")
    submit=(By.CSS_SELECTOR,".btn.btn-xl.btn-primary.profile-sub")
    logout=(By.LINK_TEXT,u"退出")
    qqlogin=(By.CLASS_NAME,"icon-sn-bg-qq")
    frame=(By.ID,"ptlogin_iframe")
    touxiang=(By.ID,"img_out_1113571834")




    def login_action(self):
        self.setlog().info('start')
        # self.logger.info('start login')
        self.driver.find_element(*self.loginbutton).click()
        self.driver.find_element(*self.user).clear()
        self.driver.find_element(*self.user).send_keys('15254587271@163.com')
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys('3739157abc')
        self.driver.find_element(*self.login).click()

    def check_login(self):
        try:
            sleep(4)
            ele=self.driver.find_element(*self.checklogin)
        except NoSuchElementException:
            self.setlog().info('login fail')
            self.getScreenshot('login fail')
            return False
        else:
            self.setlog().info('login sucess')
            return True














#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("http://ask.testfan.cn/")
#     l=LoginView(driver)
#     l.login_action()
#     l.check_login()
#     l.alert_set()



