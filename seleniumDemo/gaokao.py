import time
from selenium import  webdriver

driver = webdriver.Chrome()

driver.get('http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type=')

# btn = driver.find_element_by_css_selector('#xiaoyou')
# btn = driver.find_element_by_id('xiaoyou')
btn = driver.find_element_by_class_name('get_more')

while btn:
    btn.click()
    time.sleep(2)
    # btn = driver.find_element_by_id('xiaoyou')
    # btn = driver.find_element_by_css_selector('#xiaoyou')
    btn = driver.find_element_by_class_name('get_more')

print(driver.page_source)