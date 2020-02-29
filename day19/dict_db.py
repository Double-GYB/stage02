"""
服务端
数据处理部分
"""

import pymysql

class Database:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = '123456'
        self.charset='utf8'
        self.database = 'dict'
        self.connect_database()

    def connect_database(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user = self.user,
                                  password =self.password,
                                  database = self.database,
                                  charset = self.charset)

    def create_cursor(self):
        self.cur = self.db.cursor()

    # 帮 server 处理注册 成功 True 失败返回 False
    def register(self,name,passwd):
        # 判断这个姓名的用户是否存在
        sql = "select name from user where name=%s;"
        self.cur.execute(sql,[name])
        r = self.cur.fetchone() # 如果查询到了说明该用户已经存在
        if r:
            return False  # 不可注册
        else:
            # 插入数据库
            try:
                sql = "insert into user (name,passwd) values (%s,%s);"
                self.cur.execute(sql,[name,passwd])
                self.db.commit()
                return True
            except:
                self.db.rollback()
                return False
