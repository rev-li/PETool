# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataDirectoryWindow(object):
    def setupUi(self, DataDirectoryWindow):
        DataDirectoryWindow.setObjectName("DataDirectoryWindow")
        DataDirectoryWindow.resize(649, 466)
        self.centralwidget = QtWidgets.QWidget(DataDirectoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 1, item)
        self.CopyButton = QtWidgets.QPushButton(self.centralwidget)
        self.CopyButton.setGeometry(QtCore.QRect(480, 100, 93, 28))
        self.CopyButton.setObjectName("CopyButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 140, 141, 101))
        self.label.setText("")
        self.label.setObjectName("label")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(480, 360, 93, 28))
        self.ExitButton.setObjectName("ExitButton")
        DataDirectoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataDirectoryWindow)
        QtCore.QMetaObject.connectSlotsByName(DataDirectoryWindow)

    def retranslateUi(self, DataDirectoryWindow):
        _translate = QtCore.QCoreApplication.translate
        DataDirectoryWindow.setWindowTitle(_translate("DataDirectoryWindow", "DATA_DIRECTRY"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("DataDirectoryWindow", "Export_Dir"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("DataDirectoryWindow", "Import_Dir"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("DataDirectoryWindow", "Resource_Dir"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("DataDirectoryWindow", "Exeception_Dir"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("DataDirectoryWindow", "Security_Dir"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("DataDirectoryWindow", "BaseReloc_Dir"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("DataDirectoryWindow", "Debug_Dir"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("DataDirectoryWindow", "CopyRight_Dir"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("DataDirectoryWindow", "GlobalPtr_Dir"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("DataDirectoryWindow", "Tls_Dir"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("DataDirectoryWindow", "LoadConfig_Dir"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("DataDirectoryWindow", "BoundImport_Dir"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("DataDirectoryWindow", "IAT_Dir"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("DataDirectoryWindow", "DelayImport_Dir"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("DataDirectoryWindow", "ComDescriptor_Dir"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("DataDirectoryWindow", "Reserved_Dir"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DataDirectoryWindow", "VirtualAddress"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DataDirectoryWindow", "Size"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("DataDirectoryWindow", "  "))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(13, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(14, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("DataDirectoryWindow", " "))
        item = self.tableWidget.item(15, 1)
        item.setText(_translate("DataDirectoryWindow", " "))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.CopyButton.setText(_translate("DataDirectoryWindow", "Copy"))
        self.ExitButton.setText(_translate("DataDirectoryWindow", "Exit"))
