"""
select_server.py 服务
重点代码

【1】将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表，确定就绪IO事件
【4】处理发生的IO事件
"""

from socket import *
from select import select


# 创建监听套接字
s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

# 设置关注列表
rlist = [s]  # 处理客户端链接
wlist = []
xlist = []

while True:
    print("等待处理IO.....")
    rs,ws,xs = select(rlist,wlist,xlist)

    # 遍历返回值列表，看看是哪个IO就绪了
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("Connect from",addr)
            rlist.append(c) # 将对应的客户端链接套接字加入列表
        else:
            # 如果r遍历到客户端链接套接字说明： 有客户端给我发消息
            data = r.recv(1024)
            if not data:
                break
            print(data.decode())
            r.send(b'OK')

    for w in ws:
        pass

    for x in xs:
        pass














