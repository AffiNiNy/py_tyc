import xlwings as xw
import os
import sys
sys.path.append(os.getcwd())
from myio.xlwings.index import SelfXlwings

selfXW = SelfXlwings(SelfXlwings.initApp())
wb = selfXW.new_xlsx()

sheet = wb.sheets[0]
# sheet.range('A1').value = 'Foo 1'
#python中的一维列表，在Excel中默认为一行数据
# rng1 = sheet.range('A1').value = [[1,2], [3,4]]
#纵向插入数据
rng1 = sheet.range('A1').options(transpose=True).value = [[1,2,22], [3,4,44]]
print(rng1)

wb.save(r'D:\DEVELOP\\VSCode_Projects\ALittlePythonProg\demo\\new_Excel.xlsx')
wb.close()

#结束进程
selfXW.quit()