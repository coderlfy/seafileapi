#-*- coding: utf-8 -*-

import util.DBHelper

class SeafileInfor():
    insdbhelper = None

    @staticmethod
    def select(fileid):
        sql = "select * from SeafileInfor where FID = '{0}'".format(fileid);
        dbhelper = util.DBHelper.DBHelper()
        return dbhelper.select(sql)

    @staticmethod
    def delete(fileid):
        sql = "delete from SeafileInfor where FID = '{0}'".format(fileid)
        dbhelper = util.DBHelper.DBHelper()
        return dbhelper.execute(sql)

    def __init__(self):
        if self.insdbhelper is None:
            self.insdbhelper = util.DBHelper.DBHelper()

    def selectbyname(self, filename):
        sql = "select * from SeafileInfor where FileName = '{0}'".format(filename);
        return self.insdbhelper.select(sql, False)

    def insert(self, filename, fid):
        sql = "insert into SeafileInfor(FID, FileName, CreateTime, IsDeleted) values('{0}', '{1}', NOW(), 0)".format(fid, filename);
        return self.insdbhelper.execute(sql)