#coding=utf-8
import sys
sys.path.append('c:/project')
from business.register_business import BusinessRegister
from selenium import webdriver
import HTMLTestRunner
import time
import os

class FirstCase(object):
    def __init__(self,driver):
        self.login=BusinessRegister(driver)

    def test_search_input(self):
        self.login.input_search('123')

    def test_search_click(self):
        self.login.click_search()

if __name__ == "__main__":
    '''
    driver=webdriver.Chrome()
    driver.get("http://passport.takungpao.com/user/register")
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    time.sleep(5)
    FC=FirstCase(driver)
    FC.test_search_input()
    FC.test_search_click()
    driver.close()
    '''
    