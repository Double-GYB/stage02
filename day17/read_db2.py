"""
数据读操作演示2
"""

import pymysql

# 链接数据库
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'student',
                     charset = 'utf8')

# 创建游标  （操作数据 执行sql语句，获取结果）
cur = db.cursor()

# 输入一个名字查看他的信息
name = input("Name:")




# 关闭游标和数据库
cur.close()
db.close()
