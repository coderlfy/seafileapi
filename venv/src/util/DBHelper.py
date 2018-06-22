# -*- coding: utf-8 -*-

import MySQLdb
import time
import types
import os
import ConfigParser


class DBConnectParams(object):
    Server = '192.168.18.253'
    DB = 'eteachdb'
    Username = 'mysqluser'
    Password = 'admin123'
    Port = 3306

    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read("service.conf")

        # return all section
        #secs = cf.sections()
        #print 'sections:', secs

        #opts = cf.options("db")
        #print 'options:', opts

        kvs = cf.items("db")
        print 'db:', kvs

        self.Server = cf.get("db", "db_host")
        self.Port = cf.getint("db", "db_port")
        self.Username = cf.get("db", "db_user")
        self.Password = cf.get("db", "db_pass")
        self.DB = cf.get("db", "db_name")


class DBHelper(object):
    connparams = DBConnectParams()
    db = None

    def setconn(self, connparams):
        self.connparams = connparams

    def connectdb(self):
        if self.db is None:
            self.db = MySQLdb.connect(host=self.connparams.Server,
                                      user=self.connparams.Username,
                                      passwd=self.connparams.Password,
                                      db=self.connparams.DB,
                                      port=self.connparams.Port,
                                      charset='utf8')

    def closedb(self):
        if not None == self.db:
            self.db.close()

    def select(self, sql, closed=True):
        results = ''

        try:
            self.connectdb()
            cursor = self.db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
        finally:
            if closed:
                self.closedb()

        return results

    def execute(self, sql, closed=True):
        rowcount = 0
        try:
            self.connectdb()
            cursor = self.db.cursor()
            rowcount = cursor.execute(sql)
            self.db.commit()
        finally:
            if closed:
                self.closedb()

        return rowcount