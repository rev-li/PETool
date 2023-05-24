import time
import traceback

from PyQt5 import QtCore

from DOSWindow import Ui_DosWindow
from DataWindow import Ui_DataDirectoryWindow
from FileWindow import Ui_FileWindow
from MainWinDow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import *

from OptionalWindow import Ui_OptionalWindow
from PEAnalyze import *


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.optwin = None
        self.filewin = None
        self.doswin = None
        self.datawin = None
        self.content = None
        self.lfanew = None
        self.setupUi(self)
        self.EndName = [".exe", ".dll", ".sys", ".ocx", ".com"]
        self.filePath = None
        # 调用Drops方法
        self.setAcceptDrops(True)
        self.actionOpen.triggered.connect(self.SelDialog)

    def SelDialog(self):
        # 设置文件扩展名过滤,注意用双分号间隔
        self.filePath, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                              "All Files (*);;Text Files (*.txt)")
        print(self.filePath)
        self.CheckFile(self.filePath)

    # 鼠标进入
    def dragEnterEvent(self, evn):
        evn.accept()

    # 鼠标放开
    def dropEvent(self, evn):
        self.filePath = evn.mimeData().text().split("///")[1]
        print(self.filePath)
        self.CheckFile(self.filePath)

    def CheckFile(self, filePath):
        tmp = None
        tmp = [e for e in self.EndName if e in filePath]
        print(tmp)

        if not tmp:
            # todo
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
                    self.lfanew = GetPeFileStart(self.content)
                    self.Operate()

    def Operate(self):
        self.doswin = DosWin(self.content)
        self.filewin = FileWin(self.lfanew, self.content)
        self.optwin = OptWin(self.lfanew, self.content)
        self.datawin = DataWin(self.lfanew, self.content)
        self.actionIMAGE_DOS_HEADER.triggered.connect(self.doswin.show)
        self.actionIMAGE_FILE_HEADER.triggered.connect(self.filewin.show)
        self.actionIMAGE_OPTIONAL_HEADER.triggered.connect(self.optwin.show)
        self.actionIMAGE_DATA_HEADER.triggered.connect(self.datawin.show)


class DosWin(QMainWindow, Ui_DosWindow):
    def __init__(self, cont):
        super(DosWin, self).__init__()
        self.content = None
        self.setupUi(self)
        self.Rewrite(cont)
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

    def Rewrite(self, content):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        IDH = Image_Dos_Header(content)

        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DosWindow", IDH.e_magic))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DosWindow", IDH.e_cblp))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DosWindow", IDH.e_cp))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("DosWindow", IDH.e_crlc))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("DosWindow", IDH.e_cparhdr))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("DosWindow", IDH.e_minalloc))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("DosWindow", IDH.e_maxalloc))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("DosWindow", IDH.e_ss))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("DosWindow", IDH.e_sp))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("DosWindow", IDH.e_csum))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("DosWindow", IDH.e_ip))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("DosWindow", IDH.e_cs))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("DosWindow", IDH.e_lfarlc))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("DosWindow", IDH.e_ovno))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("DosWindow", IDH.e_res))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("DosWindow", IDH.e_oemid))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("DosWindow", IDH.e_res2))
        item = self.tableWidget.item(17, 0)
        item.setText(_translate("DosWindow", IDH.e_lfanew))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


class FileWin(QMainWindow, Ui_FileWindow):
    def __init__(self, lfanew, cont):
        super(FileWin, self).__init__()
        self.content = None
        self.setupUi(self)
        self.ReWrite(lfanew, cont)
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

    def ReWrite(self, lfanew, cont):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        IFH = IMAGE_FILE_HEADER(lfanew, cont)

        item = self.tableWidget.item(0, 0)
        item.setText(_translate("FileWindow", IFH.Machine))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("FileWindow", IFH.NumberOfSections))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("FileWindow", IFH.TimeDateStamp))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("FileWindow", IFH.PointerToSymbolTable))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("FileWindow", IFH.NumberOfSymbols))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("FileWindow", IFH.SizeOfOptionalHeader))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("FileWindow", IFH.Characteristics))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


class OptWin(QMainWindow, Ui_OptionalWindow):
    def __init__(self, lfanew, cont):
        super(OptWin, self).__init__()
        self.content = None
        self.setupUi(self)
        self.ReWrite(lfanew, cont)
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

    def ReWrite(self, lfanew, cont):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        IOH = Image_Optional_Header(lfanew, cont)

        item = self.tableWidget.item(0, 0)
        item.setText(_translate("OptionalWindow", IOH.Magic))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("OptionalWindow", IOH.MajorLinkerVersion))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("OptionalWindow", IOH.MinorLinkerVersion))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfCode))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfImage))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfUninitializedData))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("OptionalWindow", IOH.AddressOfEntryPoint))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("OptionalWindow", IOH.BaseOfCode))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("OptionalWindow", IOH.BaseOfData))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("OptionalWindow", IOH.ImageBase))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("OptionalWindow", IOH.SectionAlignment))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("OptionalWindow", IOH.FileAlignment))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("OptionalWindow", IOH.MajorOperatingSystemVersion))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("OptionalWindow", IOH.MinorOperatingSystemVersion))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("OptionalWindow", IOH.MajorImageVersion))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("OptionalWindow", IOH.MinorImageVersion))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("OptionalWindow", IOH.MajorSubsystemVersion))
        item = self.tableWidget.item(17, 0)
        item.setText(_translate("OptionalWindow", IOH.MinorSubsystemVersion))
        item = self.tableWidget.item(18, 0)
        item.setText(_translate("OptionalWindow", IOH.Win32VersionValue))
        item = self.tableWidget.item(19, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfImage))
        item = self.tableWidget.item(20, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfHeaders))
        item = self.tableWidget.item(21, 0)
        item.setText(_translate("OptionalWindow", IOH.CheckSum))
        item = self.tableWidget.item(22, 0)
        item.setText(_translate("OptionalWindow", IOH.Subsystem))
        item = self.tableWidget.item(23, 0)
        item.setText(_translate("OptionalWindow", IOH.DllCharacteristics))
        item = self.tableWidget.item(24, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfStackReserve))
        item = self.tableWidget.item(25, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfStackCommit))
        item = self.tableWidget.item(26, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfHeapReserve))
        item = self.tableWidget.item(27, 0)
        item.setText(_translate("OptionalWindow", IOH.SizeOfHeapCommit))
        item = self.tableWidget.item(28, 0)
        item.setText(_translate("OptionalWindow", IOH.LoaderFlags))
        item = self.tableWidget.item(29, 0)
        item.setText(_translate("OptionalWindow", IOH.NumberOfRvaAndSizes))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


class DataWin(QMainWindow, Ui_DataDirectoryWindow):
    def __init__(self, lfanew, cont):
        super(DataWin, self).__init__()
        self.content = None
        self.setupUi(self)
        self.ReWrite(lfanew, cont)
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

    def ReWrite(self, lfanew, cont):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()

        IDH = Image_Data_Directory(lfanew, cont)

        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Export_Dir_VAddr))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Export_Dir_Size))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Import_Dir_VAddr))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Import_Dir_Size))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Reserved_Dir_VAddr))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Resource_Dir_Size))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Exeception_Dir_VAddr))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Exeception_Dir_Size))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Security_Dir_VAddr))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Security_Dir_Size))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.BaseReloc_Dir_VAddr))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.BaseReloc_Dir_Size))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Debug_Dir_VAddr))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Debug_Dir_Size))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.CopyRight_Dir_VAddr))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.CopyRight_Dir_Size))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.GlobalPtr_Dir_VAddr))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.GlobalPtr_Dir_Size))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Tls_Dir_VAddr))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Tls_Dir_Size))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.LoadConfig_Dir_VAddr))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.LoadConfig_Dir_Size))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.BoundImport_Dir_VAddr))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.BoundImport_Dir_Size))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.IAT_Dir_VAddr))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.IAT_Dir_Size))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.DelayImport_Dir_VAddr))
        item = self.tableWidget.item(13, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.DelayImport_Dir_Size))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.ComDescriptor_Dir_VAddr))
        item = self.tableWidget.item(14, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.ComDescriptor_Dir_Size))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("DataDirectoryWindow", IDH.Reserved_Dir_VAddr))
        item = self.tableWidget.item(15, 1)
        item.setText(_translate("DataDirectoryWindow", IDH.Reserved_Dir_Size))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Main()
    mainWin.show()
    sys.exit(app.exec_())
