#-*- coding: utf-8 -*-

import dal.SeafileInfor
import entity.FileInfor
import entity.Result
import entity.SeafileServer
import BLLBase
import json
import uuid

import requests

class Seafile(object):
    seafileserver = entity.SeafileServer.SeafileServer()

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
                    fileinfor.urlpath = Seafile.getdownloadurl(fileinfor.filename)
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
                    deleteresult = Seafile.deleteseafile(data[0][1])
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
            getfileinforresult = Seafile.getfileinfor(filename)

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

    @staticmethod
    def getfileinfor(filename):
        inforresult = entity.Result.Result()
        try:
            token_headers = {'Authorization': 'Token {0}'.format(Seafile.getseafileservertoken())}
            wdlibraryid = Seafile.getwdlibraryid(token_headers)
            url = 'http://{0}:{1}/api2/repos/{2}/file/detail/?p=/{3}'.format(
                Seafile.seafileserver.seafilehost,
                Seafile.seafileserver.port,
                wdlibraryid,
                filename)

            r = requests.get(url, headers=token_headers)
            fileinfor = r.json()
            if u'id' in fileinfor:
                inforresult.success = True
            else:
                inforresult.message = 'File not found in the file server'

        except(Exception), e:
            inforresult.message = repr(e)

        return inforresult

    @staticmethod
    def deleteseafile(filename):
        result = entity.Result.Result()
        try:
            token_headers = {'Authorization': 'Token {0}'.format(Seafile.getseafileservertoken())}
            wdlibraryid = Seafile.getwdlibraryid(token_headers)
            url = 'http://{0}:{1}/api2/repos/{2}/file/?p=/{3}'.format(
                Seafile.seafileserver.seafilehost,
                Seafile.seafileserver.port,
                wdlibraryid,
                filename)

            r = requests.delete(url, headers=token_headers)

            if r.json() == 'success':
                result.success = True
            else:
                result.message = 'Delete has not allowed'

        except(Exception), e:
            result.message = repr(e)

        return result

    @staticmethod
    def getseafileservertoken():
        token_url = 'http://{0}:{1}/api2/auth-token/'.format(Seafile.seafileserver.seafilehost,
                                                             Seafile.seafileserver.port)
        token_p = {'username': Seafile.seafileserver.user, 'password': Seafile.seafileserver.pwd}
        r = requests.post(token_url, token_p)
        return r.json()[u'token']

    @staticmethod
    def getwdlibraryid(token):
        librarys_url = 'http://{0}:{1}/api2/repos/'.format(Seafile.seafileserver.seafilehost,
                                                           Seafile.seafileserver.port)
        r = requests.get(librarys_url, headers=token)
        wdlibraryid = ''
        librarys = r.json()
        for i in range(len(librarys)):
            if librarys[i][u'name'] == Seafile.seafileserver.libraryname:
                wdlibraryid = librarys[i][u'id']

        return wdlibraryid

    @staticmethod
    def getdownloadurl(filename):
        token_headers = {'Authorization': 'Token {0}'.format(Seafile.getseafileservertoken())}
        wdlibraryid = Seafile.getwdlibraryid(token_headers)
        url = 'http://{0}:{1}/api2/repos/{2}/file/?p=/{3}'.format(
            Seafile.seafileserver.seafilehost,
            Seafile.seafileserver.port,
            wdlibraryid,
            filename)

        r = requests.get(url, headers=token_headers)
        return r.json()


