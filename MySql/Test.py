from pymysql import connect

class JD(object):
    def __init__(self):
        # 打开数据库连接
        self.db = connect(host="localhost", user="root",
                     password="admin", db="db_newdb", port=3306, charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cur = self.db.cursor()

    def __del__(self):
        # 关闭连接
        self.cur.close()
        self.db.close()

    def execute_sql(self,sql):
        self.cur.execute(sql)  # 执行sql语句
        for i in  self.cur.fetchall() :
            print(i)

    def show_all_items(self):
        sql = "select * from t_test"
        self.execute_sql(sql)

    @staticmethod#加上这个就不用管self了
    def print_menu():
        print("1.所有的商品")
        print("2.所以的商品分类")
        print("所以的品牌分类")
        return input("请输入功能对应的序号")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                #查询所有的商品
                self.show_all_items()
            elif num ==  "2":
                #查询分类
                pass
            elif num == "3":
                #查询商品分类
                pass
            else:
                print("输入错误，请重新进行输入。")

def main():
    print("程序开始执行")
    jd = JD()
    jd.run()
    print("程序执行完成")

main()