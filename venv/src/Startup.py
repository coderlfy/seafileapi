#-*- coding: utf-8 -*-


import tornado.ioloop
import handler.SeafileHandler
import logging
# define the log file, file mode and logging level
logging.basicConfig(filename='debug.log',
                    filemode="w",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

settings = {
    'debug': False
}
application = tornado.web.Application([
    (r"/SeafileManager/add", handler.SeafileHandler.AddFile),
    (r"/SeafileManager/get", handler.SeafileHandler.GetFile),
    (r"/SeafileManager/delete", handler.SeafileHandler.DeleteFile),
    (r"/SeafileManager/clear", handler.SeafileHandler.ClearFile),
    (r"/SeafileManager/getuploadurl", handler.SeafileHandler.UploadLink)
], **settings)
if __name__ == "__main__":
    application.listen(28888)
    tornado.ioloop.IOLoop.instance().start()
