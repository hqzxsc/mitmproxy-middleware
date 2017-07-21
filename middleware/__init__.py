#!/usr/bin/env python
# coding: utf-8

"""
@version: v1.0
@author: Lieb
@contact: 2750416737@qq.com
@software: PyCharm
@file: __init__.py
@time: 2017/6/19 15:55
"""

from collections import deque


class Manager(object):
    def __init__(self):
        self._REQUEST_LIST = deque()
        self._RESPONSE_LIST = deque()

    def register(self, name):
        if isinstance(name, str):
            name = self.import_object(name)
        obj = name()

        if self._ismd(obj, 'request'):
            self._REQUEST_LIST.append(obj.request)

        if self._ismd(obj, 'response'):
            self._RESPONSE_LIST.append(obj.response)

    def _ismd(self, obj, method_name):
        m = getattr(obj, method_name, None)
        return m and callable(m)

    def import_object(self, name):
        """Imports an object by name.
        """
        if name.count('.') == 0:
            return __import__(name, None, None)

        parts = name.split('.')
        obj = __import__('.'.join(parts[:-1]), None, None, [parts[-1]], 0)
        try:
            return getattr(obj, parts[-1])
        except AttributeError:
            raise ImportError("No module named %s" % parts[-1])

    def register_all(self, names):
        if not names:
            names = ()

        for midd_class in names:
            self.register(midd_class)

    def _execute(self, flow, obj, *args, **kwargs):
        for fun in obj:
            fun(flow)

    def run_request(self, flow, *args, **kwargs):
        self._execute(flow, self._REQUEST_LIST)

    def run_response(self, flow, *args, **kwargs):
        self._execute(flow, self._RESPONSE_LIST)
