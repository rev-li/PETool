import traceback

from PyQt5.QtCore import QMimeData

from DOSWindow import Ui_DosWindow
from FileWindow import Ui_FileWindow
from MainWinDow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.SelDialog)

    def SelDialog(self):
        # Dire = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        # print(Dire)

        # 设置文件扩展名过滤,注意用双分号间隔
        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")

        # 保存文件
        # fileName2, ok2 = QFileDialog.getSaveFileName(self, "文件保存", "./", "All Files (*);;Text Files (*.txt)")


class DosWin(QMainWindow, Ui_DosWindow):
    def __init__(self):
        super(DosWin, self).__init__()
        self.content = None
        self.setupUi(self)
        self.tableWidget.clicked.connect(self.fillUserInfo)
        self.CopyButton.clicked.connect(self.copyText)
        self.CopyButton.clicked.connect(self.ToldSuccessfully)

    def copyText(self):
        clipboard = QApplication.clipboard()
        # 把选择的内容复制到剪贴板
        if self.content is not None:
            clipboard.setText(self.content)

    # 获取tableWidget表格内容
    def fillUserInfo(self, Item):
        try:
            row = Item.row()  # 获取行数
            col = Item.column()  # 获取列数 注意是column而不是col哦
            text = self.tableWidget.item(row, col).text()
        except Exception as e:
            traceback.print_exc()
        self.textBrowser.setText(" ")
        self.content = text

    # def show_data(self, Item):
    #     try:
    #         row = Item.row()  # 获取行数
    #         col = Item.column()  # 获取列数 注意是column而不是col哦
    #         text = Item.text()  # 获取内容
    #     except Exception as e:
    #         traceback.print_exc()
    #
    # def getPosContent(self, row, col):
    #     try:
    #         content = self.tableWidget.item(row, col).text()
    #     except:
    #         pass
    #     return content

    def ToldSuccessfully(self):
        if self.content is not None:
            self.textBrowser.setText("复制成功！")
        else:
            self.textBrowser.setText("请选择左边框中要复制的内容！！！")
        self.content = None


class FileWin(QMainWindow, Ui_FileWindow):
    def __init__(self):
        super(Ui_FileWindow, self).__init__()
        self.content = None
        self.setupUi(self)
        self.tableWidget.clicked.connect(self.fillUserInfo)
        self.CopyButton.clicked.connect(self.copyText)
        self.CopyButton.clicked.connect(self.ToldSuccessfully)

    def copyText(self):
        clipboard = QApplication.clipboard()
        # 把选择的内容复制到剪贴板
        if self.content is not None:
            clipboard.setText(self.content)

    # 获取tableWidget表格内容
    def fillUserInfo(self, Item):
        try:
            row = Item.row()  # 获取行数
            col = Item.column()  # 获取列数 注意是column而不是col哦
            text = self.tableWidget.item(row, col).text()
        except Exception as e:
            traceback.print_exc()
        self.textBrowser.setText(" ")
        self.content = text

    def ToldSuccessfully(self):
        if self.content is not None:
            self.textBrowser.setText("复制成功！")
        else:
            self.textBrowser.setText("请选择左边框中要复制的内容！！！")
        self.content = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    doswin = DosWin()
    main.show()
    main.actionIMAGE_DOS_HEADER.triggered.connect(doswin.show)
    sys.exit(app.exec_())
