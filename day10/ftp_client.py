"""
ftp 客户端
"""
from socket import *
import sys

# 全局变量
ADDR = ('127.0.0.1',8888)


# 启动函数
def main():
    # 链接服务端
    s = socket()
    s.connect(ADDR)

    # 循环发送请求
    while True:
        print("=============命令选项==============")
        print("***          list            ***")
        print("***       get file           ***")
        print("***       put file           ***")
        print("***          quit            ***")
        print("===================================")
        cmd = input("输入命令：")

        s.send(cmd.encode())

if __name__ == '__main__':
    main()
