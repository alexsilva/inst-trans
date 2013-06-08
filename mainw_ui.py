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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Fri Jun 07 23:12:00 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.progress = QtGui.QWidget(self.centralwidget)
        self.progress.setObjectName("progress")
        self.horizontalLayout.addWidget(self.progress)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Fri Jun 07 23:48:30 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.progress = QtGui.QLabel(self.centralwidget)
        self.progress.setObjectName("progress")
        self.horizontalLayout.addWidget(self.progress)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:00:29 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 2, 7, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:01:02 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 2, 7, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:02:27 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 2, 7, 7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:02:47 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 2, 7, 4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:03:24 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:23:16 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(4, 2, 4, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:25:41 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:26:49 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:27:59 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("pressed()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("pressed()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:29:33 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:33:25 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"background-color: rgb(0, 255, 255);")
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:47:48 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 255, 172, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:55:22 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(83, 171, 198, 248), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(4)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 00:55:41 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(83, 171, 198, 248), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 01:04:46 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(83, 171, 198, 248), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 01:05:31 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(83, 171, 198, 248), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 01:05:59 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(83, 171, 198, 248), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created: Sat Jun 08 01:06:06 2013
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
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtGui.QPushButton(self.centralwidget)
        self.btnBack.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/btnback-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.btnForward = QtGui.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/btnforward-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName("btnForward")
        self.horizontalLayout.addWidget(self.btnForward)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(83, 171, 198, 248), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.horizontalLayout_2.addWidget(self.progress)
        self.horizontalLayout.addWidget(self.frame)
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
        self.browserTransl.setFrameShape(QtGui.QFrame.Box)
        self.browserTransl.setFrameShadow(QtGui.QFrame.Sunken)
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
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL("clicked()"), self.browserTransl.backward)
        QtCore.QObject.connect(self.btnForward, QtCore.SIGNAL("clicked()"), self.browserTransl.forward)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Instant translator", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setText(QtGui.QApplication.translate("mainWindow", "....", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTransl.setText(QtGui.QApplication.translate("mainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.browserTransl.setHtml(QtGui.QApplication.translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

