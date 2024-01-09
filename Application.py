import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

from Window.MainWindow import MainWindow
from Window.DosHeaderWindow import DosHeaderWindow
from Window.AboutWindow import AboutWindow

from PEAnalyze import *

class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)
        self.mainWindow = None
        self.dosHeaderWindow = None
        self.aboutWindow = None
        self.messageBox = None
        self.filePath = None
        self.fileContent = None
        self.lfanew = None

    def start(self):
        self.openMainWindow()
        sys.exit(self.exec_())

    def openMainWindow(self):
        self.mainWindow = MainWindow(self)
        self.mainWindow.show()

    def openDosHeaderWindow(self):
        if self.lfanew is None:
            self.showTips("请先打开PE文件！")
            return
        if self.dosHeaderWindow is None:
            self.dosHeaderWindow = DosHeaderWindow(self)
        self.dosHeaderWindow.show()

    # TODO
    def openFileHeaderWindow(self):
        if self.lfanew is None:
            self.showTips("请先打开PE文件！")
            return
        # if self.dosHeaderWindow is None:
        #     self.dosHeaderWindow = DosHeaderWindow(self)
        # self.dosHeaderWindow.show()

    def openAboutWindow(self):
        if self.aboutWindow is None:
            self.aboutWindow = AboutWindow(self)
        self.aboutWindow.show()

    def parsePeFile(self, filePath):
        # 校验文件格式
        allowedExtensions = [".exe", ".dll", ".sys", ".ocx", ".com"]
        _, extension = os.path.splitext(filePath)
        if extension.lower() not in allowedExtensions:
            return False
        
        # 解析文件
        with open(filePath, mode="rb") as file:
            if file is None:
                self.showTips("源文件打开出错啦！")
                return False
    
            self.filePath = filePath
            self.fileContent = file.read()
            file.close()
            self.lfanew = GetPeFileStart(self.fileContent)
            self.mainWindow.showFileInfo()
            return True
    
    # 弹出系统提示信息
    def showTips(self, content):
        self.messageBox = QMessageBox()
        self.messageBox.setWindowTitle("系统提示")
        self.messageBox.setText(content)
        self.messageBox.setIcon(QMessageBox.Information)
        self.messageBox.addButton(QMessageBox.Ok)
        self.messageBox.show()

if __name__ == "__main__":
    app = Application(sys.argv)
    app.start()