"""
ftp 客户端
"""
from socket import *
import sys

# 全局变量
ADDR = ('127.0.0.1',8888)

# 查看文件列表，上传，下载，退出
class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def quit(self):
        self.sockfd.send(b'E')
        self.sockfd.close()
        sys.exit("谢谢使用")

# 启动函数
def main():
    # 链接服务端
    s = socket()
    s.connect(ADDR)

    ftp = FTPClient(s) # 实例化对象，用于调用类中的方法，具体与服务端交互

    # 循环发送请求
    while True:
        print("=============命令选项==============")
        print("***          list            ***")
        print("***         get file         ***")
        print("***         put file         ***")
        print("***          quit            ***")
        print("===================================")
        cmd = input("输入命令：")

        # 根据不同的输入进行不同的处理
        if cmd == 'quit':
            ftp.quit()

if __name__ == '__main__':
    main()
