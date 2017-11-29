#!/usr/bin/python
# -*- coding:utf-8  -*-
'''
@description: 将一个大excel分割成多个1000行的小excel
@author: 张佳俊
'''

import xlrd
import xlwt
import os

limit = 1000

readbook = raw_input('输入源Excel路径(不要包含中文):')

savebook = raw_input('输入目标Excel路径(不要包含中文):')


data = xlrd.open_workbook(readbook)


(filepath,tempfilename) = os.path.split(readbook);
(shotname,extension) = os.path.splitext(tempfilename);
if savebook == '':
    savebook = filepath
# 获取第一个sheet
table = data.sheets()[0]
# 行数
nrows = table.nrows
# 列数
ncols = table.ncols

lastRows = nrows % limit;

#拆分后的文件数
if lastRows != 0:
    fs = nrows / limit + 1
else:
    fs = nrows / limit



for i in range(0, fs):
    workbook = xlwt.Workbook(encoding='ascii');
    worksheet = workbook.add_sheet("sheet1");
    startRow = i * limit;
    endRow = (i + 1) * limit;
    rowIndex = 0;
    if i == fs - 1:
        endRow = nrows;
    for row in range(startRow, endRow):
        row_content = table.row_values(row)
        for col in range(0, ncols):
            worksheet.write(rowIndex, col, row_content[col])

        rowIndex = rowIndex + 1;
    workbook.save(savebook + "/" + shotname + str(i) + ".xls")
