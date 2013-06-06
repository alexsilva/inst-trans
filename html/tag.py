# coding: utf-8

# ---------------------------------------------------------------------------------------------------------------------
class Tag(object):
    """
    type:
    style:
    content:
    """

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

    def __str__(self):
        if type(self.params['content']) is list:
            self.params['content'] = [str(t) for t in self.params['content']]
            self.params['content'] = ''.join(self.params['content'])
        return '<{type}{space}{style}>{eol}{content}{eol}</{type}>'.format(**self.params)

    def __unicode__(self):
        if type(self.params['content']) is list:
            self.params['content'] = [u"%s"%t for t in self.params['content']]
            self.params['content'] = u''.join(self.params['content'])
        return u'<{type}{space}{style}>{eol}{content}{eol}</{type}>'.format(**self.params)

# ---------------------------------------------------------------------------------------------------------------------