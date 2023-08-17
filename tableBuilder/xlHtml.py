import pandas as pd
try:
    from .dtypes import percent, decimal, integer, money, formatCol
except:
    from dtypes import percent, decimal, integer, money, formatCol

class hwTable:
    def __init__(self, data, source=''):
        self.data = data
        self.source = f'Source: {source}'
        self.dtypes = {'percent':percent,
                        'decimal':decimal,
                        'integer':integer,
                        'money':money}
        self.tableStyle = '''
<style>
  table.hwTable {
    text-align: justify;
    font-family: Poppins, sans-serif;
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
    text-align: start;
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
    table.hwTable a {
    color: #ee3124;
    text-decoration: none;
  }
  table.hwTable a:hover {
    color: #a72119;
  }
</style>
'''

    def dataHtml(self, datatypes={}, writePath=None):
        if isinstance(self.data, str):
            df = pd.read_excel(self.data)
        else:
            df = self.data
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

# df = pd.read_excel('C:/Users/WilliamRobinson/OneDrive - HW Publishing LLC/Documents/Data/Inc5000_Insurers_2023.xlsx')
# df['Growth (3-yr Avg.)'] = df['Growth (3-yr Avg.)'].mul(100)
# hwTable(df, source='Inc. 5000 - 2023').dataHtml(datatypes=
#                                 {'Rank':('integer'),
#                                 'Growth (3-yr Avg.)':('percent', 0)},
#                                 writePath='./Inc5000_Insurers.html')