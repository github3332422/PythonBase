import redis
import json
class redis_class:
    '''初始化数据库'''
    def __init__(self,host="127.0.0.1",password='',port=6379,db=0):
        self.host = host
        self.port = port
        self.password = password
        self.db = db

    '''得到连接'''
    def get_con(self):
        try:
            self.connection_pool = redis.ConnectionPool(host=self.host,port=self.port,password=self.password,db=self.db)
            self.connection_client = redis.Redis(connection_pool=self.connection_pool)
            print("Redis DataBase connect success")
        except:
            raise "Redis DataBase connect Faild"

    '''关闭数据库连接'''
    def close_con(self):
        self.connection_client
        self.connection_pool.disconnect()

    '''插入数据'''
    def insert_redis(self,key,value):
        self.get_con()
        try:
            self.connection_client.set(key,value)
            print("insert Redis DataBase success")
        except:
            raise "insert into Redis Faild"
        self.close_con()

    '''插入json数据'''
    def insert_redis_list(self,key,value):
        self.get_con()
        try:
            self.connection_client.rpush(key,value)
            print("insert Redis DataBase json data success")
        except:
            raise "insert into Redis json data Faild"
        self.close_con()


    '''查询数据'''
    def select_redis(self,key):
        self.get_con()
        try:
            result = self.connection_client.get(key)
            print("select Redis DataBase success")
            if result:
                return result.decode('UTF-8')
            else:
                return "None"
        except:
            raise "select into Redis Faild"
        self.close_con()

    '''删除数据'''
    def delete_redis(self,key):
        self.get_con()
        try:
            result = self.connection_client.get(key)
            if result:
                self.connection_client.delete(key)
                print("delete data success")
            else:
                print("delete data not exist")
        except:
            raise "delete into Redis Faild"
        self.close_con()



# if __name__ == '__main__':
    # ms = redis_class(db=1)
    # # ms.insert_redis('name','张清')
    # # print(ms.select_redis('age'))
    # ms.delete_redis('name')