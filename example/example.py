#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example.py
@Time    :   2024/11/23 23:00:09
@Desc    :   
'''

import os
from pylibreoffice.core import PyOffice


class Example:
    def __init__(self):
        self.office = PyOffice("/usr/lib/libreoffice/program/")
        # self.office2 = pybind_office.Office("/usr/lib/libreoffice/program/")

    def doc(self):
        # Convert the doc file to pdf
        base_path = os.path.dirname(os.path.abspath(__file__))

        print(self.office.save_as(os.path.join(base_path, "test.doc"), os.path.join(base_path, "test.pdf"), "pdf"))

    def xls(self):
        # Convert the xls file to pdf
        base_path = os.path.dirname(os.path.abspath(__file__))

        print(self.office.save_as(os.path.join(base_path, "test.xls"), os.path.join(base_path, "test_xls.pdf"), "pdf"))


if __name__ == '__main__':
    ex = Example()
    ex.xls()
    ex.doc()
