# coding=utf-8
from google.cloud import translate_v2 as translate

from translator.backends import BaseBackend


class GoogleBackend(BaseBackend):

    def __init__(self):
        self.client = translate.Client()

    def translate(self, text, source=None, target=None, **kwargs):
        result = self.client.translate(text,
                                       source_language=source,
                                       target_language=target,
                                       **kwargs)
        return result
