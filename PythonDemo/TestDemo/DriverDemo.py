#coding:utf-8
'''
Created on 2016年1月5日

@author: Yangyj
'''
from selenium import webdriver
import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://www.hao123.com")
time.sleep(3)
driver.quit()


if __name__ == '__main__':
    pass