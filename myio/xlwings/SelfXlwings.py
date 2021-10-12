import xlwings as xw
from xlwings.main import App

class SelfXlwings:
    'xlwings 方法'

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
    
    def quit(self):
        self.app.quit()
