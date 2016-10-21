#coding:utf-8
'''
Created on 2016年1月8日

@author: Yangyj
'''
import demjson

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = demjson.decode(json)
print  text

if __name__ == '__main__':
    pass