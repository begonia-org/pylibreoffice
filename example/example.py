#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example.py
@Time    :   2024/11/23 23:00:09
@Desc    :   
'''


from pyoffice.py_office import PyOffice


class Example:
    def __init__(self):
        self.office = PyOffice("/usr/lib/libreoffice/program/")

    def doc(self):
        # Convert the doc file to pdf
        print(self.office.save_as("./test.doc", "./test.pdf", "pdf"))

    def xls(self):
        # Convert the xls file to pdf
        print(self.office.save_as("./test.xls", "./test_xls.pdf", "pdf"))


if __name__ == '__main__':
    ex = Example()
    ex.xls()
    ex.doc()
