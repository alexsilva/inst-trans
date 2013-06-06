# coding: utf-8
from PySide import QtCore
import threading

class Interface(threading.Thread, QtCore.QObject):
    """
     The interface makes processing occurs outside the main thread and allows you
    to return the reply by issuing the event generated by the signal.
    """
    onProcess = QtCore.Signal(str)

    def run(self, text):
        self.onProcess.emit('')