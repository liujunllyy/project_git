#coding=utf-8
from page.register_page import RegisterPage
class RegisterHandle(object):
    def __init__(self,driver):
        self.register_p=RegisterPage(driver)
    def input_search_text(self,text):
        self.register_p.get_search_input_elment().send_keys(text)

    def click_search_button(self):
        self.register_p.get_search_button_elment().click()

    def get_user_text(self,info):
        try:
            if info=='search_error':
                text=self.register_p.get_search_error_element().text
            elif info=='name_error':
                pass
        except:
            text= None

        return text