# coding: utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

import sys

from PySide import QtGui, QtCore
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

from binding import interface
from app import models
from mainw_ui import Ui_mainWindow

# ---------------------------------------------------------------------------------------------------------------------
Pixmap = QtGui.QPixmap


def pixmap(*args, **kwargs):
    """ Corrects images for the site due to errors in the ui file converter. """
    args = list(args)
    if isinstance(args[0], (str, unicode)):
        filename = os.path.basename(args[0])
        args[0] = os.path.join(settings.IMAGES_PATH, filename)
    return Pixmap(*args, **kwargs)


QtGui.QPixmap = pixmap


# ---------------------------------------------------------------------------------------------------------------------
class MainWindow(QtGui.QMainWindow):
    """
    Represents the main program window.
    """
    spinPath = os.path.join(settings.IMAGES_PATH, "spin-progress.gif")

    def __init__(self):
        super(MainWindow, self).__init__()

        self.uiMainWindow = Ui_mainWindow()
        self.uiMainWindow.setupUi(self)

        self.queryTransl.returnPressed.connect(self.processTextTransl)
        self.btnTransl.clicked.connect(self.processTextTransl)

        self.queryTransl.textChanged.connect(self.doFastTranslation)

        # Connecting the interface events to the main thread.
        self._interface = interface.Interface()
        self._interface.start.connect(self.onStartTransl)
        self._interface.end.connect(self.onEndTransl)
        self._interface.error.connect(self.onErrorTransl)

        self.progressMovie = QtGui.QMovie(self.spinPath)
        self.progressMovie.jumpToNextFrame()

        self.progress.setPixmap(self.progressMovie.currentPixmap())

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self._update)
        timer.start()

    def getTranslationQuery(self, text):
        try:
            query = models.Translation.objects.get(source=text)
        except models.Translation.DoesNotExist:
            query = None
        return query

    def doFastTranslation(self, text):
        if self.getTranslationQuery(text.strip()) is not None:
            self.processTextTransl()

    def _update(self):
        self.progress.setPixmap(self.progressMovie.currentPixmap())

    def onStartTransl(self, value):
        self.progressMovie.start()
        print value

    def onEndTransl(self, query):
        self.progressMovie.stop()

        if not isinstance(query, models.Translation):
            return

        tmpl = get_template('translation.html')

        html = tmpl.render(Context({
            'queryset': query
        }))

        self.browserTransl.setHtml(html)

    def onErrorTransl(self, value):
        self.progressMovie.stop()
        print "Error: " + value

    def processTextTransl(self, text=''):
        self.progressMovie.jumpToNextFrame()
        text = self.queryTransl.text().strip()

        query = self.getTranslationQuery(text)

        if query is None:
            job = interface.Job(text, self._interface)
            job.start()
        else:
            self.onEndTransl(query)

    def __getattr__(self, name):
        """ Shortens the call attributes ui for self object. """
        attr = (getattr(self.uiMainWindow, name) if hasattr(self.uiMainWindow, name)
                else super(MainWindow, self).__getattr__(name))
        return attr


# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainw = MainWindow()
    mainw.show()

    sys.exit(app.exec_())
