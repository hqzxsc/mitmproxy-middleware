#!/usr/bin/env python
# coding: utf-8

"""
@version: v1.0
@author: Lieb
@contact: 2750416737@qq.com
@software: PyCharm
@file: middleware.py
@time: 2017/6/19 16:22
"""
from conf import config
from mitmproxy import ctx
from lib import crypto
import json


class DecryptMiddleware:
    '''请求和响应数据解密中间件'''
    TYPE_DT1 = 'DT1'
    secret = None

    def get_decrypt(self, secret, content):
        data_cipher = crypto.new(DecryptMiddleware.TYPE_DT1, secret)
        try:
            return data_cipher.decrypt(content)
        except Exception as e:
            ctx.log.error('-------decrypt error')

    def get_secret(self,response):
        self.secret = json.loads(response.text).get('data').get('token').get('secret')

    def request(self, flow):
        req = flow.request
        if req.headers.get('Content-Type') and DecryptMiddleware.TYPE_DT1 in req.headers.get('Content-Type'):
            try:
                if self.secret:
                    content = self.get_decrypt(self.secret, req.raw_content)
                    if content:
                        ctx.log.info('{} request decrypt'.format(req.path.split("?")[0]))
                        flow.request.raw_content = content
                        flow.request.headers['Content-Type'] = "application/json;charset=UTF-8"
                        flow.request.path = flow.request.path.split('?')[0]
                else:
                    ctx.log.warn('-------not get secret')
            except Exception as e:
                ctx.log.error(e)

    def response(self, flow):
        req = flow.request
        res = flow.response
        if res.status_code == 200:
            if req.pretty_host in config.FILTER_HOST:
                if '/tool/gettoken' in req.path:
                    self.get_secret(res)
                    if not self.secret:
                        ctx.log.error('-------not get secret,please restart')
                if res.headers.get('Content-Type') and DecryptMiddleware.TYPE_DT1 in res.headers.get('Content-Type'):
                    if self.secret:
                        content = self.get_decrypt(self.secret, res.raw_content)
                        if content:
                            ctx.log.info('-------{} response decrypt'.format(req.path.split("?")[0]))
                            flow.response.raw_content = content
                    else:
                        ctx.log.warn('-------not secret')