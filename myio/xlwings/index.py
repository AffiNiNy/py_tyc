import xlwings as xw
from xlwings.main import App, Books

class SelfXlwings:
    'xlwings 方法'

    def __init__(self, app) -> None:
        self.app = app

    @staticmethod
    def initApp():
        app = xw.App(visible=False,add_book=False)
        #不显示Excel消息框
        app.display_alerts = False
        #关闭屏幕更新,可加快宏的执行速度
        app.screen_updating = False
        return app
    
    @classmethod
    def new_xlsx(self) -> Books:
        return self.app.books.add()
    
    @classmethod
    def print_attr(self):
        print(self.num)
    
    @classmethod
    def quit(self):
        self.app.quit()
