#-*- coding: utf-8 -*-
import Result
import time

class FileInfor(Result.Result):
    fid = ''
    filename = ''
    urlpath = ''
    createtime = time.ctime(1)

    def __init__(self):
        self.fid = ''
        #self.filename = ''
        #self.urlpath = ''
