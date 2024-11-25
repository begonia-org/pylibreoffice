#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // 支持 std::string 和其他 STL 容器
#include "office.hpp"

namespace py = pybind11;

// 定义 Python 类绑定
PYBIND11_MODULE(pybind11_office, m) {
    m.doc() = "Pybind11 bindings for Office";

    py::class_<Office>(m, "Office")
        .def(py::init<std::string>(), py::arg("bin_dir") = "/usr/lib/libreoffice/program")  // 绑定构造函数
        .def("save_as", &Office::saveAs, py::arg("input_file"), py::arg("output_file"), py::arg("out_format") = "pdf",
             "Save a file to a specific format")
        .def("release", &Office::release, "Release resources");

    py::class_<CyOffice>(m, "CyOffice")
        .def(py::init<std::string>(), py::arg("libreoffice_dir") = "/usr/lib/libreoffice/program")  // 构造函数
        .def("save_as", &CyOffice::save_as, py::arg("input_file"), py::arg("output_file"), py::arg("out_format") = "pdf",
             "Save a file")
        .def("release", &CyOffice::release, "Release resources");
}
