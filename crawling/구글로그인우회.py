from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox('./geckodriver')

driver.get('https://stackoverflow.com/')
time.sleep(0.5)

driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
time.sleep(0.5)

driver.find_element_by_id('identifierId').send_keys('edmclasson@gmail.com')

driver.find_element_by_xpath( '//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(2)

driver.find_element_by_xpath( '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('goedm39587$')

driver.find_element_by_xpath( '//*[@id="passwordNext"]/div/button/div[2]').click()

driver.get('https://analytics.google.com/analytics/web/?hl=ko&pli=1#/dashboard/xSVVMpdKSZyTxqGNPJVhiw/a97177317w224305445p212665896/_u.date00=20210308&_u.date01=20210308')
time.sleep(2)
