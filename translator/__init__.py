# coding: utf-8
__author__ = 'alex'

import urllib2

from cjson import Json
from config import Config


# ---------------------------------------------------------------------------------------------------------------------
class Groups(object):
    def __init__(self, data):
        self.data = data

    def simple(self):
        try:
            d = self.data[0][0]
            d = [i for i in d if i]
        except IndexError:
            d = []
        d.reverse()
        return d

    def complex(self):
        group = []
        try:
            d = self.data[1]
        except IndexError:
            d = []
        for i in d:
            if type(i) is list:
                rel = {}
                try:
                    if isinstance(i[0], (str, unicode)):
                        rel["name"] = i[0]
                        rel["words"] = i[1]
                except IndexError:
                    continue
                rel["details"] = {}
                try:
                    for defs in i[-1]:
                        try:
                            word, deflist = defs[0], defs[1]
                            rel["details"][word] = deflist
                        except IndexError:
                            continue
                except Exception:
                    pass
                group.append(rel)
        return group

    @property
    def related(self):
        rel = {
            "simple": self.simple(),
            "class": self.complex()
        }
        return rel


# ---------------------------------------------------------------------------------------------------------------------
class Engine(object):
    """
    Handles all translation engine.
    """

    def __init__(self, config):
        self.config = config

    def transl(self):
        """
        returns translations in the form of dictionaries.

        where the keys:
         simple: it is the translation of the text in the form of a list.
         class: the set of grammatical class.
          - name: the name of the class.
          - words: words of grammatical class.
          - details: details of each word
        """
        request = self.config.getRequest()

        sock = urllib2.urlopen(request)
        data = sock.read()
        sock.close()

        cjson = Json(data)
        groups = Groups(cjson.decode())

        return groups.related
