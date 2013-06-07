# coding: utf-8

from PySide import QtGui, QtCore
from mainw_ui import Ui_mainWindow
from binding import interface
from html.style import Style
from html.tag import Tag

from db import models
from django.template.loader import get_template
from django.template import Context
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
        self._interface.start.connect(self.onStartTransl)
        self._interface.end.connect(self.onEndTransl)
        self._interface.error.connect(self.onErrorTransl)

    def onStartTransl(self, value):
        print value

    def onEndTransl(self, query):
        if not isinstance(query, models.Translation):
            return

        tmpl = get_template('translation.html')

        html = tmpl.render(Context({
            'queryset': query
        }))

        self.browserTransl.setHtml(html)

    def onErrorTransl(self, value):
        print "on_error..."+value

    def processTextTransl(self, text=''):
        text = self.queryTransl.text()

        try:
            query = models.Translation.objects.get(source=text)
        except models.Translation.DoesNotExist:
            query = None

        if query is None:
            job = interface.Job(text, self._interface)
            job.start()
        else:
            self.onEndTransl(query)

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