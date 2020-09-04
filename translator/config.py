# coding: utf-8
import urllib
import urllib2

from remote import Remote


# ---------------------------------------------------------------------------------------------------------------------
class Translation(object):
    """
    Sets the source language and target translation.

    """

    def __init__(self, query, source, target):
        """
        :param query: Word.
        :param source: Language of origin.
        :param target: Translation target.
        """
        self._source = source
        self._target = target
        self._query = query

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, q):
        self._query = q

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, src):
        self._source = src

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, tg):
        self._target = tg


# ---------------------------------------------------------------------------------------------------------------------
class Config(object):
    remote = Remote()

    def __init__(self, tranlation):
        self.tranlation = tranlation

    def _createQuery(self):
        """
        Formats the query string in the format:
        application/x-www-form-urlencoded
        """
        params = self.remote.params  # to dict and cache

        params["q"] = self.tranlation.query
        params["sl"] = self.tranlation.source
        params["tl"] = self.tranlation.target

        return urllib.urlencode(params)

    def getRequest(self):
        """
        Creates the request of translation joining all necessary parameters.
        return: urllib2 request object(urllib2.Request).
        """
        request = urllib2.Request(
            self.remote.source,
            data=self._createQuery(),
            headers=self.remote.headers
        )
        return request
