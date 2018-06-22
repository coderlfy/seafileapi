#-*- coding: utf-8 -*-
import tornado.web
import entity.Result
import bll.Seafile
import HandlerBase


class AddFile(tornado.web.RequestHandler):
    def post(self):
        filename = HandlerBase.HandlerBase.getparam(self, 'filename')
        if filename.success:
            self.write(bll.Seafile.Seafile.add(filename.value))
        else:
            self.write(HandlerBase.HandlerBase.getjson(fileid))


class GetFile(tornado.web.RequestHandler):
    def get(self):
        fileid = HandlerBase.HandlerBase.getparam(self, 'fileid')
        if fileid.success:
            self.write(bll.Seafile.Seafile.get(fileid.value))
        else:
            self.write(HandlerBase.HandlerBase.getjson(fileid))


class DeleteFile(tornado.web.RequestHandler):
    def post(self):
        fileid = HandlerBase.HandlerBase.getparam(self, 'fileid')
        if fileid.success:
            self.write(bll.Seafile.Seafile.delete(fileid.value))
        else:
            self.write(HandlerBase.HandlerBase.getjson(fileid))


# 只保留n个月的缓存
class ClearFile(tornado.web.RequestHandler):
    def post(self):
        self.write('ClearFile!')