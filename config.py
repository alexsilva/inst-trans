# coding: utf-8
import urllib

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
    translSource = "https://translate.google.com.br/translate_a/t"

    _translParams = [
        ("client", 't'),
        ("hl", 'pt-BR'), ## page locale
        ("sl", ''),      ## source translation
        ("tl", ''),      ## translation language
        ("q",  ''),      ## query translation
        ("ie", 'UTF-8'),
        ("oe", 'UTF-8'),
        ("multires", 1),
        ("prev", 'btn'),
        ("ssel", 0),
        ("tsel", 0),
        ("sc", 1)
    ]

    transOpts = [
        ('af', 'Afrikaans'),
        ('sq', 'Albanian'),
        ('ar', 'Arabic'),
        ('hy', 'Armenian'),
        ('az', 'Azerbaijani'),
        ('eu', 'Basque'),
        ('be', 'Belarusian'),
        ('bn', 'Bengali'),
        ('bs', 'Bosnian'),
        ('bg', 'Bulgarian'),
        ('ca', 'Catalan'),
        ('ceb', 'Cebuano'),
        ('zh-CN', 'Chinese (Simplified)'),
        ('zh-TW', 'Chinese (Traditional)'),
        ('hr', 'Croatian'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('nl', 'Dutch'),
        ('eo', 'Esperanto'),
        ('et', 'Estonian'),
        ('tl', 'Filipino'),
        ('fi', 'Finnish'),
        ('fr', 'French'),
        ('gl', 'Galician'),
        ('ka', 'Georgian'),
        ('de', 'German'), ('el', 'Greek'),
        ('gu', 'Gujarati'),
        ('ht', 'Haitian Creole'),
        ('iw', 'Hebrew'),
        ('hi', 'Hindi'),
        ('hmn', 'Hmong'),
        ('hu', 'Hungarian'),
        ('is', 'Icelandic'),
        ('id', 'Indonesian'),
        ('ga', 'Irish'),
        ('it', 'Italian'),
        ('ja', 'Japanese'),
        ('jw', 'Javanese'),
        ('kn', 'Kannada'),
        ('km', 'Khmer'),
        ('ko', 'Korean'),
        ('lo', 'Lao'),
        ('la', 'Latin'), ('lv', 'Latvian'),
        ('lt', 'Lithuanian'),
        ('mk', 'Macedonian'),
        ('ms', 'Malay'),
        ('mt', 'Maltese'),
        ('mr', 'Marathi'),
        ('no', 'Norwegian'),
        ('fa', 'Persian'),
        ('pl', 'Polish'),
        ('pt', 'Portuguese'),
        ('ro', 'Romanian'),
        ('ru', 'Russian'),
        ('sr', 'Serbian'),
        ('sk', 'Slovak'),
        ('sl', 'Slovenian'),
        ('es', 'Spanish'),
        ('sw', 'Swahili'),
        ('sv', 'Swedish'),
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('uk', 'Ukrainian'),
        ('ur', 'Urdu'),
        ('vi', 'Vietnamese'),
        ('cy', 'Welsh'),
        ('yi', 'Yiddish')
    ]

    @property
    def translParams(self):
        return dict(self._translParams)

    def __init__(self, tranlation):
        self.tranlation = tranlation

    def _createQuery(self):
        """
        Formats the query string in the format:
        application/x-www-form-urlencoded
        """
        params = self.translParams # to dict and cache

        params["q"]  = self.tranlation.query
        params["sl"] = self.tranlation.source
        params["tl"] = self.tranlation.target

        return urllib.urlencode( params )