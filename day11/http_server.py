"""
httpserver 2.0
io多路服用，类封装练习
"""

from socket import *
from select import *

# 具体功能实现
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port = port
        self.dir = dir



if __name__ == '__main__':
    """
    希望通过使用这个类，可以快速搭建一个服务，展示我的网页
    """
    # 用户自己决定的内容
    HOST = '0.0.0.0'
    PORT = 8888
    DIR = "./static"
    # 实例化对象 --》 对象调用方法实现具体功能
    httpd = HTTPServer(HOST,PORT,DIR)
    httpd.serve_forever() # 启动服务