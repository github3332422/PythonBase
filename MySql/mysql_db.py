import pymysql

class mysql_class:
    '''初始化'''
    def __init__(self,host="127.0.0.1", username="root", password="admin", port=3306, database="spring",charset='UTF-8'):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database
        self.charset = charset

    '''获取数据库连接 '''
    def get_con(self):
        try:
            self.con = pymysql.connect(host=self.host, user=self.username, password=self.password,
                                               port=self.port, database=self.database,)
            self.cur = self.con.cursor()
            print('数据库连接成功')
        except:
            raise "DataBase connect error,please check the db config."

    '''关闭数据库连接'''
    def close(self):
        self.con.close()

    '''创建数据库'''
    def create_table(self,sql):
        try:
            self.cur.execute(sql)
        except:
            raise "table create error,please check the sql."

    '''删除数据库'''
    def drop_table(self,sql):
        try:
            self.cur.execute(sql)
        except:
            raise "table create error,please check the sql."

    '''执行查询语句 '''
    def select_mysql(self,sql):
        self.get_con()
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            for result in results:
                print(result)
        except:
            raise "数据查询失败"
        self.close()

    '''执行插入语句，不带参数 '''
    def insert_mysql(self,sql):
        self.get_con()
        try:
            print(sql)
            self.cur.execute(sql)
            self.con.commit()
        except:
            self.con.rollback()
            raise "数据插入失败"
        self.close()

    '''执行插入语句，带参数'''
    def insert_mysql(self,sql,param):
        self.get_con()
        try:
            print(sql)
            self.cur.execute(sql,(param['username'],param['balance']))
            # self.cur.execute(sql,param)
            self.con.commit()
        except:
            self.con.rollback()
            raise "数据插入失败"
        self.close()

    '''执行删除语句，不带参数'''
    def delect_mysql(self,sql):
        self.get_con()
        try:
            print(sql)
            self.cur.execute(sql)
            self.con.commit()
        except:
            self.con.rollback()
            raise "数据删除失败"
        self.close()

    '''执行删除语句，带参数'''
    def delect_mysql(self,sql,param):
        self.get_con()
        try:
            print(sql)
            self.cur.execute(sql %(param[0]))
            # self.cur.execute(sql, (int)(param))
            self.con.commit()
        except:
            self.con.rollback()
            raise "数据删除失败"
        self.close()

    '''执行修改语句，不带参数'''
    def update_mysql(self,sql):
        self.get_con()
        try:
            print(sql)
            self.cur.execute(sql)
            self.con.commit()
        except:
            self.con.rollback()
            raise "数据修改失败"
        self.close()

    '''执行修改语句，带参数'''
    def update_mysql(self,sql,param):
        self.get_con()
        try:
            print(sql)
            self.cur.execute(sql % (param[0], param[1]))
            self.con.commit()
        except:
            self.con.rollback()
            raise "数据修改失败"
        self.close()


if __name__ == '__main__':
    ms = mysql_class()
    # 插入测试
    # sql = '''select id,username,balance from account'''
    # ms.select_mysql(sql)

    #插入数据测试 不带参数
    # sql = '''insert into account(username,balance) values('tom',1000)'''
    # ms.insert_mysql(sql)

    #插入数据测试 带参数
    # sql = '''insert into account(username,balance) values(%s,%s)'''
    # param = {"username": "zq", 'balance': 1234.5}
    # sql = '''insert into account values(%s,%f)'''
    # param = ("zq",1234.0)
    # ms.insert_mysql(sql,param)

    #删除数据测试 不带参数
    # sql = '''delete from account where id = 8'''
    # ms.delect_mysql(sql)

    #删除测试数据 带参数
    sql = '''delete from account where id = (%d)'''
    param = (9)
    # ms.delect_mysql(sql,param)
    # param = {"id":5}
    ms.delect_mysql(sql, param)

    #修改测试数据 带参数
    # sql = '''update account set username = '%s' where id = %d'''
    # param = ['zhang',2]
    # ms.update_mysql(sql,param)

