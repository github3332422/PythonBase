import pymongo

#客户端
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#插入的数据库
mydb = myclient["testdb"]
#插入的文档
mycol = mydb["site"]

def insert_mongo():
    mylist = [
        {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ]
    x = mycol.insert_many(mylist)
    # 输出插入的所有文档对应的 _id 值
    print(x.inserted_ids)

def select_mongo():
    #查询全部数据
    # for x in mycol.find():
    #     print(x)
    #查询一条数据
    # x = mycol.find_one()
    # print(x)
    #查询需要的内容
    # for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    #     print(x)
    # for x in mycol.find({}, {"alexa": 0}):
    #     print(x)
    # 按照条件查询
    myquery = {"name": "Facebook"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def updata_mongo():
    myquery = {"alexa": "103"}
    newvalues = {"$set": {"alexa": "12345"}}
    mycol.update_one(myquery, newvalues)
    # 输出修改后的  "sites"  集合
    for x in mycol.find():
        print(x)

def delete_mongo():
    #按照提交删除文档
    myquery = {"name": "Taobao"}
    mycol.delete_one(myquery)
    for x in mycol.find():
        print(x)
    #删除所有文档
    x = mycol.delete_many({})
    print(x.deleted_count, "个文档已删除")
    #删除集合
    mycol.drop()
    print('集合删除成功')
insert_mongo()
# select_mongo()
# updata_mongo()
# delete_mongo()