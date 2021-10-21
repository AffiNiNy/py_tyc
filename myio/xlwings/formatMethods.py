import xlwings as xw


def formatHeader_comInfo(sheet:xw.main.Sheet) -> None:
    # 表头
    h = sheet.range('A1:V1')
    h.value = '公司基本信息'
    h.merge()
    h.row_height = 18.75
    h.font.size = 14
    h.font.bold = True

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
    row2.row_height = 36
    row2.font.size = 12
    row2.font.bold = True
    row3 = sheet.range('A3:V3')
    row3.row_height = 67
    row3.font.size = 11
    format_vCenter_hCenter(sheet.range('A1:V8'))
    introDetailRng = sheet.range('F4:V8')
    introDetailRng.wrap_text = True
    format_vLeft_hCenter(introDetailRng)

def formatHeader_shareHolders(range:xw.main.Range) -> None:
    pass

def formatHeader_mainStaff(range:xw.main.Range) -> None:
    pass

def formatHeader_coreTeam(range:xw.main.Range) -> None:
    pass

def formatHeader_comBusiness(range:xw.main.Range) -> None:
    pass

#HorizontalAlignment: -4108 居中 -4131 靠左 -4152 靠右;
#VerticalAlignment: -4108 居中 -4160 靠上 -4107 靠下
def format_vCenter_hCenter(range:xw.main.Range) -> None:
    """水平居中 - 垂直居中"""
    range.api.HorizontalAlignment = -4108
    range.api.VerticalAlignment = -4108
    
def format_vLeft_hCenter(range:xw.main.Range) -> None:
    """水平靠左 - 垂直居中"""
    range.api.HorizontalAlignment = -4131
    range.api.VerticalAlignment = -4108
    
def format_vRight_hCenter(range:xw.main.Range) -> None:
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