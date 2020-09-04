# coding: utf-8
import json


# ---------------------------------------------------------------------------------------------------------------------
class Json(object):
    """
    Corrects and decodes the data in json.
    """

    def __init__(self, data):
        self.data = data

    def _clean(self):
        while self.data.find(",,") > 0:
            self.data = self.data.replace(",,", ",")

    def decode(self):
        self._clean()

        return json.loads(self.data)
