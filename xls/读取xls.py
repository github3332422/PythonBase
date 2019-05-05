import xlrd
import json
#导入自己写入的类，会报错，但是不影响使用
# from mysql_db import mysql_class
# from mongo_db import mongo_class
from RedisDemo.redis_db import redis_class

book = xlrd.open_workbook('p4.xlsx')
sheet = book.sheet_by_name('Table 9 ')
print("*"*50)
#读取一行
# row = sheet.row_values(50)
# print(row,row[0])

#读取多行
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))

#读取一定范围
count = 0
for i in range(15,223):
    row = sheet.row_values(i)
    # print(row[1],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
    print("*"*50)
    famale = []
    famale.append(row[8])
    famale.append(row[9])
    male = []
    male.append(row[6])
    male.append(row[7])
    total =[]
    total.append(row[4])
    total.append(row[5])
    married_by_15 = []
    married_by_15.append(row[10])
    married_by_15.append(row[11])
    married_by_18 = []
    married_by_18.append(row[12])
    married_by_18.append(row[13])
    dat = {
        'country':row[1],
        'child_labor':{
            'famale':famale,
            'male':male,
            'total':total
        },
        'child_marriage':{
            'married_by_15':married_by_15,
            'married_by_18': married_by_18
        }
    }

    print(row[1],dat)

    #写入到json数据格式
    # dat = json.dumps(dat)
    # fileObject = open('zhangqing.json', 'a+')
    # fileObject.write(dat)
    # fileObject.write('\n')
    # # fileObject.writelines(dat)
    # fileObject.close()

    #写入到MySQL数据库
    # ms = mysql_class()
    # sql = '''insert into t_test(country,child_labor,child_marriage) values(%s,%s,%s)'''
    # param = {"country": str(dat['country']), "child_labor": str(dat['child_labor']),"child_marriage":str(dat['child_marriage'])}
    # ms.insert_mysql(sql, param)

    #写入到MongoDb数据库
    # mo = mongo_class(collection='p4')
    # mo.insert_mongodb_one(dat)

    #写入到redis数据库
    if row[1] != '':
        ms = redis_class(db=3)
        ms.insert_redis_list(row[1], str(dat['child_labor']))
        ms.insert_redis_list(row[1], str(dat['child_marriage']))
        # ms.insert_redis(row[1], str(dat))

