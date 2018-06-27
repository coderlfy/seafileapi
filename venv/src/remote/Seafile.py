#-*- coding: utf-8 -*-

import entity.Result
import entity.SeafileServer
import requests


class Seafile(object):
    seafileserver = entity.SeafileServer.SeafileServer()

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

    @staticmethod
    def getuploadurl(token):
        token_headers = {'Authorization': 'Token {0}'.format(token)}
        wdlibraryid = Seafile.getwdlibraryid(token_headers)
        url = 'http://{0}:{1}/api2/repos/{2}/upload-link/'.format(
            Seafile.seafileserver.seafilehost,
            Seafile.seafileserver.port,
            wdlibraryid)

        r = requests.get(url, headers=token_headers)

        return r.json()

    @staticmethod
    def upload(filename):
        uploadurl = Seafile.getuploadurl()




