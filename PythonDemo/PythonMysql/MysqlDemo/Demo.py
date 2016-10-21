#coding:utf-8
'''
Created on 2016年1月9日

@author: Yangyj
'''
from _sqlite3 import Cursor
from datetime import date
print "你好，杨要军！"

import MySQLdb
#链接数据库
db = MySQLdb.connect("localhost","yang","Meicai@2015","mytest")
#获取游标
cursor = db.cursor()

print cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print "database version:%s" % data
'''创建数据 表
cursor.execute("drop table if exists tabletest")

sql = """create table tabletest(first_name char(20) not null,last_name char(20),
        age int,sex char(1),income float)"""
cursor.execute(sql)
'''
#cursor.excutemany()
#插入数据
insertsql = "inster into tabletest(first_name,last_name,age,sex,income) values('Mac','Mohan',20,'M',2000)"        

try:
    cursor.execute(insertsql)
    db.commit()
except:
    db.rollback()

db.close()

