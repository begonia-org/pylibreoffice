#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_conv.py
@Time    :   2024/11/23 15:48:32
@Desc    :   
'''


import time
import unittest
from pylibreoffice.core import PyOffice


class TestDocConverter(unittest.TestCase):
    # def __init__(self, methodName: str = "runTest") -> None:
    #     super().__init__(methodName)
    #     print("init")

    def setUp(self) -> None:
        pass
        # self.office = PyOffice("/usr/lib/libreoffice/program/")

    def test_doc_conv_pdf(self):
        print("test_doc_conv_pdf")
        # ret = self.office.save_as("/data/work/office-converter/tests/data/test.doc",
        #                           "/data/work/office-converter/tests/data/test.pdf", "pdf")
        self.assertTrue(True)

    def test_xls_conv_pdf(self):
        print("test_xls_conv_pdf")
        self.office = PyOffice("/usr/lib/libreoffice/program/")
        ret = self.office.save_as("/data/work/office-converter/tests/data/test.doc",
                                  "/data/work/office-converter/tests/data/test.pdf", "pdf")
        self.assertTrue(ret)
        start = time.time()
        ret = self.office.save_as("/data/work/office-converter/tests/data/test.xls",
                                  "/data/work/office-converter/tests/data/test_xls.pdf", "pdf")
        end = time.time()
        print(f"Conversion time: {end - start:.2f} seconds")
        self.assertTrue(ret)
        time.sleep(30)

    def tearDown(self) -> None:
        # self.office.release()
        # del self.office
        # gc.collect()  # 主动触发垃圾回收

        pass


if __name__ == '__main__':
    unittest.main()
