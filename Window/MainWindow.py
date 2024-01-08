from Window.UI.Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog

stylesheet = """
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
        self.widgetOpenFile.setStyleSheet(stylesheet)
        self.buttonDrop.clicked.connect(self.onButtonDropClicked)
        self.setAcceptDrops(True)

        # 菜单事件
        self.actionOpen.triggered.connect(self.onMenuOpenClicked)
        self.actionExit.triggered.connect(self.onMenuExitClicked)
        self.actionDosHeader.triggered.connect(self.onMenuDosHeaderClicked)
        self.actionFileHeader.triggered.connect(self.onMenuFileHeaderClicked)

    # 鼠标进入
    def dragEnterEvent(self, event):
        event.accept()

    # 鼠标放开
    def dropEvent(self, event):
        filePath = event.mimeData().text().split("///")[1]
        print(filePath)

    def onButtonDropClicked(self):
        self.onMenuOpenClicked()
        
    def onMenuOpenClicked(self):
        file = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        print(file)
        
    def onMenuExitClicked(self):
        self.app.quit()

    # todo
    def onMenuDosHeaderClicked(self):
        pass

    def onMenuFileHeaderClicked(self):
        pass
