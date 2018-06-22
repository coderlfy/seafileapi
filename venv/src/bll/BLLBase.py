#-*- coding: utf-8 -*-

import json

class BLLBase(object):

    @staticmethod
    def exceptionwrapper(action, r):
        try:
            if not None is action:
                action()
        except(Exception), e:
            r.success = False
            r.message = repr(e)

    @staticmethod
    def getjson(r):
        return json.dumps(r, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)


