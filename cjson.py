# coding: utf-8
import re
import json

# ---------------------------------------------------------------------------------------------------------------------
class Json(object):
    def __init__(self, data):
        self.data = data

    def _clean(self):
        ## re.search(",/s+,", self.data, re.DOTALL)

        while (self.data.find(",,") > 0):
            self.data = self.data.replace(",,", ",")

    def decode(self):
        self._clean()

        return json.loads( self.data )