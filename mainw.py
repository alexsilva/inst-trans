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

        self.queryTransl.returnPressed.connect(self.processTextTransl)
        self.btnTransl.clicked.connect(self.processTextTransl)

        # Connecting the interface events to the main thread.
        self._interface = interface.Interface()
        self._interface.start.connect(self.on_start)
        self._interface.end.connect(self.on_end)
        self._interface.error.connect(self.on_error)

    def on_start(self, value):
        print value

    def on_end(self, obj):
        transl = obj.get("simple", [])
        classes = obj.get("class", [])

        html = ['<h3>%s</h3>'%(': '.join(transl))]
        html.append('<hr>')

        for cls in classes:
            html.append('<p>%s</p>' % cls["name"])

            html.append('<ul>')
            for word in cls["words"]:
                html.append('<li>%s</li>'%word)
            html.append('</ul>')

            for word in cls["words"]:
                html.append('<strong>%s = </strong>'%word)
                text = '; '.join(cls["details"][word])
                html.append('<i>%s</i>'%text)
                html.append('<br/>')
        self.browserTransl.setHtml(u''.join(html))

    def on_error(self, value):
        print "on_error..."+value

    def processTextTransl(self, text=''):
        text = self.queryTransl.text()

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