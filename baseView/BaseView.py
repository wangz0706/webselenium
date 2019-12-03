#encoding=utf-8
from selenium import webdriver

class BaseView(object):
    def __init__(self,driver):
        self.driver=driver


    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

# if __name__ == '__main__':
#     b = BaseView()