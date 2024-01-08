from PyQt5.QtWidgets import QMainWindow, QFileDialog
from Window.UI.Ui_MainWindow import Ui_MainWindow
from Window.AboutWindow import AboutWindow

WIDGET_STYLES_SHEET = """
    QWidget {
        background-image: url("Resources/ButtonDropBackground.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
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
        self.actionDosHeader.triggered.connect(self.onMenuDosHeaderClicked)
        self.actionFileHeader.triggered.connect(self.onMenuFileHeaderClicked)
        self.actionAbout.triggered.connect(self.onMenuAboutClicked)

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
        if not self.app.parsePeFile(filePath):
            self.app.showTips("请选择正确格式的文件！")
        
    def onMenuExitClicked(self):
        self.app.quit()

    # todo
    def onMenuDosHeaderClicked(self):
        pass

    # todo
    def onMenuFileHeaderClicked(self):
        pass

    # 打开关于信息弹窗
    def onMenuAboutClicked(self):
        aboutWindow = AboutWindow(self.app)
        aboutWindow.show()

    def showFileInfo(self, fileInfo):
        self.textBrowser.show()
        self.widgetOpenFile.close()
        self.textBrowser.setText(fileInfo)
