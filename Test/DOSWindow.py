# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DOSWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DosWindow(object):
    def setupUi(self, DosWindow):
        DosWindow.setObjectName("DosWindow")
        DosWindow.resize(845, 710)
        DosWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(DosWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(730, 480, 93, 28))
        self.CloseButton.setObjectName("CloseButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 851, 691))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.CopyButton = QtWidgets.QPushButton(self.centralwidget)
        self.CopyButton.setGeometry(QtCore.QRect(730, 210, 93, 28))
        self.CopyButton.setAutoDefault(False)
        self.CopyButton.setDefault(False)
        self.CopyButton.setFlat(False)
        self.CopyButton.setObjectName("CopyButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(720, 260, 110, 30))
        self.textBrowser.setMinimumSize(QtCore.QSize(110, 30))
        self.textBrowser.setMaximumSize(QtCore.QSize(110, 30))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setAcceptRichText(False)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit.raise_()
        self.CloseButton.raise_()
        self.CopyButton.raise_()
        self.textBrowser.raise_()
        DosWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DosWindow)
        self.statusbar.setObjectName("statusbar")
        DosWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DosWindow)
        QtCore.QMetaObject.connectSlotsByName(DosWindow)

    def retranslateUi(self, DosWindow):
        _translate = QtCore.QCoreApplication.translate
        DosWindow.setWindowTitle(_translate("DosWindow", "IMAGE_DOS_HEADER"))
        self.CloseButton.setText(_translate("DosWindow", "Close"))
        self.CopyButton.setText(_translate("DosWindow", "拷贝"))
        self.CopyButton.setShortcut(_translate("DosWindow", "Ctrl+C"))
        self.textBrowser.setHtml(_translate("DosWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">123</p></body></html>"))
