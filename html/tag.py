# coding: utf-8

# ---------------------------------------------------------------------------------------------------------------------
class Tag(object):
    """
    type:
    style:
    content:
    """

    _str_repr = '<{type}{space}{style}>{eol}{content}{eol}</{type}>'
    _unicode_repr = u'<{type}{space}{style}>{eol}{content}{eol}</{type}>'

    def __init__(self, **params):
        self.params = params

        self.params['content'] = params.get('content', [])
        self.params['style'] = params.get('style', "")
        self.params['space'] = params.get('space', " ")
        self.params['eol'] = params.get('eol', "\n")

    def __setitem__(self, key, value):
        self.params[key] = value

    def __getitem__(self, key):
        return self.params[key]

    def __convert(self, _u_str, method):
        if type(self.params['content']) is list:
            self.params['content'] = [method(item) for item in self.params['content']]
            self.params['content'] = _u_str.join(self.params['content'])

    def __str__(self):
        self.__convert('', str)
        return self._str_repr.format(**self.params)

    def __unicode__(self):
        self.__convert(u'', lambda v: u'%s' % v)
        return self._unicode_repr.format(**self.params)

# ---------------------------------------------------------------------------------------------------------------------