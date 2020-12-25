lfrom selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://hira.kacnet.co.kr/")
time.sleep(3)

# driver.find_element_by_xpath(
#     """//*[@id="wrap"]/div[2]/div[2]/div/div[2]/div[1]/div/a""").click()

# driver.find_element_by_xpath(
#     '//a[contains(@href, "/new_board/List.php?boardtype=A&amp;type=List&amp;bkind=kong")]').click()

# driver.find_element_by_css_selector(
#     '#wrap > div.main_back > div.contents_box01 > div > div.notice_line > div.notice_box.h-341 > div > a').click()

driver.find_element_by_class_name('link_master.new_icon').click()

# driver.find_element_by_name('pw').send_keys('')
