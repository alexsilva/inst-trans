# coding: utf-8

from PySide import QtGui, QtCore
from mainw_ui import Ui_mainWindow
from binding import interface
from html.style import Style
from html.tag import Tag

from db import models
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

    def cacheTransl(self, simple, cls):
        """"""
        transl = models.Translation(
            source=simple[0],
            target=simple[1],
            sourceLocale='en',
            targetLocale='pt'
        )
        transl.save()

        for _cls in cls:
            gc = models.GrammaticalClass(name=_cls["name"], translation=transl)
            gc.save()

            for _word in _cls['words']:
                word = models.Word(word=_word, grammaticalClass=gc)
                word.save()

    def on_end(self, obj=None, query=None):
        if not obj is None:
            transl = obj.get("simple", [])
            classes = obj.get("class", [])

            q = models.Translation.objects.filter(source=transl[0])

            if len(transl) > 1 and q.count() == 0:
                self.cacheTransl(transl, classes)

        elif not query is None:
            transl = query.simple
            classes = []#query.grammaticalclass_set.all()
            print 'using cache...'

        # ---------------------------------------------------------------------
        div = Tag(type='div', content=[])

        h2 = Tag(type='h2', content=[])
        h2['content'] = ': '.join(transl)
        h2['style'] = Style(color="blue")

        div['content'].append(h2)
        div['content'].append(Tag(type='hr'))

        for cls in classes:
            h3 = Tag(type='h3', content=cls["name"])
            h3['style'] = Style(color='#00FFFF')
            div['content'].append(h3)

            ul = Tag(type='ul', content=[])

            for index, word in enumerate(cls["words"]):
                li = Tag(type='li')
                li['content'] = Tag(type="a", attr={'href': "#"+word.replace(' ', '-')}, content=word)
                ul['content'].append(li)

            div['content'].append(ul)

            for index, word in enumerate(cls["words"]):
                strong = Tag(type="strong", content="%s =" % word)

                details_div = Tag(type='div', attr={'id': word.replace(' ', '-')}, content=[])
                details_div['content'].append(strong)

                i = Tag(type="i", content='; '.join(cls["details"][word]))
                details_div['content'].append(i)

                div['content'].append(details_div)
        self.browserTransl.setHtml(unicode(div))

    def on_error(self, value):
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
            self.on_end(query=query)

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