from redis import *
if __name__ == '__main__':
    try:
        # 创建一个StrictRedis对象，连接Redis数据库
        sr = StrictRedis()
        #设置一个值
        # res = sr.set('a5','z')
        # print(res)返回true或false
        #修改
        # res = sr.set('a5','123')返回true或false
        #获取一个值
        # res = sr.get('a5')
        # print(res)返回true或false
        #删除
        # res = sr.delete('a1','a2')
        # print(res)
        #获取数据库中所有的键
        res = sr.keys()
        print(res)
    except Exception as e:
        print(e)
