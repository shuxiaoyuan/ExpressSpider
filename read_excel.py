#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/12/13 11:20
# @Description: 从 excel 中读取快递单号

import xlrd


class ExcelReader:

    def __init__(self):
        self.__row_express_num = 1
        self.__column_express_num = 17
        self.__express_num_list = []

    def get_express_num_list(self, path):
        excel = xlrd.open_workbook(path)
        sheet = excel.sheets()[0]
        for i in range(self.__row_express_num, sheet.nrows):
            self.__express_num_list.append(sheet.cell_value(i, self.__column_express_num))
        return self.__express_num_list


if __name__ == '__main__':
    excel_reader = ExcelReader()
    express_num_list = excel_reader.get_express_num_list('./test.xlsx')

    print('len: %d' % len(express_num_list))
    for express_num in express_num_list:
        print(express_num)
