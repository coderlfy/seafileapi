#-*- coding: utf-8 -*-


#布尔型过滤器：哪列显示就置哪列为True（注：请确认列数一定与data的列数相同）
class FilterBool(object):
    def __init__(self):
         self.visibleColumns = (
            False,

            True
        )