import xlwings as xw
from xlwings.main import App

class SelfXlwings:
    """xlwings 方法"""

    def __init__(self):
        self.app = SelfXlwings.initApp()

    @staticmethod
    def initApp():
        app = xw.App(visible=False,add_book=True)
        #不显示Excel消息框
        app.display_alerts = False
        #关闭屏幕更新,可加快宏的执行速度
        app.screen_updating = False
        return app
    
    def new_xlsx(self):
        return self.app.books.add()
    
    def open_xlsx(self, xlsxPath):
        return self.app.books.open(xlsxPath)
    
    def formatTitle(self, range, titleName):
        """
        设置 sheet 表头(第一行)

        Parameters
        ----------
        name : excelSheet
            Sheet wanted to be processed.
        titleName : String
            Table title.
        ----------
        """
        range.merge()
        range.value = titleName
        range.font.size = 14
        range.font.bold = True
        range.row_height = 18.75
        range.api.HorizontalAlignment = -4108
        range.api.VerticalAlignment = -4108
    
    def formatHeader(self, range):
        range.font.size = 12
        range.font.bold = True
        range.api.HorizontalAlignment = -4108
        range.api.VerticalAlignment = -4108

    def formatInAllCenter(self, range):
        """
        水平居中; 垂直居中;
        """
        range.api.HorizontalAlignment = -4108
        range.api.VerticalAlignment = -4108

    def formatLeftCenter(self, range):
        """
        水平靠左; 垂直居中;
        """
        range.api.HorizontalAlignment = -4131
        range.api.VerticalAlignment = -4108
    
    def kill(self):
        self.app.kill()
