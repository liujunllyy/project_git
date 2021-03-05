#coding=utf-8
import ddt
import sys
sys.path.append('c:/project')
from business.register_business import BusinessRegister
from selenium import webdriver
import time
import unittest
import os
import HTMLTestRunner
from util.excel_uti import ExcelUti
ex=ExcelUti()
data=ex.get_data()
@ddt.ddt
class FirstDdtTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        time.sleep(2)
        self.login=BusinessRegister(self.driver)

    def tearDown(self):
        # if sys.exc_info()[0]:  ptthon 2 处理
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.getcwd()+'/report/'+case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
        
    '''
    @ddt.data(
        ['text','search_error'],
        ['aaa','search_error']
    )

    @ddt.unpack
    '''

    @ddt.data(*data)
    def test_search_input(self,data):
        text,assertcode=data
        text=self.login.input_search_function(text,assertcode)
        return self.assertTrue(text,'测试失败')

if __name__ == "__main__":
    file_path=os.path.join(os.getcwd()+'/report/'+'first_report.html')
    f=open(file_path,'wb')
    suit = unittest.TestLoader().loadTestsFromTestCase(FirstDdtTest)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='This is first report',description=u'这是测试报告',verbosity=2)
    runner.run(suit)
