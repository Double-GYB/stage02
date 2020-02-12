"""
chat room 客户端
发送请求，得到结果
"""

from socket import *
import os

# 服务端地址
ADDR = ('127.0.0.1',8888)

# 启动函数 -->  向服务端发送初始请求
def main():
    # udp 客户端
    s = socket(AF_INET,SOCK_DGRAM)

    s.sendto(b"request",ADDR)

if __name__ == '__main__':
    main()