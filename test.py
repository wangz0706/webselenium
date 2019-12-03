#encoding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://ask.testfan.cn/')
driver.implicitly_wait(4)
driver.maximize_window()

# By报错需调试？？？
# login=(By.NAME,"email")
driver.find_element_by_link_text('登录').click()
# driver.find_element(login).clear()  这样表示报错？？
driver.find_element(By.NAME,"email").clear()
driver.find_element(By.NAME,"email").send_keys('15254587271@163.com')
# driver.find_element_by_xpath("//input[@name='email']").clear()
# driver.find_element_by_xpath("//input[@name='email']").send_keys('15254587271@163.com')


driver.find_element_by_css_selector("[name='password']").clear()
driver.find_element_by_css_selector("[name='password']").send_keys('3739157abc')
driver.find_element_by_css_selector('.btn.btn-primary').click()


driver.close()

