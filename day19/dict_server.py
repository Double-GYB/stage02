"""
服务端
逻辑处理
"""

from socket import *
from multiprocessing import Process
import  signal,sys

# 定义地址为全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)


# 处理客户端请求
def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        print(data)

# 创建多进程并发模型
def main():
    # 创建套接字
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    print("Listen the port 8000")
    while True:
        # 等待客户端链接
        c,addr = s.accept()
        print("Connect from",addr)

        # 为每个客户端创建进程
        p = Process(target=handle,args=(c,))
        p.start()


if __name__ == '__main__':
    main()