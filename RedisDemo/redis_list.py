import redis

db = redis.Redis(host='127.0.0.1',port='6379',db=4)

def push_list(lis):
    for li in lis:
        db.rpush('ip',li)
lis = [
    '111.226.188.230:8010',
	'122.193.245.70:9999',
	'171.41.81.43:9999',
	'171.41.81.115:9999',
	'171.41.81.105:9999',
	'171.41.82.23:9999',
	'171.41.81.171:9999',
	'112.85.167.253:9999'
]
#循环遍历列表，一个数据一个数据的放入
# for li in lis:
#     db.rpush('ip',li)

#把整个列表放入，通过自己手写方法实现
# push_list(lis)

#遍历整个链表
# print(db.lrange('ip',0,-1))
# print("*"*50)
# t = db.lpop('ip')
# print(t)
# db.rpush('ip',t)
# #遍历整个链表
# print(db.lrange('ip',0,-1))

#输出列表长度
# print(db.llen('ip'))

