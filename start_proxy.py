#!/usr/bin/env python
# coding: utf-8

"""
@version: v1.0
@author: Lieb
@contact: 2750416737@qq.com
@software: PyCharm
@file: db_util.py
@time: 2017/6/19 11:09
"""

import subprocess
import signal
from conf import config

config.MIDDLEWARE_CLASS.pop(0)


def main():
    def quit(signum, frame):
        print('You choose to stop me!')
        exit()
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)
    cmd = 'mitmweb -p 8888 --web-iface 0.0.0.0 --web-port 8081 --no-browser  -s script.py'
    proc = subprocess.Popen(cmd,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
    for line in iter(proc.stdout.readline, ""):
        print(line)

if __name__ == "__main__":
    # import pydevd

    # pydevd.settrace("192.168.12.66", port=5678, stdoutToServer=True, stderrToServer=True)
    main()
