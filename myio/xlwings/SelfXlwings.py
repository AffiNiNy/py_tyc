from _typeshed import Self
import time
import xlwings as xw
from xlwings.main import App

curYear = time.localtime(time.time()).tm_year


class SelfXlwings:
    tableSpaceRows = 3
    dateFormat = 'yyyy"年"m"月"d"日"'
    
    def __init__(self):
        self.app = SelfXlwings.initApp()
        self.curRowNum = 1

    @staticmethod
    def initApp():
        app = xw.App(visible=False,add_book=True)
        #不显示Excel消息框
        app.display_alerts = False
        #关闭屏幕更新,可加快宏的执行速度
        app.screen_updating = False
        return app
    
    @staticmethod
    def formatTableTitle(range:xw.main.Range):
        range.merge()
        range.font.size = 14
        range.font.bold = True
        range.row_height = 18.75
        SelfXlwings.format_vCenter_hCenter(range)

    @staticmethod
    def formatTableHeader(range:xw.main.Range):
        range.font.size = 12
        range.font.bold = True
        range.row_height = 36
        SelfXlwings.format_vCenter_hCenter(range)

    @staticmethod
    def format_tableData(range:xw.main.Range):
        range.row_height = 15.5
        SelfXlwings.format_vCenter_hCenter(range)

    def new_xlsx(self):
        return self.app.books.add()
    
    def open_xlsx(self, xlsxPath):
        return self.app.books.open(xlsxPath)

    def formatHeader_shareHolders(self, sheet:xw.main.Sheet):
        sTitleRng = sheet.range('A11:N11')
        sTitleRng.value = '股东信息'
        SelfXlwings.formatTableTitle(sTitleRng)

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
        SelfXlwings.formatTableHeader(sheet.range('A12:N12'))

    # 股东信息列表  开始返回下一个表格的开始行号
    def fill_holdersInfo(self, sheet:xw.main.Sheet, infoList):
        startRowNum = self.curRowNum = 13
        for i in range(len(infoList)):
            self.curRowNum += i # 股东信息列表开始行
            rowNumStr = str(self.curRowNum)
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
            rd6.number_format = SelfXlwings.dateFormat
        
        SelfXlwings.format_tableData(sheet.range('A'+str(startRowNum) + ':N'+rowNumStr))
        SelfXlwings.formatFontAndBorders(sheet.range('A11:N' + rowNumStr))
        self.curRowNum += SelfXlwings.tableSpaceRows
        print('--- 股东信息列表完成')

    # 主要人员表头
    def formatHeader_mainStaff(self, sheet:xw.main.Sheet):
        srnStr = str(self.curRowNum)
        msTitle = sheet.range('A'+srnStr + ":I"+srnStr)
        msTitle.value = '主要人员'
        SelfXlwings.formatTableTitle(msTitle)

        self.curRowNum += 1
        srnStr = str(self.curRowNum)
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
        SelfXlwings.formatTableHeader(sheet.range('A'+srnStr + ':I'+srnStr))

    # 主要人员列表
    def fill_mainStaffInfo(self, sheet:xw.main.Sheet, staffList):
        self.curRowNum += 1
        startRowNum = self.curRowNum
        for i in range(len(staffList)):
            self.curRowNum += 1
            rnStr = str(self.curRowNum)
            sheet.range('A' + rnStr).value = staffList[i][0]
            rd2 = sheet.range('B'+rnStr + ':C'+rnStr)
            rd2.value = staffList[i][1]
            rd2.merge()
            rd2 = sheet.range('D'+rnStr + ':E'+rnStr)
            rd2.value = staffList[i][2]
            rd2.merge()
            rd2 = sheet.range('F'+rnStr + ':G'+rnStr)
            rd2.value = staffList[i][3]
            rd2.merge()
            # rd2.number_format = '##.##%'
            rd2 = sheet.range('H'+rnStr + ':I'+rnStr)
            rd2.value = staffList[i][4]
            rd2.merge()
            # rd2.number_format = '##.##%'
        
        SelfXlwings.format_tableData(sheet.range('A'+str(startRowNum) + ':I'+rnStr))
        SelfXlwings.formatFontAndBorders(sheet.range('A'+str(startRowNum - 2) + ':I' + rnStr))
        self.curRowNum += SelfXlwings.tableSpaceRows
        print('--- 主要人员列表完成')

    # 核心团队
    def formatHeader_mainTeam(self, sheet:xw.main.Sheet):
        srnStr = str(self.curRowNum)
        mtTitle = sheet.range('A'+srnStr + ':V'+srnStr)
        mtTitle.value = '核心团队'
        SelfXlwings.formatTableTitle(mtTitle)
        
        self.curRowNum += 1
        srnStr = str(self.curRowNum)
        rh = sheet.range('A'+srnStr)
        rh.value = '序号'
        rh = sheet.range('B'+srnStr + ':C'+srnStr)
        rh.value = '姓名'
        rh.merge()
        rh = sheet.range('D'+srnStr + ':F'+srnStr)
        rh.value = '职位'
        rh.merge()
        rh = sheet.range('G'+srnStr + ':V'+srnStr)
        rh.value = '简介'
        rh.merge()
        SelfXlwings.formatTableHeader(sheet.range('A'+srnStr + ':V'+srnStr))

    # 核心团队列表
    def fill_mainTeamInfo(self, sheet:xw.main.Sheet, teamList):
        self.curRowNum += 1
        startRowNum = self.curRowNum
        for eachEle in teamList:
            rw1 = str(self.curRowNum)
            rw2 = str(self.curRowNum + 1)
            rd2 = sheet.range('A'+rw1 + ':A'+rw2)
            rd2.value = eachEle[0]
            rd2.merge()
            rd2 = sheet.range('B'+rw1 + ':C'+rw2)
            rd2.value = eachEle[1]
            rd2.merge()
            rd2 = sheet.range('D'+rw1 + ':F'+rw2)
            rd2.value = eachEle[2]
            rd2.merge()
            rd2 = sheet.range('G'+rw1 + ':V'+rw2)
            rd2.value = eachEle[3]
            rd2.merge()
            self.curRowNum += 2
        
        SelfXlwings.format_tableData(sheet.range('A'+str(startRowNum) + ':V'+rw2))
        SelfXlwings.formatFontAndBorders(sheet.range('A'+str(startRowNum - 2) + ':V' + rw2))
        self.curRowNum += SelfXlwings.tableSpaceRows
        print('--- 核心团队列表完成')

    # 企业业务
    def formatHeader_firmProd(self, sheet:xw.main.Sheet):
        srnStr = str(self.curRowNum)
        fpTitle = sheet.range('A'+srnStr + ':Q'+srnStr)
        fpTitle.value = '企业业务'
        SelfXlwings.formatTableTitle(fpTitle)

        self.curRowNum += 1
        srnStr = str(self.curRowNum)
        sheet.range('A' + srnStr).value = '序号'
        rh = sheet.range('B'+srnStr + ':E'+srnStr)
        rh.value = '产品名称'
        rh.merge()
        rh = sheet.range('F'+srnStr + ':G'+srnStr)
        rh.value = '成立日期'
        rh.merge()
        rh = sheet.range('H'+srnStr + ':I'+srnStr)
        rh.value = '当前融资轮次'
        rh.merge()
        rh = sheet.range('J'+srnStr + ':K'+srnStr)
        rh.value = '产品标签'
        rh.merge()
        rh = sheet.range('L'+srnStr + ':M'+srnStr)
        rh.value = '所属地'
        rh.merge()
        rh = sheet.range('N'+srnStr + ':Q'+srnStr)
        rh.value = '产品介绍'
        rh.merge()
        SelfXlwings.formatTableHeader(sheet.range('A'+srnStr + ':Q'+srnStr))
    
    # 企业业务列表
    def fill_firmPordInfo(self, sheet:xw.main.Sheet, prodList):
        self.curRowNum += 1
        startRowNum = self.curRowNum
        for i in range(len(prodList)):
            self.curRowNum += i
            rnStr = str(self.curRowNum)
            sheet.range('A' + rnStr).value = prodList[i][0]
            rd2 = sheet.range('B'+rnStr + ':E'+rnStr)
            rd2.value = prodList[i][1]
            rd2.merge()
            rd2 = sheet.range('F'+rnStr + ':G'+rnStr)
            rd2.value = prodList[i][2]
            rd2.merge()
            rd2.number_format = SelfXlwings.dateFormat
            rd2 = sheet.range('H'+rnStr + ':I'+rnStr)
            rd2.value = prodList[i][3]
            rd2.merge()
            rd2 = sheet.range('J'+rnStr + ':K'+rnStr)
            rd2.value = prodList[i][4]
            rd2.merge()
            rd2 = sheet.range('L'+rnStr + ':M'+rnStr)
            rd2.value = prodList[i][5]
            rd2.merge()
            rd2 = sheet.range('N'+rnStr + ':Q'+rnStr)
            rd2.value = prodList[i][6]
            rd2.merge()
        
        SelfXlwings.format_tableData(sheet.range('A'+str(startRowNum) + ':Q'+rnStr))
        SelfXlwings.formatFontAndBorders(sheet.range('A'+str(startRowNum - 2) + ':Q' + rnStr))
        self.curRowNum += SelfXlwings.tableSpaceRows
        print('--- 企业业务列表完成')

    # 招投标表
    def setBidsHeader(self, sheet:xw.main.Sheet):
        bidTitle = sheet.range('A1:H1')
        bidTitle.value = '中标项目({0}-至今)'.format(curYear - 5)
        bidTitle.merge()
        SelfXlwings.formatTableTitle(bidTitle)
        SelfXlwings.formatTableHeader(sheet.range('A2:H2'))
        sheet.range('A2').value = '公司名称'
        sheet.range('A2').column_width = 14.25
        sheet.range('B2').value = '项目名称'
        sheet.range('B2').column_width = 60
        pass

    #HorizontalAlignment: -4108 居中 -4131 靠左 -4152 靠右;
    #VerticalAlignment: -4108 居中 -4160 靠上 -4107 靠下
    @staticmethod
    def format_vCenter_hCenter(range:xw.main.Range):
        """水平居中 - 垂直居中"""
        range.api.HorizontalAlignment = -4108
        range.api.VerticalAlignment = -4108
    
    @staticmethod
    def format_vLeft_hCenter(range:xw.main.Range):
        """水平靠左 - 垂直居中"""
        range.api.HorizontalAlignment = -4131
        range.api.VerticalAlignment = -4108
    
    @staticmethod
    def format_vRight_hCenter(range:xw.main.Range):
        """水平靠右 - 垂直居中"""
        range.api.HorizontalAlignment = -4152
        range.api.VerticalAlignment = -4108
    
    # 全表格式
    @staticmethod
    def formatFontAndBorders(range:xw.main.Range):
        """
        所有框线: 1;
        字体: 宋体;
        """
        range.api.Borders.LineStyle = 1
        range.font.name = '宋体'
    
    def kill(self):
        self.app.kill()
 