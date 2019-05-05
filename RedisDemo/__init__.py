import redis

db = redis.Redis(host='127.0.0.1',port='6379',db=2)
# db.set('age',18)
# print(db.get('age').decode('utf8'))

#set操作
#添加元素
# db.sadd('myset1','6','5','0')
#删除元素
# db.srem('myset1','2')
#判断集合中是否存在某个元素
# print(db.sismember('myset1','5'))
#查看集合的个数
# print(db.scard('myset1'))
#遍历集合
# print(db.smembers('myset1'))
#随机移除一个元素
# print(db.spop('myset1'))
print(db.exists('myset1'))
print(db.delete('myset1'))