#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // 支持 STL 容器，如 std::string
#include "office.hpp"

namespace py = pybind11;

PYBIND11_MODULE(pybind11_office, m) {
    m.doc() = "Pybind11 bindings for Office class";

    // 绑定 office::Office 类
    py::class_<office::Office>(m, "Office")
        .def(py::init<const std::string &>(), py::arg("bin_dir"),
             "Initialize the Office instance with LibreOffice binary directory")
        .def("save_as", &office::Office::saveAs, 
             py::arg("input_file"), py::arg("output_file"), py::arg("format"),
             "Save the input file to the specified output format")
        .def("release", &office::Office::release, "Release resources");
}
