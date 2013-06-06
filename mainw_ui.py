# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Wed Jun 05 20:02:13 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(699, 290)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.queryTransl = QtGui.QLineEdit(self.centralwidget)
        self.queryTransl.setObjectName("queryTransl")
        self.horizontalLayout.addWidget(self.queryTransl)
        self.btnTransl = QtGui.QPushButton(self.centralwidget)
        self.btnTransl.setObjectName("btnTransl")
        self.horizontalLayout.addWidget(self.btnTransl)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.browserTransl = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.browserTransl.sizePolicy().hasHeightForWidth())
        self.browserTransl.setSizePolicy(sizePolicy)
        self.browserTransl.setObjectName("browserTransl")
        self.verticalLayout.addWidget(self.browserTransl)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

