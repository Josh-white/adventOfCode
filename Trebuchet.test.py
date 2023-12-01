import unittest

from Trebuchet import get_calibration_value


class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_list = """1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet"""
        result = get_calibration_value(test_list)
        self.assertEqual(result, 142)


if __name__ == '__main__':
    unittest.main()
