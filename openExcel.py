# -*- coding: utf-8 -*-
# 打开excel调用单元格
import  xdrlib ,sys
import xlrd

# try:
data = xlrd.open_workbook('E:\\file.xlsx')
table = data.sheets()[0]
nrows = table.nrows #行数
ncols = table.ncols #列数
# 第二行
cell_A1 = table.col(0)[1].value# 第1列
cell_B1 = table.col(1)[1].value# 第2列
cell_C1 = table.col(2)[1].value# 第3列
print(table.row_values(0))
print('A1',cell_A1)
print('B1',cell_B1)
print('C1',cell_C1)
print(ncols)
