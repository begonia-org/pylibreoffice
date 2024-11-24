#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pyoffice.py
@Time    :   2024/11/23 23:13:55
@Desc    :   
'''

from pyoffice.py_office import CyOffice


class PyOffice:
    def __init__(self, libreoffice_dir="/usr/lib/libreoffice/program"):
        self.__office = CyOffice(libreoffice_dir)

    def save_as(self, src: str, dest: str, fmt: str = "pdf") -> bool:
        return self.__office.save_as(src, dest, fmt)
