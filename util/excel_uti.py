#coding=utf-8
import os

# 获取当前文件的上一层路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
casedata_path = os.path.join(os.path.join(cur_path,'config'),'casedata.xls')
import xlrd
from xlutils.copy import copy
class ExcelUti():
    def __init__(self,excel_path=None,index=None):
        if excel_path==None:
            self.excel_path=casedata_path
        else:
            self.excel_path=excel_path
        if index==None:
            index=0
        self.data=xlrd.open_workbook(self.excel_path)
        self.table=self.data.sheets()[index]

    def get_data(self):
        result=[]
        rows=self.get_lines()
        if rows!=None:
            for i in range(rows):
                col=self.table.row_values(i)
                result.append(col)
            return result
        else:
            return None

    def get_lines(self):
        rows=self.table.nrows
        if rows>=1:
            return rows
        else:
            return None

    def get_cols(self):
        cols=self.table.ncols
        if cols>=1:
            return cols
        else:
            return None

    def get_col_value(self,row,col):
        if self.get_lines()>row and self.get_cols()>col:
            data = self.table.cell(row,col).value
            return data
        else:
            return None

    def write_value(self,row,value):
        read_value=xlrd.open_workbook(self.excel_path)
        write_data=copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)

if __name__ == "__main__":
    ex=ExcelUti("C:/project/config/keyword.xls")
    #print(ex.get_data())
    print(ex.get_col_value(6,9))
    #ex.write_value(7,'wer')