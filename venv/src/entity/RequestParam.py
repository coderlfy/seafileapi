#-*- coding: utf-8 -*-

class RequestParam(object):
    success = False
    keyname = ''
    value = ''
    message = ''
    def __init__(self, keyname):
        self.success = False
        self.keyname = keyname