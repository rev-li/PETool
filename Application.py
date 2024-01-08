import sys
from PyQt5.QtWidgets import QApplication
from Window.MainWindow import MainWindow

class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)

    def start(self):
        self.mainWindow = MainWindow(self)
        self.mainWindow.show()
        sys.exit(self.exec_())

    def parsePEFile(filepath):
        pass

if __name__ == "__main__":
    app = Application(sys.argv)
    app.start()