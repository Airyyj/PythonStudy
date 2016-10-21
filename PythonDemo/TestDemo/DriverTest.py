#coding:utf-8
'''
Created on 2016年1月5日

@author: Yangyj
'''
from selenium import webdriver
import time
#chromedriver = "D:\Python27\chromedriver_x64.exe"

#driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome()
driver.get("http:www.hao123.com")

time.sleep(5)

driver.quit()

if __name__ == '__main__':
    pass