from tableBuilder import dtypes
import unittest

import pandas as pd

class DtypesTests(unittest.TestCase):
    
    def test_percent_up(self):
        self.assertEqual(dtypes.percent(1.115), '1.12%')

    def test_percent_down(self):
        self.assertEqual(dtypes.percent(1.1114, 3), '1.111%')

    def test_decimal_up(self):
        self.assertEqual(dtypes.decimal(7.995), '8.00')
    
    def test_decimal_down(self):
        self.assertEqual(dtypes.decimal(7.994), '7.99')

    def test_decimal_negative(self):
        self.assertEqual(dtypes.decimal(-7.995, 3), '-7.995')

    def test_integer_up(self):
        self.assertEqual(dtypes.integer(4.5), '5')

    def test_integer_down(self):
        self.assertEqual(dtypes.integer(4.49), '4')

    def test_integer_thousands(self):
        self.assertEqual(dtypes.integer(1000), '1,000')

    def test_money_up(self):
        self.assertEqual(dtypes.money(1234.567, 1), '$1,234.6')

    def test_money_down(self):
        self.assertEqual(dtypes.money(980.554), '$980.55')

    def test_money_negative(self):
        self.assertEqual(dtypes.money(-999), '$(999.00)')

    def test_perc_col(self):
        self.assertEqual(dtypes.formatCol(
                            pd.Series([1.115, 1.114, -5]),
                            dtypes.percent,
                            2
                        ),
                        ['1.12%', '1.11%', '-5.00%'])
        
    def test_deci_col(self):
        self.assertEqual(dtypes.formatCol(
                            pd.Series([7.995, 7.994, -8]),
                            dtypes.decimal
                        ),
                        ['8.00', '7.99', '-8.00'])
        
    def test_int_col(self):
        self.assertEqual(dtypes.formatCol(
                            [4.5, 4.49, -1000],
                            dtypes.integer
                        ),
                        ['5', '4', '-1,000'])
        
    def test_money_col(self):
        self.assertEqual(dtypes.formatCol(
                            pd.Series([1234.567, 980.554, -999]),
                            dtypes.money,
                            1
                        ),
                        ['$1,234.6', '$980.6', '$(999.0)'])

if __name__ == '__main__':
    unittest.main()