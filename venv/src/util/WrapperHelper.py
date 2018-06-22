#-*- coding: utf-8 -*-


class WrapperHelper(object):
    @staticmethod
    def toChange(selectResult, dataWrapper = ''):
        selectResult = list(selectResult)

        if dataWrapper == '':
            print 'no change'
        else:
            for rIndex in range(len(selectResult)):
                row = list(selectResult[rIndex])
                #print len(row)
                for c in range(len(row)):
                    if dataWrapper.wrapperFunctions[c] != '':
                        row[c] = dataWrapper.wrapperFunctions[c](row, c)

                selectResult[rIndex] = row;


        return selectResult

    @staticmethod
    def cutID(row, cIndex):
        return row[cIndex][0:3]

    @staticmethod
    def toCnDate(row, cIndex):
        return row[cIndex].strftime("%Y-%m-%d %H:%M:%S")

