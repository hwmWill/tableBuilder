import pandas as pd

from dtypes import percent, decimal, integer, money

class hwTable:
    def __init__(self):
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