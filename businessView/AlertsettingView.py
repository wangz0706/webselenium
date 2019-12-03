# encoding=utf-8
from baseView import BaseView
from common.common_fun import Common
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium import webdriver


class SettingView(Common):
    loginbutton = (By.LINK_TEXT, u"登录")
    login = (By.TAG_NAME, "button")
    # login=(By.CLASS_NAME,"btn btn-primary pull-right pl20 pr20")定位不到
    checklogin = (By.ID, "unread_messages")
    newer = (By.CSS_SELECTOR, '.dropdown.user-avatar')
    setting = (By.LINK_TEXT, u"账号设置")
    name = (By.NAME, 'name')
    gender = (By.NAME, "gender")
    birthday = (By.ID, "birthday")
    province = (By.ID, "province")
    city = (By.ID, "city")
    submit = (By.CSS_SELECTOR, ".btn.btn-xl.btn-primary.profile-sub")
    logout = (By.LINK_TEXT, u"退出")
    qqlogin = (By.CLASS_NAME, "icon-sn-bg-qq")
    frame = (By.ID, "ptlogin_iframe")
    touxiang = (By.ID, "img_out_1113571834")


    def third_partlogin(self):
        # 三方登录，切换frame
        self.driver.find_element(*self.loginbutton).click()
        self.driver.find_element(*self.qqlogin).click()
        changeframe = self.driver.find_element(*self.frame)
        self.driver.switch_to.frame(changeframe)
        self.driver.find_element(*self.touxiang).click()


    def check_login(self):
        try:
            sleep(4)
            ele = self.driver.find_element(*self.checklogin)
        except NoSuchElementException:
            self.setlog().info('login fail')
            self.getScreenshot('login_fail')
            return False
        else:
            self.setlog().info('login sucess')
            return True

    def alert_set(self):
        self.driver.find_element(*self.newer).click()
        self.driver.find_element(*self.setting).click()
        self.driver.find_element(*self.name).clear()
        self.driver.find_element(*self.name).send_keys('测试selenium')
        genders = self.driver.find_elements(*self.gender)
        for g in genders:
            if (not g.is_selected()):
                sleep(2)
                g.click()
                break
        # 使用js来取消输入框的点击绑定事件，然后再输入，实现生日日期输入
        js = "$('#birthday').unbind()"
        self.driver.execute_script(js)

        self.driver.find_element(*self.birthday).clear()
        self.driver.find_element(*self.birthday).send_keys('2018-11-01')
        # 选择省份和市   使用Select模块
        s = Select(self.driver.find_element(*self.province))
        s.select_by_index(28)
        sleep(2)
        t = Select(self.driver.find_element(*self.city))
        t.select_by_visible_text('成都')

        self.driver.find_element(*self.submit).click()
        sleep(3)
        self.driver.find_element(*self.newer).click()
        self.driver.find_element(*self.logout).click()
        sleep(2)


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get("http://ask.testfan.cn/")
#     driver.maximize_window()
#     l=SettingView(driver)
#     l.third_partlogin()
#     l.check_login()
#     l.alert_set()


