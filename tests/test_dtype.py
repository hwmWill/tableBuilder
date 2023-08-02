from tableBuilder.dtypes import percent


import unittest

class BasicTestSuite(unittest.TestCase):
    
    def test_percent_up(self):
        self.assertEqual(percent(1.115), '1.12%')

    def test_percent_down(self):
        self.assertEqual(percent(1.1114, 3), '1.111%')


if __name__ == '__main__':
    unittest.main()