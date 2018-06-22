#-*- coding: utf-8 -*-


import tornado.ioloop
import handler.SeafileHandler


settings = {
    'debug': False
}
application = tornado.web.Application([
    (r"/SeafileManager/add", handler.SeafileHandler.AddFile),
    (r"/SeafileManager/get", handler.SeafileHandler.GetFile),
    (r"/SeafileManager/delete", handler.SeafileHandler.DeleteFile),
    (r"/SeafileManager/clear", handler.SeafileHandler.ClearFile)
], **settings)
if __name__ == "__main__":
    application.listen(28888)
    tornado.ioloop.IOLoop.instance().start()
