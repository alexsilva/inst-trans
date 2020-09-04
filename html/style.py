# coding: utf-8

# ---------------------------------------------------------------------------------------------------------------------
class Style(object):
    """
    """

    def __init__(self, **params):
        self.params = params

    def __setitem__(self, key, value):
        self.params[key] = value

    def __str__(self):
        rules = ["{0}:{1}".format(*args) for args in self.params.items()]
        rules = ";".join(rules)
        return 'style="{rules}"'.format(rules=rules)

    def __unicode__(self):
        return self.__class__.__str__(self).decode("utf-8")

# ---------------------------------------------------------------------------------------------------------------------
