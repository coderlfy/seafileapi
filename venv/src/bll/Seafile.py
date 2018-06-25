#-*- coding: utf-8 -*-

import dal.SeafileInfor
import entity.FileInfor
import entity.Result
import BLLBase
import uuid
import remote.Seafile

import requests

class Seafile(object):

    @staticmethod
    def get(fileid):
        fileinfor = entity.FileInfor.FileInfor()

        try:
            if fileid != '':
                r = dal.SeafileInfor.SeafileInfor.select(fileid)
                if len(r) > 0:
                    fileinfor.success = True
                    fileinfor.id = r[0][0]
                    fileinfor.filename = r[0][1]
                    fileinfor.urlpath = remote.Seafile.Seafile.getdownloadurl(fileinfor.filename)
                else:
                    fileinfor.message = 'File not found.'
        except(Exception), e:
            fileinfor.message = repr(e)

        return BLLBase.BLLBase.getjson(fileinfor)

    @staticmethod
    def delete(fileid):
        r = entity.Result.Result()

        try:
            if fileid != '':
                data = dal.SeafileInfor.SeafileInfor.select(fileid)
                if len(data) > 0:
                    deleteresult = remote.Seafile.Seafile.deleteseafile(data[0][1])
                    if deleteresult.success:
                        rowcount = dal.SeafileInfor.SeafileInfor.delete(fileid)
                        if rowcount == 0:
                            r.message = 'File not found.'
                        else:
                            r.success = True
                    else:
                        r.message = deleteresult.message
                else:
                    r.message = 'File not found.'
            else:
                r.message = 'fileid is empty.'
        except(Exception), e:
            r.message = repr(e)

        return BLLBase.BLLBase.getjson(r)

    @staticmethod
    def add(filename):
        #根据文件名去文件服务器查询该文件是否存在，若存在则走下步
        #根据文件名获取当前是否有该文件记录
        #若无该文件记录则进行插入
        #若存在该文件记录则返回错误
        r = entity.Result.Result()
        try:
            getfileinforresult = remote.Seafile.Seafile.getfileinfor(filename)

            if getfileinforresult.success:
                seafiledal = dal.SeafileInfor.SeafileInfor();
                files = seafiledal.selectbyname(filename)
                if len(files) > 0:
                    r.message = 'The cache has found the file, please change the file name to upload again!';
                else:
                    rowcount = seafiledal.insert(filename, uuid.uuid1())
                    if rowcount <= 0:
                        r.message = 'The file add to cache failed.';
                    else:
                        r.success = True
            else:
                r.message = getfileinforresult.message

        except(Exception), e:
            r.message = repr(e)

        return BLLBase.BLLBase.getjson(r)



