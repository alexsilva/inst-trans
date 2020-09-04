# coding: utf-8
import inspect
from .backends import BaseBackend

__author__ = 'alex'


class Engine(object):
    """
    Handles all translation engine.
    """

    def __init__(self, backends, **options):
        self.backends = backends
        self.options = options

    def load_backends(self):
        backends = []
        for backend in self.backends:
            package, module_name = backend.rsplit('.', 1)
            module = __import__(package,
                                globals=globals(),
                                locals=locals(),
                                fromlist=[module_name])
            module = getattr(module, module_name)
            for name in dir(module):
                _class_obj = getattr(module, name)
                if inspect.isclass(_class_obj) and \
                        _class_obj is not BaseBackend and \
                        issubclass(_class_obj, BaseBackend):
                    backends.append(_class_obj())
        return backends

    def translate(self, text, source=None, target=None, **kwargs):
        """returns translations in the form of dictionaries"""
        backends = self.load_backends()

        results = []
        for backend in backends:
            result = backend.translate(text,
                                       source=source,
                                       target=target,
                                       **kwargs)
            results.append({
                backend: result
            })
        return results
