# mitmproxy-middleware
扩展mitmproxy，封装代理拦截中间件

# 依赖环境
python3.6
mitmproxy2.0.2

# 使用 
编写中间件拦截http流量，可以做mock、数据解码、xss安全测试等，middlerware文件夹里已写几个简单的中间件例子供参考，后期可增加对tcp、websocket流量的拦截。

命令行输入：mitmweb -s script.py 或者直接python start_proxy.py运行
