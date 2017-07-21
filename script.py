#coding=utf-8
'''mitmproxy2.02'''
from mitmproxy import http,ctx
from middleware import Manager
from conf import config
import os
import sys

os.environ['BASIC_PATH'] = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.environ['BASIC_PATH'])

        
class Customer:
    def __init__(self):
        self.m = Manager()
        if config.MIDDLEWARE_CLASS:
            self.m.register_all(config.MIDDLEWARE_CLASS)

    def response(self,flow: http.HTTPFlow) -> None:
        self.m.run_response(flow)

                
    def request(self,flow: http.HTTPFlow) -> None:
        self.m.run_request(flow)
    
    def websocket_handshake(self, f):
        pass

    def websocket_start(self, flow):
        pass

    def websocket_message(self, flow):
        pass

    def websocket_error(self, flow):
        pass

    def websocket_end(self, flow):
        pass


def start():
    '''main func'''
    return Customer()
