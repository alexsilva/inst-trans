# coding: utf-8

from PySide import QtGui, QtCore
from mainw_ui import Ui_mainWindow

import sys

# ---------------------------------------------------------------------------------------------------------------------
class MainWindow(QtGui.QMainWindow):
    """
    Represents the main program window.
    """

    def __init__(self):
        super(MainWindow, self).__init__()

        self.uiMainWindow = Ui_mainWindow()
        self.uiMainWindow.setupUi(self)

        self.queryTransl.textChanged.connect(self.processTextTransl)
        self.btnTransl.clicked.connect(self.processTextTransl)

    def processTextTransl(self, text=''):
        text = self.queryTransl.text()

        self.browserTransl.setHtml('<h3 style="color:blue;">%s</3>'%text)

    def __getattr__(self, name):
        """ Shortens the call attributes ui for self object. """
        attr = (getattr(self.uiMainWindow, name) if hasattr(self.uiMainWindow, name)
                else super(MainWindow,self).__getattr__(name))
        return attr


# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainw = MainWindow()
    mainw.show()

    sys.exit(app.exec_())