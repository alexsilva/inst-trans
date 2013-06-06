# coding: utf-8

from PySide import QtGui, QtCore
from mainw_ui import Ui_mainWindow
from binding import interface
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

        # Connecting the interface events to the main thread.
        self._interface = interface.Interface()
        self._interface.start.connect(self.on_start)
        self._interface.end.connect(self.on_end)
        self._interface.error.connect(self.on_error)

    def on_start(self, value):
        print "on_start..."+value

    def on_end(self, value):
        print "on_end..."+value

    def on_error(self, value):
        print "on_error..."+value

    def processTextTransl(self, text=''):
        text = self.queryTransl.text()

        #self.browserTransl.setHtml('<h3 style="color:blue;">%s</3>'%text)

        job = interface.Job(text, self._interface)
        job.start()

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