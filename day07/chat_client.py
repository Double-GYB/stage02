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

    while True:
        name = input("请输入姓名:")
        msg = "L "+name  # 组织协议的格式
        s.sendto(msg.encode(),ADDR) # 发送请求
        data,addr = s.recvfrom(128) # 等待反馈结果
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print("该用户已存在")


if __name__ == '__main__':
    main()