from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1')
# btn = driver.find_element_by_css_selector('#app > div > div.article > a')
# btn.click()
# while btn:
#     btn.click()
#     time.sleep(5)
#     btn = driver.find_element_by_css_selector('#app > div > div.article > a')

print(driver.page_source)
