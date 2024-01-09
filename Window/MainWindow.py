from PyQt5.QtWidgets import QMainWindow, QFileDialog
from Window.UI.Ui_MainWindow import Ui_MainWindow

WIDGET_STYLES_SHEET = """
    QWidget {
        background-image: url("Resources/ButtonDropBackground.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

# 文件信息模板 TODO 替换内容
FILE_INFO_TEMPLATE = """
=============================================================================
文件路径      ：{}
文件大小      ：xxxxx 字节
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
=============================================================================

完善信息展示。。。。。。。。。。。。。。。。。。。。。。。
"""

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)

        # 拖拽打开文件
        self.textBrowser.close()
        self.widgetOpenFile.show()
        self.widgetOpenFile.setStyleSheet(WIDGET_STYLES_SHEET)
        self.buttonDrop.clicked.connect(self.onButtonDropClicked)
        self.setAcceptDrops(True)

        # 菜单事件
        self.actionOpen.triggered.connect(self.onMenuOpenClicked)
        self.actionExit.triggered.connect(self.onMenuExitClicked)
        self.actionDosHeader.triggered.connect(self.app.openDosHeaderWindow)
        self.actionFileHeader.triggered.connect(self.app.openFileHeaderWindow)
        self.actionAbout.triggered.connect(self.app.openAboutWindow)

    # 鼠标进入
    def dragEnterEvent(self, event):
        event.accept()

    # 鼠标放开
    def dropEvent(self, event):
        filePath = event.mimeData().text().split("///")[1]
        if not self.app.parsePeFile(filePath):
            self.app.showTips("请选择正确格式的文件！")

    def onButtonDropClicked(self):
        self.onMenuOpenClicked()
        
    def onMenuOpenClicked(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        if filePath == "":
            return
        if not self.app.parsePeFile(filePath):
            self.app.showTips("请选择正确格式的文件！")
        
    def onMenuExitClicked(self):
        self.app.quit()

    def showFileInfo(self):
        self.textBrowser.show()
        self.widgetOpenFile.close()
        self.textBrowser.setText(FILE_INFO_TEMPLATE.format(self.app.filePath))
