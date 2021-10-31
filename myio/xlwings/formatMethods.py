import xlwings as xw

tableSpaceRows = 3


def formatHeader_comInfo(sheet:xw.main.Sheet):
    # 表头
    h = sheet.range('A1:V1')
    h.value = '公司基本信息'
    formatTableTitle(h)

    th = sheet.range('A2:E2')
    th.value = '公司名称'
    th.merge()
    sheet.range('A2:E2').merge()
    sheet.range('A3:E3').merge()
    th2 = sheet.range('F2:H2')
    th2.value = '企业类型'
    th2.merge()
    sheet.range('F3:H3').merge()
    sheet.range('F3:H3').wrap_text = True
    th3 = sheet.range('I2:J2')
    th3.value = '成立时间'
    th3.merge()
    sheet.range('I3:J3').merge()
    sheet.range('I3:J3').wrap_text = True
    th4 = sheet.range('K2:L2')
    th4.value = '注册资金\r\n(万元)'
    th4.merge()
    sheet.range('K3:L3').merge()
    sheet.range('K3:L3').wrap_text = True
    th5 = sheet.range('M2:N2')
    th5.value = '法宝代表人'
    th5.merge()
    sheet.range('M3:N3').merge()
    sheet.range('M3:N3').wrap_text = True
    th6 = sheet.range('O2:R2')
    th6.value = '经营范围'
    th6.merge()
    sheet.range('O3:R3').merge()
    sheet.range('O3:R3').wrap_text = True
    th7 = sheet.range('S2:V2')
    th7.value = '主要客户群体'
    th7.merge()
    sheet.range('S3:V3').merge()
    sheet.range('S3:V3').wrap_text = True
    th8 = sheet.range('A4:E8')
    th8.value = '简介'
    th8.merge()
    sheet.range('F4:V8').merge()
    sheet.range('F4:V8').wrap_text = True

    row2 = sheet.range('A2:V2')
    formatTableHeader(row2)
    row3 = sheet.range('A3:V3')
    row3.row_height = 67
    row3.font.size = 11
    format_vCenter_hCenter(sheet.range('A1:V8'))
    introDetailRng = sheet.range('F4:V8')
    introDetailRng.wrap_text = True
    format_vLeft_hCenter(introDetailRng)
    formatFontAndBorders(sheet.range('A1:V8'))

def formatHeader_shareHolders(sheet:xw.main.Sheet): 
    sTitleRng = sheet.range('A11:N11')
    sTitleRng.value = '股东信息'
    formatTableTitle(sTitleRng)

    sheet.range('A12').value = '序号'
    th2 = sheet.range('B12:F12')
    th2.value = '股东(发起人)'
    th2.merge()
    th3 = sheet.range('G12:H12')
    th3.value = '招股比例'
    th3.merge()
    th4 = sheet.range('I12:J12')
    th4.value = '最终受益股份'
    th4.merge()
    th5 = sheet.range('K12:L12')
    th5.value = '认缴出资比例'
    th5.merge()
    th6 = sheet.range('M12:N12')
    th6.value = '认缴出资日期'
    th6.merge()
    formatTableHeader(sheet.range('A12:N12'))

# 从股东信息列表开始返回下一个表格的开始行号
def fill_holdersInfo(sheet:xw.main.Sheet, infoList):
    startRowNum = currentRowNum = 13
    for i in range(len(infoList)):
        currentRowNum += i # 股东信息列表开始行
        rowNumStr = str(currentRowNum)
        sheet.range('A' + rowNumStr).value = infoList[i][0]
        rd2 = sheet.range('B'+rowNumStr + ':F'+rowNumStr)
        rd2.value = infoList[i][1]
        rd2.merge()
        rd3 = sheet.range('G'+rowNumStr + ':H'+rowNumStr)
        rd3.value = infoList[i][2]
        rd3.merge()
        rd3.number_format = '##.##%'
        rd4 = sheet.range('I'+rowNumStr + ':J'+rowNumStr)
        rd4.value = infoList[i][3]
        rd4.merge()
        rd4.number_format = '##.##%'
        rd5 = sheet.range('K'+rowNumStr + ':L'+rowNumStr)
        rd5.value = infoList[i][4]
        rd5.merge()
        rd6 = sheet.range('M'+rowNumStr + ':N'+rowNumStr)
        rd6.value = infoList[i][5]
        rd6.merge()
    
    format_tableData(sheet.range('A'+str(startRowNum) + ':N'+rowNumStr))
    formatFontAndBorders(sheet.range('A11:N' + rowNumStr))
    currentRowNum += tableSpaceRows
    return currentRowNum

def formatHeader_mainStaff(sheet:xw.main.Sheet, startRowNum):
    srnStr = str(startRowNum)
    msTitle = sheet.range('A'+srnStr + ":I"+srnStr)
    msTitle.value = '主要人员'
    formatTableTitle(msTitle)

    startRowNum += 1
    srnStr = str(startRowNum)
    sheet.range('A'+srnStr).value = '序号'
    th2 = sheet.range('B'+srnStr + ':C'+srnStr)
    th2.value = '姓名'
    th2.merge()
    th3 = sheet.range('D'+srnStr + ':E'+srnStr)
    th3.value = '职位'
    th3.merge()
    th4 = sheet.range('F'+srnStr + ':G'+srnStr)
    th4.value = '持股比例'
    th4.merge()
    th5 = sheet.range('H'+srnStr + ':I'+srnStr)
    th5.value = '最终受益股份'
    th5.merge()
    formatTableHeader(sheet.range('A'+srnStr + ':I'+srnStr))

    return startRowNum

def fill_mainStaffInfo(sheet:xw.main.Sheet, startNum, staffList):

    pass

def formatHeader_coreTeam(range:xw.main.Range) -> None:
    pass

def formatHeader_comBusiness(range:xw.main.Range) -> None:
    pass

def formatTableTitle(range:xw.main.Range):
    range.merge()
    range.font.size = 14
    range.font.bold = True
    range.row_height = 18.75
    format_vCenter_hCenter(range)

def formatTableHeader(range:xw.main.Range):
    range.font.size = 12
    range.font.bold = True
    range.row_height = 36
    format_vCenter_hCenter(range)

def format_tableData(range:xw.main.Range):
    range.row_height = 15.5
    format_vCenter_hCenter(range)

#HorizontalAlignment: -4108 居中 -4131 靠左 -4152 靠右;
#VerticalAlignment: -4108 居中 -4160 靠上 -4107 靠下
def format_vCenter_hCenter(range:xw.main.Range):
    """水平居中 - 垂直居中"""
    range.api.HorizontalAlignment = -4108
    range.api.VerticalAlignment = -4108
    
def format_vLeft_hCenter(range:xw.main.Range):
    """水平靠左 - 垂直居中"""
    range.api.HorizontalAlignment = -4131
    range.api.VerticalAlignment = -4108
    
def format_vRight_hCenter(range:xw.main.Range):
    """水平靠右 - 垂直居中"""
    range.api.HorizontalAlignment = -4152
    range.api.VerticalAlignment = -4108

# 全表格式
def formatFontAndBorders(range:xw.main.Range) -> None:
    """
    所有框线: 1;
    字体: 宋体;
    """
    range.api.Borders.LineStyle = 1
    range.font.name = '宋体'