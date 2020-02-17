"""
FTP 文件处理
多线程并发和套接字练习
"""

from socket import *
from threading import Thread
import os,time


# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 文件库
FTP = "/home/tarena/FTP/"


# 处理客户端请求 (自定义线程类)
class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    # 处理文件列表
    def list(self):
        # 判断文件库是否为空
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        # 发送文件列表
        data = '\n'.join(file_list)  # 将文件以\n拼接
        self.connfd.send(data.encode())


    #  循环接收请求，分发任务
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()  # 接收请求
            if not data or data == 'E':
                return   # run函数结束对应线程即退出
            elif data == 'L':
                self.list()

# 框架结构，启动函数
def main():
    # 创建监听套接字
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port 8888")

    # 循环等待客户端链接
    while True:
        c, addr = s.accept()
        print("Connect from", addr)

        # 创建线程处理客户端请求
        t = FTPServer(c)  # 通过自定义线程类创建线程
        t.setDaemon(True)  # 分支线程随主线程退出
        t.start()

    s.close()

if __name__ == '__main__':
    main()