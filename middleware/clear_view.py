#!/usr/bin/env python
# coding: utf-8

"""
@version: v1.0
@author: Lieb
@contact: 2750416737@qq.com
@software: PyCharm
@file: clear_view.py
@time: 2017/7/4 11:11
"""


from conf import config
from mitmproxy import ctx


class ClearMiddleware:
    '''清理过多的view数据流中间件
        只对mitmweb模块生效
    '''

    def request(self, flow):
        if len(ctx.master.view._view) > 100:
            ctx.master.view.clear()
