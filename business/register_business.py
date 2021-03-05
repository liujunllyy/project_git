#coding=utf-8
from handle.register_handle import RegisterHandle

class BusinessRegister(object):
    def __init__(self,driver):
        self.register_h=RegisterHandle(driver)

    def input_search(self,text):
        self.register_h.input_search_text(text)
    
    def click_search(self):
        self.register_h.click_search_button()

    def input_search_error(self,text):
        self.register_h.input_search_text(text)
        get_text=self.register_h.get_user_text('search_error')
        if get_text==text:
            return True
        else:
            return False
        
    def input_search_function(self,text,assertcode):
        self.register_h.input_search_text(text)
        get_text=self.register_h.get_user_text(assertcode)
        if get_text==text:
            return True
        else:
            return False
        