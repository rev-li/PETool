from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog
from Window.UI.Ui_DosHeaderWindow import Ui_DosHeaderWindow

from PEAnalyze import Image_Dos_Header

class DosHeaderWindow(QMainWindow, Ui_DosHeaderWindow):
    def __init__(self, app):
        super(DosHeaderWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.Rewrite()

    def Rewrite(self):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        IDH = Image_Dos_Header(self.app.fileContent)

        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_magic))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_cblp))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_cp))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_crlc))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_cparhdr))
        item = self.tableWidget.item(5, 0)
        # item.setText(_translate("DosHeaderWindow", IDH.e_minalloc))
        # item = self.tableWidget.item(6, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_maxalloc))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_ss))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_sp))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_csum))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_ip))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_cs))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_lfarlc))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_ovno))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_res))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_oemid))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_res2))
        item = self.tableWidget.item(17, 0)
        item.setText(_translate("DosHeaderWindow", IDH.e_lfanew))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # 调整列宽
        self.tableWidget.resizeColumnsToContents()
