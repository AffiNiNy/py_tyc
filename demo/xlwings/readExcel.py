import os
import sys
import xlwings as xw
sys.path.append(os.getcwd())
from myio.xlwings.SelfXlwings import *


sxw = SelfXlwings()
workbook = sxw.open_xlsx('D:\VSCode_Projects\py_tyc\demo\航天精一（广东）信息科技有限公司_相关信息收集.xlsx')
s1 = workbook.sheets[0]
rng = s1.range('A2:V2')
print(rng.merge_cells)
print(s1.range('B2').merge_area)

sxw.quit()