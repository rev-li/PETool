import time
import traceback

from PyQt5.QtCore import QMimeData, Qt

from DOSWindow import Ui_DosWindow
from DataWindow import Ui_DataDirectoryWindow
from FileWindow import Ui_FileWindow
from MainWinDow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *

from OptionalWindow import Ui_OptionalWindow
from TipWindow import Ui_TipWindow


def Operate():
    main = Main()
    main.show()
    doswin = DosWin()
    filewin = FileWin()
    optwin = OptWin()
    datawin = DataWin()
    main.actionIMAGE_DOS_HEADER.triggered.connect(doswin.show)
    main.actionIMAGE_FILE_HEADER.triggered.connect(filewin.show)
    main.actionIMAGE_OPTIONAL_HEADER.triggered.connect(optwin.show)
    main.actionIMAGE_DATA_HEADER.triggered.connect(datawin.show)


class TipWin(QMainWindow, Ui_TipWindow):
    def __init__(self):
        super(TipWin, self).__init__()
        self.content = None
        self.setupUi(self)
        self.EndName = [".exe", ".dll", ".sys", ".ocx", ".com"]
        # 调用Drops方法
        self.setAcceptDrops(True)
        self.actionOpen.triggered.connect(self.SelDialog)

    def SelDialog(self):
        # 设置文件扩展名过滤,注意用双分号间隔
        filePath, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        print(filePath)
        self.CheckFile(filePath)

    # 鼠标进入
    def dragEnterEvent(self, evn):
        evn.accept()

    # 鼠标放开
    def dropEvent(self, evn):
        filePath = evn.mimeData().text().split("///")[1]
        print(filePath)
        self.CheckFile(filePath)

    def CheckFile(self, filePath):
        tmp = None
        tmp = [e for e in self.EndName if e in filePath]
        print(tmp)

        if not tmp:
            self.label.setText("这不是一个正确的文件o，请重新打开@_@")
            print("这不是一个正确的文件")
        else:
            self.label.setText("正在加载，请稍后^_^")
            print("正在打开这个文件...")
            with open(filePath, mode="rb") as file:
                if file is None:
                    self.label.setText("源文件打开出错啦！！")
                    print("源文件打开出错啦！！")
                else:
                    self.content = file.read()
                    # print(self.content)
                    file.close()
                    Operate()


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
            self.content = self.tableWidget.item(row, col).text()
        except Exception as e:
            traceback.print_exc()
        self.label.setText("        *_*      ")

    def ToldSuccessfully(self):
        if self.content is not None:
            self.label.setText("复制成功！")
        else:
            self.label.setText("请选择左边框中要复制的内容！！！")
        self.content = None


class FileWin(QMainWindow, Ui_FileWindow):
    def __init__(self):
        super(FileWin, self).__init__()
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
            self.content = self.tableWidget.item(row, col).text()
        except Exception as e:
            traceback.print_exc()
        self.label.setText(" ")

    def ToldSuccessfully(self):
        if self.content is not None:
            self.label.setText("复制成功！")
        else:
            self.label.setText("请选择左边框中要复制的内容！！！")
        self.content = None


class OptWin(QMainWindow, Ui_OptionalWindow):
    def __init__(self):
        super(OptWin, self).__init__()
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
            self.content = self.tableWidget.item(row, col).text()
        except Exception as e:
            traceback.print_exc()
        self.textBrowser.setText("        *_*      ")

    def ToldSuccessfully(self):
        if self.content is not None:
            self.textBrowser.setText("复制成功！")
        else:
            self.textBrowser.setText("请选择左边框中要复制的内容！！！")
        self.content = None


class DataWin(QMainWindow, Ui_DataDirectoryWindow):
    def __init__(self):
        super(DataWin, self).__init__()
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
            self.content = self.tableWidget.item(row, col).text()
        except Exception as e:
            traceback.print_exc()
        self.textBrowser.setText(" ")

    def ToldSuccessfully(self):
        if self.content is not None:
            self.textBrowser.setText("复制成功！")
        else:
            self.textBrowser.setText("请选择左边框中要复制的内容！！！")
        self.content = None


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.content = None
        self.setupUi(self)
        # 调用Drops方法
        self.setAcceptDrops(True)
        self.actionOpen.triggered.connect(self.SelDialog)

    def SelDialog(self):
        # 设置文件扩展名过滤,注意用双分号间隔
        filePath, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        print(filePath)

    # 鼠标进入
    def dragEnterEvent(self, evn):
        evn.accept()

    # 鼠标放开
    def dropEvent(self, evn):
        filePath = evn.mimeData().text().split("///")[1]
        print(filePath)
        if "." not in filePath:
            # TODO
            # 要把信息显示到窗口上
            print("这不是一个文件")
            return None

        with open(filePath, mode="rb") as file:
            if file is None:
                print("源文件打开出错啦！！")
            else:
                # print("开始读取PE文件的二进制格式内容...")
                self.content = file.read()
                # print(content)
                # print("二进制格式内容读取完毕，正在关闭文件...")
                file.close()
                # print("关闭成功^_^")

    # def CheckFile(self, filePath):
    #     tmp = None
    #     tmp = [e for e in self.EndName if e in filePath]
    #     print(tmp)
    #
    #     if not tmp:
    #         self.label.setText("这不是一个正确的文件o，请重新打开@_@")
    #         print("这不是一个文件")
    #     else:
    #         self.label.setText("正在加载，请稍后^_^")
    #         print("正在打开这个文件...")
    #         with open(filePath, mode="rb") as file:
    #             if file is None:
    #                 self.label.setText("源文件打开出错啦！！")
    #                 print("源文件打开出错啦！！")
    #             else:
    #                 self.content = file.read()
    #                 # print(self.content)
    #                 file.close()

    # 鼠标拖动
    def dragMoveEvent(self, evn):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    FirstWin = TipWin()
    FirstWin.show()
    sys.exit(app.exec_())
