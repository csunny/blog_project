#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
import MySQLdb
from proxy import GetIp, ParseJson
from pymongo import MongoClient

# 插入数据库时中文用'gbk'编码格式
# for i, item in enumerate(items):
#     if i < 10:
#         print item[3].decode('gbk')


class HandleDb(object):
    def __init__(self, items):
        self.items = items
        self.con = MySQLdb.connect(db='magic', user='user', passwd='12345670',
                                   host='192.168.1.100', port=3306, use_unicode='true', charset='utf8')
        self.cur = self.con.cursor()

    def insert(self):
        for item in self.items:
            sql = ("insert into proxy(IP, PORT, TYPE, POSITION, SPEED, LAST_CHECK_TIME)"
                   "values(%s, %s, %s, %s, %s, %s)")

            lis = (item[0], item[5], item[4], item[3].decode('gbk'), item[2], item[1])
            try:
                self.cur.execute(sql, lis)
            except Exception as e:
                print "Insert error {}".format(e)
            else:
                self.con.commit()
                print "Insert successfully"


class WriteJson(HandleDb):
    def __init__(self, items):
        super(WriteJson, self).__init__(items)
        self.items = items

    def insert(self):
        for item in self.items:
            sql = ("insert into proxy(IP, PORT, TYPE, POSITION, SPEED, LAST_CHECK_TIME)"
                   "values(%s, %s, %s, %s, %s, %s)"
                   )
            if item.has_key('SPEED'):
                lis = (item['IP'], item['PORT'], item['TYPE'],
                       item['POSITION'].decode('unicode-escape'), item['SPEED'], item['LAST_CHECK_TIME'])
            else:
                lis = (item['IP'], item['PORT'], item['TYPE'],
                       item['POSITION'].decode('unicode-escape'), 0, item['LAST_CHECK_TIME'])

            try:
                self.cur.execute(sql, lis)
            except Exception as e:
                print "Insert error {}".format(e)
            else:
                self.con.commit()
                print "Insert successfully"


# 使用mongodb， 将数据写入mongodb中.
class MongoHandle(object):
    def __init__(self):
        self.client = MongoClient('192.168.1.100', 27017)

    def insert(self, item):
        db = self.client.magic
        try:
            db.proxy.insert_one(item)
        except Exception as e:
            print e
        else:
            print "Insert succesfully"


# Insert db from csv file to mysql database
def test():
    items = GetIp('../ips.csv').result
    hdd = HandleDb(items)
    hdd.insert()


# Insert db from json file to mysql
def main():
    pj = ParseJson()
    items = pj.items
    wj = WriteJson(items)
    wj.insert()


# 插入数据到mongodb
def testmongo():
    pj = ParseJson()
    items = pj.items
    for item in items:
        item.update({'POSITION': item['POSITION'].decode('unicode-escape')})
        mh = MongoHandle()
        mh.insert(item)


if __name__ == '__main__':
   testmongo()
