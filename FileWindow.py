# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileWindow(object):
    def setupUi(self, FileWindow):
        FileWindow.setObjectName("FileWindow")
        FileWindow.resize(600, 290)
        FileWindow.setMinimumSize(QtCore.QSize(600, 290))
        FileWindow.setMaximumSize(QtCore.QSize(600, 290))
        self.centralwidget = QtWidgets.QWidget(FileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 600, 290))
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 290))
        self.tableWidget.setMaximumSize(QtCore.QSize(600, 280))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(7)
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
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.CopyButton = QtWidgets.QPushButton(self.centralwidget)
        self.CopyButton.setGeometry(QtCore.QRect(470, 70, 93, 28))
        self.CopyButton.setObjectName("CopyButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(440, 130, 151, 141))
        self.textBrowser.setObjectName("textBrowser")
        FileWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FileWindow)
        QtCore.QMetaObject.connectSlotsByName(FileWindow)

    def retranslateUi(self, FileWindow):
        _translate = QtCore.QCoreApplication.translate
        FileWindow.setWindowTitle(_translate("FileWindow", "IMAGE_FILE_HEADER"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("FileWindow", "Machine"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("FileWindow", "NumberOfSections"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("FileWindow", "TimeDataStamp"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("FileWindow", "PointOfSymbolTable"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("FileWindow", "NumberOfSymbols"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("FileWindow", "SizeOfOptionHeader"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("FileWindow", "Characteristics"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FileWindow", "Content"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FileWindow", "Size"))
        self.CopyButton.setText(_translate("FileWindow", "Copy"))
