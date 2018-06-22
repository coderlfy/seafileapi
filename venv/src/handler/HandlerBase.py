#-*- coding: utf-8 -*-

import json
import entity.RequestParam
import const

class HandlerBase(object):
    const.PARAMETERMISSING = 'Parameter is missing, parameter`s name is {0}'

    @staticmethod
    def getjson(r):
        return json.dumps(r, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def getparam(handler, keyname):
        p = entity.RequestParam.RequestParam(keyname)

        if handler.request.arguments.has_key(keyname):
            p.value = handler.get_argument(keyname)
            p.success = True
        else:
            if handler.request.body != '':
                data = json.loads(handler.request.body)
                p.value = data[keyname]
                p.success = True
            else:
                p.message = const.PARAMETERMISSING.format(keyname)

        return p