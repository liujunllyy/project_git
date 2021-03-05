#coding=utf-8
from util.read_ini import Read_Ini
class FindElement(object):
    """获取元素所在位置"""
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = Read_Ini()
        data = read_ini.get_value(key)
        by,value = data.split('>')

        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            else:
                return self.driver.find_element_by_css(value)
        except Exception as e:
            # print("find_element错误信息：",e)
            return None