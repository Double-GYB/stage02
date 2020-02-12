"""
chat room
env:python3
socket and fork exercise
"""

from socket import *

# 全局变量
ADDR = ('0.0.0.0',8888)


# 基本结构 （接收请求，分配任务）
def main():
    # udp服务端套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    # 循环接收请求
    while True:
        data,addr = s.recvfrom(1024)
        print("接收到的请求:",data.decode())
        # data --> 接收到的请求
        if data == 'jr':
            pass
        elif data == 'lt':
            pass

if __name__ == '__main__':
    main()