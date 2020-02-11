"""
搭建一个http服务，当浏览器发起请求的时候向浏览器发送 index.html 网页

* 将http处理部分封装为函数
* 分析请求内容，如果请求内容是 / 则响应 index.html网页
  如果请求内容是其他的则响应404

思路：参考http_test,将响应体改为index.html内容即可
     如果分析响应内容则使用split函数切割获取响应内容，看看是不是/
"""

from socket import *

# 创建套接字
s = socket()
s.bind(('127.0.0.1',8000))
s.listen(3)

# 等待客户端（浏览器）链接
c,addr = s.accept()
print("Connect from",addr)

# http请求
data = c.recv(2048)
print(data.decode())


# 设计响应
f = open('index.html')

data = "HTTP/1.1 200 OK\r\n"
data += "Content-Type:text/html\r\n"
data += "\r\n"
data += f.read()


c.send(data.encode())

c.close()
s.close()