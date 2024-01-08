import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from Window.MainWindow import MainWindow

# 初始化主界面
def initMainWindow(app, ui):
    ui.actionExit.triggered.connect(lambda: app.quit())

def openFile():
    pass
    # # 设置文件扩展名过滤,注意用双分号间隔
    # self.filePath, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
    #                                                         "All Files (*);;Text Files (*.txt)")
    # print(self.filePath)
    # self.CheckFile(self.filePath)

# 程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())