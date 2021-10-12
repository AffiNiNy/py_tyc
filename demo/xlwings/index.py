import xlwings as xw
import os
import sys
sys.path.append(os.getcwd())
from myio.xlwings.SelfXlwings import *

selfxw = SelfXlwings()
wb = selfxw.new_xlsx()
comIntroSht = wb.sheets[0]
comIntroSht.range('A1').value = 1243
comIntroSht.name = '公司简介'
print(comIntroSht.name)
print(comIntroSht.range('A1').value)
wb.save(r'D:\DEVELOP\\VSCode_Projects\ALittlePythonProg\demo\\output_Excel.xlsx')
# wb.save()

selfxw.quit()

# sheet = wb.sheets[0]
# # sheet.range('A1').value = 'Foo 1'
# #python中的一维列表，在Excel中默认为一行数据
# # rng1 = sheet.range('A1').value = [[1,2], [3,4]]
# #纵向插入数据
# rng1 = sheet.range('A1').options(transpose=True).value = [[1,2,22], [3,4,44]]
# print(rng1)

# wb.save(r'D:\DEVELOP\\VSCode_Projects\ALittlePythonProg\demo\\new_Excel.xlsx')
# wb.close()

# #结束进程
# selfXW.quit()