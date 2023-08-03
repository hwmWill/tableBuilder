from tableBuilder.xlHtml import hwTable
import unittest

import pandas as pd

class DtypesTests(unittest.TestCase):
    
    def test_from_excel(self):
        self.assertEqual(hwTable('tests/Example.xlsx').xlsxHtml(datatypes=
                                {'Money':('money'),
                                'Volume':('integer'),
                                'Percent':('percent', 2),
                                'Float':('decimal', 3)}), 
                        open('tests/example.html', 'r').read())

if __name__ == '__main__':
    unittest.main()