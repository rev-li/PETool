import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from Window.MainWindow import MainWindow
from PEAnalyze import *

# 文件信息模板 TODO 替换内容
FILE_INFO_TEMPLATE = """
================================================================================
文件路径      ：{}
文件大小      ：37376 字节
创建时间      ：2024.01.01 15:29:39
修改时间      ：2024.01.01 15:29:39
访问时间      ：2024.01.09 01:56:54
运行平台      ：Win32 位
PE文件头地址  ：0x000000E8
基地址        ：0x00400000
入口点EP(RVA) ：0x000011A0
入口点OEP(RAW)：0x00000000
入口点EP所在节：超出范围
入口点EP首字节：4D 5A 90 00 03 00 00 00 
区段数目      ：4 个
链接器版本信息：9.0
子系统        ：Windows 控制台/字符子系统
================================================================================


================================================================================
文件路径      ：
文件大小      ：37376 字节
创建时间      ：2024.01.01 15:29:39
修改时间      ：2024.01.01 15:29:39
访问时间      ：2024.01.09 01:56:54
运行平台      ：Win32 位
PE文件头地址  ：0x000000E8
基地址        ：0x00400000
入口点EP(RVA) ：0x000011A0
入口点OEP(RAW)：0x00000000
入口点EP所在节：超出范围
入口点EP首字节：4D 5A 90 00 03 00 00 00 
区段数目      ：4 个
链接器版本信息：9.0
子系统        ：Windows 控制台/字符子系统
================================================================================
"""

class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)
        self.mainWindow = None
        self.filePath = None
        self.fileContent = None
        self.lfanew = None

    def start(self):
        self.openMainWindow()
        sys.exit(self.exec_())

    def openMainWindow(self):
        self.mainWindow = MainWindow(self)
        self.mainWindow.show()

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
            self.mainWindow.showFileInfo(FILE_INFO_TEMPLATE.format(self.filePath))
            return True
    
    # 弹出系统提示信息
    def showTips(self, content):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("系统提示")
        messageBox.setText(content)
        messageBox.setIcon(QMessageBox.Information)
        messageBox.addButton(QMessageBox.Ok)
        messageBox.exec_()

if __name__ == "__main__":
    app = Application(sys.argv)
    app.start()