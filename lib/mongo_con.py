#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: Lieb
@contact: 2750416737@qq.com
@software: PyCharm
@file: mongo_con.py
@time: 2017/6/20 20:43
"""


import traceback
from pymongo import *
from conf import config


class MongoCon(object):
    """mongodb connect
    """
    def __init__(self):
        client = MongoClient(**config.db_config['inter_data'])
        self.db = client['inter_data']

    def find(self, table, SON=None, pn=0, rn=0, sort=None, count=False, projection=None):
        try:
            data = []
            col = collection.Collection(self.db, table)
            cur = col.find(filter=SON,projection=projection, skip=pn*rn, limit=rn, sort=sort)
            for doc in cur:
                data.append(doc)
            return data
        except Exception as e:
            print(traceback.format_exc())

    def insert(self, table, DOC):
        ret = None
        try:
            col = collection.Collection(self.db, table)
            if isinstance(DOC, dict):
                ret = col.insert_one(DOC)
            elif isinstance(DOC, list):
                ret = col.insert_many(DOC)
        except Exception as e:
            print(traceback.format_exc())
        finally:
            return ret

    def update(self, table, SON, DOC, upsert=False, multi=False):
        try:
            col = collection.Collection(self.db, table)
            if not multi:
                col.update_one(SON, DOC, upsert)
            else:
                col.update_many(SON, DOC, upsert)
        except Exception as e:
            print(traceback.format_exc())

    def remove(self, table, DOC, multi=True):
        try:
            col = collection.Collection(self.db, table)
            if not multi:
                col.delete_one(DOC)
            else:
                col.delete_many(DOC)
        except Exception as e:
            print(traceback.format_exc())



