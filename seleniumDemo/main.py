# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# input = driver.find_element_by_id('kw')
# input = driver.find_element(By.ID,'kw')
# input = driver.find_element_by_name('wd')
# input = driver.find_element(By.NAME,'wd')
# input = driver.find_element_by_class_name('s_ipt')
# input = driver.find_element(By.CLASS_NAME,'s_ipt')
# input = driver.find_element_by_css_selector('#kw')
# input = driver.find_element(By.CSS_SELECTOR,'#kw')
# input = driver.find_element_by_xpath('//input[@class="s_ipt"]')
# input = driver.find_element(By.XPATH,'s_ipt')
# input.send_keys('张伟')
# # driver.close()


# driver.get('https://www.douban.com/')
# checkBoxBut = driver.find_element_by_name('remember')
# checkBoxBut = driver.find_element(By.ID,'account-form-remember')
# checkBoxBut.click()
# driver.get('https://www.douban.com/')
# time.sleep(3)
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()

# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome()
# selectTag = Select(driver.get('url'))
# #根据索引选择
# selectTag.select_by_index("")
# #根据value值选择
# selectTag.select_by_value("")
# #根据文本选择
# selectTag.select_by_visible_text("")
# #取消选中所有选择
# selectTag.deselect_all()
# inputTag = driver.find_element_by_id('su')
# inputTag.click()



# url = 'https://www.baidu.com/'
# driver = webdriver.Chrome()
# driver.get(url)
# inputTag = driver.find_element_by_id('kw')
# inputTag.clear()
# inputTag.send_keys('Python')
# inputButten = driver.find_element_by_id('su')
# inputButten.click()

# from selenium.webdriver.common.action_chains import ActionChains
# url = 'https://www.baidu.com/'
# driver = webdriver.Chrome()
# driver.get(url)
# inputTag = driver.find_element_by_id('kw')
# inputButten = driver.find_element_by_id('su')
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag,'Python')
# actions.move_to_element(inputButten)
# actions.click(inputButten)
# actions.perform()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get('https://www.douban.com/')
# driver.implicitly_wait(50)
#
# element = WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.ID,'anony-nav'))
# )
# print(element)

#页面切换
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.execute_script("window.open('https://www.douban.com/')")
# print(driver.current_url)
# driver.switch_to_window(driver.window_handles[1])
# print(driver.current_url)


#ip代理
# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://59.62.167.198:9999")
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('http://httpbin.org/ip')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.taobao.com/")
input = driver.find_element_by_name('q')
print(input)
input.clear()
input.send_keys('衬衫')

inputButton= driver.find_element_by_css_selector('#J_TSearchForm > div.search-button > button')
inputButton.click()
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#J_SearchForm > button'))
    )
print(driver.page_source)
# subminBut = driver.find_element_by_id('kw')
# print(type(subminBut))
# print(subminBut.get_attribute("value"))
# driver.save_screenshot("baidu.png")

TiMS8vd7PhfQ3E8
