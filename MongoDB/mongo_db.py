import pymongo


class mongo_class:
    '''数据库初始化'''
    def __init__(self,host='127.0.0.1',port=27017,database = 'db_test',collection='test'):
        self.host = host
        self.port = port
        self.database = database
        self.collection = collection

    '''获取连接'''
    def get_con(self):
        try:
            self.conn = pymongo.MongoClient(host=self.host, port=self.port)
            # self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.conn[self.database]
            # print('DataBase connection success')
        except:
            raise "self.conn is not None and self.db is not None"

    '''关闭连接'''
    def close_con(self):
        self.conn.close()

    '''插入一条数据'''
    def insert_mongodb_one(self, data):
        self.get_con()
        try:
            # print(data)
            ret = self.db[self.collection].insert_one(data)
            print("Data insertion success",ret.inserted_id)
        except:
            raise "Data insertion failed"
        finally:
            self.close_con()

    '''插入多条数据'''
    def insert_mongodb_many(self,  data):
        self.get_con()
        try:
            ret = self.db[self.collection].insert_many(data)
            print("Data insertion success",ret.inserted_ids)
        except:
            raise "Data insertion failed"
        finally:
            self.close_con()

    '''删除一条数据'''
    def delete_mongo_one(self,data):
        self.get_con()
        try:
            ret = self.db[self.collection].delete_one(data)
            print("Data delete success")
        except:
            raise "Data delete one failed"
        finally:
            self.close_con()

    '''删除多条数据'''
    def delete_mongo_many(self , data):
        self.get_con()
        try:
            ret = self.db[self.collection].delete_many(data)
            print("Data delete success")
        except:
            raise "Data insertion many failed"
        finally:
            self.close_con()

    '''修改一条数据'''
    def update_mongo_one(self,myquery,newvalues):
        self.get_con()
        try:
            ret = self.db[self.collection].update_one(myquery, newvalues)
            print("Data updata success")
        except:
            raise "Data updata one failed"
        finally:
            self.close_con()

    '''修改多条数据'''
    def update_mongo_many(self,myquery,newvalues):
        self.get_con()
        try:
            ret = self.db[self.collection].update_many(myquery, newvalues)
            print("Data updata success")
        except:
            raise "Data updata many failed"
        finally:
            self.close_con()

    '''查询一条数据'''
    def select_mongo_one(self,data):
        self.get_con()
        try:
            ret = self.db[self.collection].find_one(data)
            print("Data find one success",ret)
            return ret
        except:
            raise "Data find one failed"
        finally:
            self.close_con()

    '''查询多条数据'''
    def select_mongo_many(self,data):
        self.get_con()
        try:
            ret = self.db[self.collection].find(data)
            print("Data find many success",ret)
            return ret
        except:
            raise "Data find many failed"
        finally:
            self.close_con()

    '''查询前N条数据'''
    def select_mongo_limit(self,data,n):
        self.get_con()
        try:
            ret = self.db[self.collection].find(data).limit(n)
            print("Data find many success", ret)
            return ret
        except:
            raise "Data find many failed"
        finally:
            self.close_con()

    '''查询前N--M条数据'''
    def select_mongo_skip(self,data,n,m):
        self.get_con()
        try:
            ret = self.db[self.collection].find(data).skip(m-1).limit(n-m+1)
            print("Data find skip success")
            return ret
        except:
            raise "Data find skip failed"
        finally:
            self.close_con()


if __name__ == '__main__':
    mo = mongo_class()

    '''测试插入一条数据'''
    # mylist = {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    # mo.insert_mongodb_one(mylist)

    '''测试插入多条数据'''
    # mylist = [
    #     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    #     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    #     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    #     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    #     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    # ]
    # mo.insert_mongodb_many(mylist)

    '''测试删除一条数据'''
    # myquery = {"name": "Github"}
    # mo.delete_mongo_one(myquery)

    '''测试删除多条数据'''
    # myquery = {"name": "Github"}
    # mo.delete_mongo_many(myquery)

    '''测试修改一条数据'''
    # myquery = {"alexa": "103"}
    # newvalues = {"$set": {"alexa": "12345"}}
    # mo.update_mongo_one(myquery, newvalues)

    '''测试修改多条数据'''
    # myquery = {"name": "张清"}
    # newvalues = {"$set": {"name": "GitHub"}}
    # mo.update_mongo_many(myquery, newvalues)

    '''测试查询一条数据'''
    # myquery = {"name": "Facebook"}
    # mo.select_mongo_one(myquery)

    '''测试查询多条数据'''
    myquery = {"name": "GitHub"}
    ret = mo.select_mongo_many(myquery)
    # ret.limit(3)
    for re in ret:
        print(re)

    '''测试查询前N条数据'''
    # myquery = {"name": "GitHub"}
    # n = 3
    # ret = mo.select_mongo_limit(myquery,n)
    # for re in ret:
    #     print(re)

    '''测试查询第N到M条数据'''
    # myquery = {"name": "GitHub"}
    # n = 2
    # m = 3
    # ret = mo.select_mongo_skip(myquery,n,m)
    # for re in ret:
    #     print(re)