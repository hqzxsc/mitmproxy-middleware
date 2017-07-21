#!/usr/bin/env python
# coding=utf-8

#中间件列表
MIDDLEWARE_CLASS = [
    "middleware.decrypt.DecryptMiddleware",
    "middleware.save_mongo.Save_Mongo_Middleware",
    "middleware.clear_view.ClearMiddleware",
    "middleware.xss.XssMiddleware",
    ]

FILTER_HOST = ['www.baidu.com',
               '192.168.4.10',
               ]

db_config = {
    "inter_data": {
        "host": "mongodb://test:123456@192.168.4.22:27017/inter_data",
    },
    "redis": {
        "main": {
            "host": "192.168.4.20",
            "port": 6379,
            "db": 0,
            "max_connections": 8
        },
    },
    "mysql": {
        "testdb": {
            "host": "192.168.4.21",
            "db": "testdb",
            "charset": "utf8",
            "user": "db_rw",
            "passwd": "db_rw",
            "cached": 12
        }
    },
}
