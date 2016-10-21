#coding:utf-8
'''
Created on 2016年1月5日

@author: Yangyj
'''
'''
from selenium import webdriver

chromeDriver = webdriver.Chrome()
chromeDriver.get("http://hao123.com")
chromeDriver.implicitly_wait(5)
chromeDriver.maximize_window()
'''
import MySQLdb
conn = MySQLdb.connect("localhost","yang","Meicai@2015","mytest")
curs = conn.cursor()
count = curs.execute("select * from employee")

print count


print "你好！"


if __name__ == '__main__':
    pass