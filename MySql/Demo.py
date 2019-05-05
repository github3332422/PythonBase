import pymysql
import datetime

def select_mysql():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root",
                         password="admin", db="spring", port=3306,charset='utf8')
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 1.查询操作
    # 编写sql 查询语句  user 对应我的表名
    sql = "select * from t_test"
    try:
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        print("id", "name", "password")
        # 遍历结果
        for row in results:
            id = row[0]
            name = row[1]
            password = row[2]
            print(id, name, password)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接

def insert_mysql(dict_user):
    print(dict_user['id'],dict_user['name'],dict_user['password'])
    db = pymysql.connect(host="localhost", user="root",
                         password="admin", db="db_newdb", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    sql_insert = """insert into t_test(id,name,password) values(%s,%s,%s)"""
    try:
        # cur.execute(sql_insert %(dict_user['id'],dict_user['name'],dict_user['password']))
        cur.execute(sql_insert,(dict_user['id'],dict_user['name'],dict_user['password']))
        # 提交，如果没有执行commit的话
        db.commit()
        print('插入成功')
    except Exception as e:
        # 错误回滚
        print(e)
        db.rollback()#如果不想执行所写的sql语句的话也可以使用回滚进行执行
        print('插入失败')
    finally:
        db.close()

def delete_mysql():
    db = pymysql.connect(host="localhost", user="root",
                         password="admin", db="db_newdb", port=3306)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_delete = "delete from t_test where id = %d"

    try:
        cur.execute(sql_delete % (1))  # 像sql语句传递参数
        # 提交
        db.commit()
        print('删除成功')
    except Exception as e:
        # 错误回滚
        db.rollback()
        print('删除失败')
    finally:
        db.close()

def updata_mysql():
    db = pymysql.connect(host="localhost", user="root",
                         password="admin", db="db_newdb", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    sql_update = "update t_test set name = '%s' where id = %d"
    try:
        cur.execute(sql_update % ("张清", 2))  # 像sql语句传递参数
        # 提交
        db.commit()
        print('插入成功')
    except Exception as e:
        # 错误回滚
        db.rollback()
        print('插入失败')
    finally:
        db.close()
        
if __name__ == '__main__':
    dict_user = {"id": '1', "name": "zq",'password':'123456'}
    start_time = datetime.datetime.now()
    insert_mysql(dict_user)
    end_time = datetime.datetime.now()
    print("%s" % (start_time - end_time))
