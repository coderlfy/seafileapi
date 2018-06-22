#-*- coding: utf-8 -*-
import Result
import time

class FileInfor(Result.Result):
    id = ''
    filename = ''
    urlpath = ''
    createtime = time.ctime(1)

    '''
    def __init__(self, success, msg):
        self.success = success
        self.message = msg
    '''