#coding=utf-8
import sys
import os
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(cur_path)
from business.register_business import BusinessRegister
from selenium import webdriver
import time
import unittest
#import HTMLTestRunner
from HwTestReport import HTMLTestReport
from HwTestReport import HTMLTestReportEN
from log.user_log import UserLog


class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.imgs = []
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.log.info("this is chrome")
        self.driver.maximize_window()
        time.sleep(2)
        self.login=BusinessRegister(self.driver)

    def tearDown(self):
        # if sys.exc_info()[0]:  ptthon 2 处理
        # for method_name,error in self._outcome.errors:
        #     if error:
        #         case_name=self._testMethodName
        #         file_path=os.path.join(os.getcwd()+'/report/'+case_name+'.png')
        #         self.driver.save_screenshot(file_path)
        self.driver.close()

    def get_screenshot(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    #@unittest.skip('不执行')
    def test_search_input(self):
        self.login.input_search('123')
        self.get_screenshot()
        self.assertFalse(True)

    def test_search_click(self):
        self.login.click_search()
        self.get_screenshot()

    def test_search_error(self):
        text=self.login.input_search_error('asd')
        self.get_screenshot()
        return self.assertTrue(text,'测试失败')

if __name__ == "__main__":
    # unittest.main()
    file_path=os.path.join(os.getcwd()+'/report/'+'first_report.html')
    f=open(file_path,'wb')
    suit = unittest.TestSuite()
    suit.addTest(FirstCase01('test_search_input'))
    suit.addTest(FirstCase01('test_search_click'))
    suit.addTest(FirstCase01('test_search_error'))
    # unittest.TextTestRunner().run(suit)

    # runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='This is first report',description=u'这是测试报告',verbosity=2)
    # runner.run(suit)


    runner = HTMLTestReportEN(stream=f,
                            verbosity=2,
                            images=True,
                            title='HwTestReport 测试',
                            description='带截图，带饼图，带详情',
                            tester='Johnny')
    runner.run(suit)