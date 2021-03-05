#coding=utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd=FindElement(driver)

    def get_search_input_elment(self):
        return self.fd.get_element("search_input")

    def get_search_button_elment(self):
        return self.fd.get_element("search_button")

    def get_search_error_element(self):
        return self.fd.get_element("search_input")
