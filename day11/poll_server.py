"""
poll 方法实践
"""
from socket import *
from select import *


# 创建套接字作为监控对象
s = socket()
s.bind(("0.0.0.0",8888))
s.listen(5)

# 关注s
p = poll()
p.register(s,POLLIN)

# 建立查找字典 时刻与register保持一直
fdmap = {s.fileno():s}

# 提交监控
while True:
    print("等待IO发生....")
    events = p.poll()
    for fd,event in events:
        print(fd,event)

