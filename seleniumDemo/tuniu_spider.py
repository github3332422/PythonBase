from pyquery import PyQuery as pq
import time
import pymysql
from selenium import webdriver
import os
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options
#from IP_pool import get_ip                                 #导入ip代理

# 请求的url的列表1
url_list1 = ['http://www.tuniu.com/g906/pkg-all-0/','http://www.tuniu.com/g3300/pkg-all-0/']
# 请求的url列表2
url_list2 = ['http://www.tuniu.com/g600/pkg-sz-0/','http://www.tuniu.com/g700/pkg-sz-0/']



chrome_options = Options()

'''
# 设置代理
'''
#chromeOptions.add_argument("--proxy-server=%s"%get_ip())
'''
# 使用无头谷歌浏览器模式
'''
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

'''
 # 加载该项，可避免网站对selenium检测
'''
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

'''
# 禁止图片加载
'''
ban_img = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", ban_img)
bro = webdriver.Chrome(options=chrome_options)

#第一个列表旅游景点总体信息
def tour_01():
    for url in url_list1:
        bro.get(url)
        time.sleep(5)       #开启网页睡眠5秒
        free_index = bro.find_element_by_xpath('//*[@id="niuren_list"]/div[1]/div/div[3]/a[3]').click()   #第一次选择自由行标签
        time.sleep(3)
        page_num = bro.find_element_by_xpath('//*[@id="contentcontainer"]/div[2]/div[1]/div[1]/div[3]/div/a[7]').text   #获取景点自由行总页数
        for x in range(int(page_num)):
            html_code = bro.page_source      #网页源码
            doc = pq(html_code)
            datas = doc('.theinfo').items()  #使用items()方法遍历
            for i in datas:
                all_spot = {

                    'title':i.find('.main-tit').attr('title'),                            #标题
                    'recd':'|'.join(i.find('.sub-tuijian').text().strip('|\xa0')),        #景区特点
                    'spot':i.find('.overview-scenery').text(),                            #附近特点
                    'live':i.find('.mytip-grey').text().strip('住\n'),                    #居住
                    'price':i.find('.tnPrice').text().strip('¥\n起'),                     #价格
                    'fraction':i.find('.comment-satNum').text().strip('满意度\n%'),        #评分
                    'peo_num':i.find('.person-num').text().strip('\n人已出游'),            #景点出游人数c
                    'com_num':i.find('.person-comment').text().strip('\n人点评'),          #景点评论人数
                    'url':i.find('.clearfix').attr('href').strip('//')                     #景点URL地址
                }
                print(all_spot)
                #写sql插入语句

                sy_sql = "insert into tuniu_sanya(title,recd,spot,live,price,fraction,peo_num,com_num,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                data_save(all_spot,sy_sql) #存储函数，传入all_spot值和sql语句两个参数

            Slide() #调用网页滑动效果函数，让滚动条动起来
            try:

                next_button = bro.find_element_by_class_name('page-next').click()   #点击下一页 这里需要注意，不能打开网页就点击，可能会导致抓取重复的数据
                                                                                    #因为可能没加载到按钮，点击下一页，不执行点击，只是跳转到当前页面，所以滑动的时候最好滑动到按钮的位置
                                                                                    #你也可以执行鼠标移动到点击下一页的标签上，这样也可以。
            except:
                pass




#第二个列表旅游景点总体信息  该思路同上
def tour_02():
    for url in url_list2:
        bro.get(url)
        time.sleep(5)
        free_index = bro.find_element_by_xpath('//*[@id="niuren_list"]/div[1]/div/div[3]/a[3]').click()
        page_num = bro.find_element_by_xpath('//*[@id="contentcontainer"]/div[2]/div[1]/div[1]/div[3]/div/a[7]').text
        for x in range(int(page_num)):
            html_code = bro.page_source
            doc = pq(html_code)
            datas = doc('.theinfo').items()
            for i in datas:
                all_spot = {

                    'title':i.find('.main-tit').attr('title'),
                    'recd':i.find('.sub-tuijian').text().strip('|\xa0'),
                    'spot':i.find('.overview-scenery').text(),
                    'live':i.find('.mytip-grey').text().strip('住\n'),
                    'price':i.find('.tnPrice').text().strip('¥\n起'),
                    'fraction':i.find('.comment-satNum').text().strip('满意度\n%'),
                    'peo_num':i.find('.person-num').text().strip('\n人已出游'),
                    'com_num':i.find('.person-comment').text().strip('\n人点评'),
                    'url':i.find('.clearfix').attr('href').strip('//')
                }
                print(all_spot)
                yn_sql = "insert into tuniu_yunnan(title,recd,spot,live,price,fraction,peo_num,com_num,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                data_save(all_spot,yn_sql)
            Slide()
            try:
                next_button = bro.find_element_by_class_name('page-next').click()
            except:
                pass

'''
插入到数据库
'''
def data_save(data_dict,my_sql):
    db =pymysql.connect(host='localhost',user='root',password='admin',port=3306,db='spring')
    a = data_dict
    cursor = db.cursor()
    sql = my_sql
    params = (a['title'],a['recd'],a['spot'],a['live'],a['price'],a['fraction'],a['peo_num'],a['com_num'],a['url'])
    cursor.execute(sql,params)
    db.commit()
    db.close()


'''
  定义一个滚动条
  滑动的函数
  如果想加载查找标签有多种
  方法，鼠标定位，JS滚动等
'''
def Slide():
    a_next = "window.scrollTo(0,1000);"
    b_next = "window.scrollTo(0,2000);"
    c_next = "window.scrollTo(0,3000);"
    d_next = "window.scrollTo(0,4000);"
    e_next = "window.scrollTo(0,5000);"
    f_next = "window.scrollTo(0,5500);"
    bro.execute_script(a_next) #开始第一次滑动
    time.sleep(0.5)
    bro.execute_script(b_next)#开始第二次滑动
    time.sleep(0.5)
    bro.execute_script(c_next) #以下的以此类推
    time.sleep(0.5)
    bro.execute_script(d_next)
    time.sleep(0.5)
    bro.execute_script(e_next)
    time.sleep(1)
    bro.execute_script(f_next)

if __name__ == '__main__':
    SY = Process(target=tour_01)
    YN = Process(target=tour_02)
    SY.start()
    YN.start()

