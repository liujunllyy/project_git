#coding=utf-8
import sys
sys.path.append('c:/project')
from business.register_business import BusinessRegister
from selenium import webdriver
import time
import unittest

class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass

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

    @unittest.skip('不执行')
    def test_search_input_01(self):
        self.login.input_search('123')

    def test_search_click_02(self):
        self.login.click_search()

    def test_search_click_03(self):
        text=self.login.input_search_error('asd')
        return self.assertFalse(text,'测试失败')

if __name__ == "__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(FirstCase01('test_search_input_01'))
    suit.addTest(FirstCase01('test_search_click_02'))
    suit.addTest(FirstCase01('test_search_click_03'))
    unittest.TextTestRunner().run(suit)