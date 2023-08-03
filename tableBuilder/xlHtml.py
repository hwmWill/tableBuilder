import pandas as pd

from .dtypes import percent, decimal, integer, money, formatCol

class hwTable:
    def __init__(self, filePath, source=''):
        self.filePath = filePath
        self.source = f'Source: {source}'
        self.dtypes = {'percent':percent,
                        'decimal':decimal,
                        'integer':integer,
                        'money':money}
        self.tableStyle = '''
<style>
  table.hwTable {
    text-align: justify;
    border-spacing: 0;
    border-collapse: separate;
    border-radius: 10px;
    border: solid 1px black;
  }
  table.hwTable tr:nth-child(even) {
    background-color: lightgrey;
  }
  table.hwTable td {
    border-left: solid;
    border-right: solid;
    border-color: black;
    border-width: 1px;
    padding-top: 3px;
    padding-bottom: 3px;
    padding-left: 5px;
    padding-right: 5px;
    word-break: break-all;
  }
  table.hwTable th {
   text-align: center; 
   padding: 3px;
   background-color: black;
   color: white;
  }
  table.hwTable th:first-child {
    border-top-left-radius: 10px;
  }
  table.hwTable th:last-child {
    border-top-right-radius: 10px;
  }
  table.hwTable tfoot td {
    background-color: black;
    color: white;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }
</style>
'''

    def xlsxHtml(self, datatypes={}, writePath=None):
        df = pd.read_excel(self.filePath)
        if len(datatypes) > 0:
            for col, params in datatypes.items():
                try:
                    df[col] = formatCol(df[col], 
                                        dtype=self.dtypes[params[0]], 
                                        roundTo=params[1])
                except:
                    df[col] = formatCol(df[col], 
                                        dtype=self.dtypes[params])
        table = df.to_html(index=False, classes='hwTable', border=0)
        if self.source != 'Source: ':
            table = table.replace('</tbody>',
                          f'''</tbody>
<tfoot>
    <tr><td colspan="100%">{self.source}</td></tr>
</tfoot>
''')
        else:
            table = table.replace('</tbody>',
                          f'''</tbody>
<tfoot>
    <tr><td colspan="100%"></td></tr>
</tfoot>
''')
        if writePath:
            f = open(writePath, 'w')
            f.write(self.tableStyle + '\n' + table)
            f.close()
            return
        return self.tableStyle + '\n' + table

