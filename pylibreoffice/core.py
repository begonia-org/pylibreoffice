#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pylibreoffice.py
@Time    :   2024/11/23 23:13:55
@Desc    :   
'''

# 添加 pylibreoffice 目录到 sys.path
from pylibreoffice.py_office import CyOffice
import pylibreoffice.pybind11_office as _pybind11_office  # type: ignore


class PyOffice:
    def __init__(self, libreoffice_dir="/usr/lib/libreoffice/program", bridge="pybind11"):
        if bridge == "pybind11":
            self.__office = _pybind11_office.Office(libreoffice_dir)
        else:
            self.__office = CyOffice(libreoffice_dir)

    def save_as(self, src: str, dest: str, fmt: str = "pdf") -> bool:
        return self.__office.save_as(src, dest, fmt)
