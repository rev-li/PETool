from Window.UI.Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.actionExit.triggered.connect(self.close)