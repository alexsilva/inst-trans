# coding: utf-8

import urllib2, urllib
from config import Config
from cjson import Json

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
        rel = {}
        try: d = self.data[1]
        except IndexError:
            d = []
        for i in d:
            if type(i) is list:
                try:
                    if isinstance(i[0], (str, unicode)):
                        rel[i[0]] = i[1]
                except IndexError:
                    continue
                try:
                    details = {}
                    for defs in i[-1]:
                        try:
                            word, _deflist = defs[0], defs[1]
                            details[word] = _deflist
                        except IndexError:
                            continue
                except Exception:
                    continue
                rel[i[0]].append({"details": details})
        return rel

    @property
    def related(self):
        rel = {}
        rel["simple"] = self.simple()
        rel["class"] = self.complex()
        return rel

# ---------------------------------------------------------------------------------------------------------------------
class Engine(object):
    """
    Handles all translation engine.
    """

    def __init__(self, config):
        self.config = config

    def trans(self):
        request = self.config.getRequest()

        sock = urllib2.urlopen( request )
        data = sock.read()
        sock.close()

        cjson = Json(data)

        return cjson.decode()
