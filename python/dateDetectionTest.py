import unittest
from dateDetection import *
class test(unittest.TestCase):
    def test1(self):
        input = "date is 01/8/2303"
        expected = (1,8,2303)
        self.assertEqual(expected,dateDetection(input),"Error!")
    def test2(self):
        input = "date is 01./01.2002"
        expected = None
        self.assertEqual(expected,dateDetection(input),"Error!")
unittest.main()