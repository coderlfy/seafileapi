#-*- coding: utf-8 -*-


class FilterHelper(object):
    @staticmethod
    def getData(data, filter):
        if isinstance(filter, FilterBool):
            for row in data:
                for c in range(len(row)-1, -1, -1):
                    if filter.visibleColumns[c] == False:
                        row.pop(c)

        return data