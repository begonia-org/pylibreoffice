# cython: language_level=3
# distutils: sources = src/office.cxx
# py_office.pyx
# distutils: language=c++
# cython: c_string_type=unicode, c_string_encoding=utf8

from libcpp.string cimport string
from libc.stdlib cimport malloc, free
from libc.string cimport strcpy, strlen

cdef extern from "office.hpp" namespace "office":
    cdef cppclass Office:
        Office(string bin_dir)
        # saveAs(const std::string& output_file, const std::string& format)
        bint saveAs(string input_file, string output_file, string out_format)
        bint release()

cdef class CyOffice:
    cdef Office* office  # 声明 C++ 指针

    def __cinit__(self, str libreoffice_dir="/usr/lib/libreoffice/program"):
        self.office = new Office(libreoffice_dir)
    
    def __dealloc__(self):
        if self.office is not NULL:
            del self.office
            self.office = NULL
    
    def save_as(self, str input_file, str output_file, out_format="pdf")->bool:
        return self.office.saveAs(input_file, output_file, out_format)
    def release(self):
        self.office.release()
