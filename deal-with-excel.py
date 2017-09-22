# -*- coding: utf-8 -*- 

# Use python lib xlrd to deal with Microsoft Excel, 
# Library for developers to extract data from Microsoft Excel (tm) spreadsheet files.
# Which Public Website is https://pypi.python.org/pypi/xlrd

import xdrlib, sys
import xlrd

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

# 根据索引获取Excel表格中的数据
# 参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= '20170825_j1801.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    print  nrows # byhankswang
    ncols = table.ncols #列数
    print ncols
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= '20170825_j1801.xls',colnameindex=0,by_name= '日成交持仓排名'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list


def getExcelData(filename):
    book = xlrd.open_workbook(filename)
    sheetName = book.sheet_names()
    sheet1 = book.sheet_by_name(sheetName[0])
    top5_buyer_name = sheet1.col_values(5)[4:9]
    top5_buyer_data = sheet1.col_values(6)[4:9]
    print (repr(top5_buyer_name).decode('unicode-escape'))
    print (repr(top5_buyer_data).decode('unicode-escape'))
    print "=====Work Done====="
    print(repr(sheetName).decode('unicode-escape'))


def main():
   tables = excel_table_byindex()
   for row in tables:
       print row

   tables = excel_table_byname()
   for row in tables:
       print row

   getExcelData("20170922_jm1801.xls")

if __name__== "__main__":
    main()
