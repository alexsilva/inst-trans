# coding=utf-8

class BaseBackend:
    def translate(self, text, source=None, target=None, **kwargs):
        raise NotImplementedError