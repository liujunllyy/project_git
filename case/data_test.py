#coding=utf-8
import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(
        [1,2],
        [4,6],
        [6,8]
    )
    @ddt.unpack
    def test_1(self,a,b):
        print(a+b)

if __name__ == "__main__":
    unittest.main()