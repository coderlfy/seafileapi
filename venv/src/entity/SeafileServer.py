#-*- coding: utf-8 -*-

import Result
import ConfigParser

class SeafileServer(Result.Result):
    seafilehost = ''
    port = 0
    user = ''
    pwd = ''
    libraryname = ''
    groupkey = "seafileserver"

    def __init__(self):

        cf = ConfigParser.ConfigParser()
        cf.read("service.conf")

        kvs = cf.items(SeafileServer.groupkey)
        print SeafileServer.groupkey + ':', kvs

        self.seafilehost = cf.get(SeafileServer.groupkey, "ip")
        self.port = cf.getint(SeafileServer.groupkey, "port")
        self.user = cf.get(SeafileServer.groupkey, "admin")
        self.pwd = cf.get(SeafileServer.groupkey, "pwd")
        self.libraryname = cf.get(SeafileServer.groupkey, "library_name")

        self.success = True
