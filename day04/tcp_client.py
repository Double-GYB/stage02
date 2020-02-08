"""
tcp_client.py
tcp客户端演示: 重点代码
"""

from socket import *

# 服务器地址
server_addr = ("127.0.0.1",8888)

# 创建tcp套接字
sockfd = socket() # 默认值就是tcp

# 连接服务器
sockfd.connect(server_addr)

# 发送接收消息
data = input(">>")
sockfd.send(data.encode())
data = sockfd.recv(1024)
print("From server:",data.decode())

sockfd.close()

