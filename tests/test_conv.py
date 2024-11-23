#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_conv.py
@Time    :   2024/11/23 15:48:32
@Desc    :   
'''


import unittest
from pyoffice.py_office import PyOffice


class TestDocConverter(unittest.TestCase):
    def setUp(self) -> None:
        self.office = PyOffice("/usr/lib/libreoffice/program/")

    def test_doc_conv_pdf(self):
        ret = self.office.save_as("/data/work/office-converter/tests/data/test.doc",
                                  "/data/work/office-converter/tests/data/test.pdf", "pdf")
        self.assertTrue(ret)

    # def test_xls_conv_pdf(self):
    #     ret = self.office.save_as("/data/work/office-converter/tests/data/test.xls",
    #                               "/data/work/office-converter/tests/data/test.pdf", "pdf")
    #     self.assertTrue(ret)


if __name__ == '__main__':
    unittest.main()
