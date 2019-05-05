from selenium import webdriver
from selenium.webdriver.chrome.options import Options


option = webdriver.ChromeOptions()
'''
设置避免检测到是selenium的请求
'''
option.add_experimental_option('excludeSwitches', ['enable-automation'])

'''
设置请求的编码
'''
# option.add_argument('lang=zh_CN.UTF-8')

'''
# 使用无头谷歌浏览器模式
'''
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')

'''
设置手机请求头
http://www.fynas.com/ua
通过这个网站可以查看每种手机的请求头
'''
option.add_argument('--user-agent=iphone')
# mobile_emulation = {
#     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
#     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
# }
# chrome_options = Options()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

'''
设置禁止图片的下载
'''
# ban_img = {"profile.managed_default_content_settings.images": 2}
# option.add_experimental_option("prefs", ban_img)

'''
使用浏览器上的一些扩展程序
'''
# extension_path = 'D:/extension/XPath-Helper_v2.0.2.crx'
# option.add_extension(extension_path)

driver = webdriver.Chrome(chrome_options=option)
driver.get('http://www.lagou.com/')
print(driver.page_source)


