#-*- coding: utf-8 -*-


#本类由调用者根据业务进行调整
class DataWrapper(object):
    def __init__(self):
        #检索出的数据由多少列，元祖容量就是多少个
        #若不需要转换的列，直接置空
        self.wrapperFunctions = (
            WrapperHelper.cutID,
            ''
         )