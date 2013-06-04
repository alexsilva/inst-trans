# coding: utf-8

import urllib2, urllib
from config import Config
from cjson import Json


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
