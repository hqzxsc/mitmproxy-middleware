#!/usr/bin/env python
# coding: utf-8

"""
@version: v1.0
@author: Lieb
@contact: 2750416737@qq.com
@software: PyCharm
@file: save_mongo.py
@time: 2017/6/20 17:54
"""

from mitmproxy import ctx
import datetime
from lib import mongo_con
from conf import config


class Save_Mongo_Middleware:
    '''请求和响应数据保存到mongo中间件'''

    def response(self, flow):
        if flow.response.status_code == 200:
            if config.FILTER_HOST in flow.request.pretty_host:
                self.db_insert(flow)

    def db_insert(self, flow):
        mongo = mongo_con.MongoCon()
        insert_dict = {}
        if flow:
            path = flow.request.path.split('?')[0] if '?data_type=DT1' in flow.request.path else flow.request.path
            insert_dict = {
                'time': datetime.datetime.today(),
                'path': path,
                'request': {
                    'timestamp_start': flow.request.timestamp_start,
                    'timestamp_end': flow.request.timestamp_end,
                    'url': flow.request.url.split('?')[0],
                    'scheme': flow.request.scheme,
                    'path': path,
                    'method': flow.request.method,
                    'header': dict(flow.request.headers),
                    'content': flow.request.text
                },
                'response': {
                    'timestamp_start': flow.response.timestamp_start,
                    'timestamp_end': flow.response.timestamp_end,
                    'header': dict(flow.response.headers),
                    'content': flow.response.text
                }
            }
            ctx.log.info('-------{} update to mongo'.format(path))
            mongo.update('cbet', {'path': flow.request.path}, {"$set": insert_dict}, upsert=True)  # upsert无结果添加
