cmake_minimum_required(VERSION 3.10...3.30)

project(pylibreoffice)

# 设置工作目录
set(WORKDIR "${CMAKE_CURRENT_SOURCE_DIR}")

# 设置编译器
set(CMAKE_CXX_COMPILER "g++")

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 设置编译选项
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ldl -Wall -W -Wno-shadow -Wno-unused-parameter -Wpointer-arith -Wcast-align")

# 打印 Python 环境信息
find_program(CYTHON_EXECUTABLE cython REQUIRED)
message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
message(STATUS "Python3_INCLUDE_DIRS: ${Python3_INCLUDE_DIRS}")

# 查找 LibreOfficeKit 的头文件和库
file(GLOB LIBREOFFICE_INCLUDE_DIRS
    "/opt/libreoffice*/sdk/include"
)

message(STATUS "LIBREOFFICE_INCLUDE_DIRS: ${LIBREOFFICE_INCLUDE_DIRS}")
find_path(LIBREOFFICE_INCLUDE_DIR LibreOfficeKit/LibreOfficeKit.hxx
          PATHS /usr/include /usr/local/include /opt/libreoffice/include ${LIBREOFFICE_INCLUDE_DIRS}
          PATH_SUFFIXES LibreOfficeKit)

find_library(LIBREOFFICE_LIBRARY "libreglo.so"
             PATHS /usr/lib /usr/local/lib /opt/libreoffice/lib "/usr/lib/libreoffice/program" "/usr/lib64/libreoffice/program")

if (LIBREOFFICE_INCLUDE_DIR AND LIBREOFFICE_LIBRARY)
    message(STATUS "LibreOfficeKit found:")
    message(STATUS "  Include directory: ${LIBREOFFICE_INCLUDE_DIR}")
    message(STATUS "  Library: ${LIBREOFFICE_LIBRARY}")
else()
    message(FATAL_ERROR "LibreOfficeKit not found. Please install libreoffice.")
endif()

include_directories(${LIBREOFFICE_INCLUDE_DIR})

################################# 生成 office 库 #################################
file(GLOB OFFICE_SRCS "${WORKDIR}/src/*.cxx")
add_library(office SHARED ${OFFICE_SRCS})


#################### 编译生成 Cython 模块 ####################
set(CYTHON_CPP_FILE "${WORKDIR}/src/py_office.cpp")

add_custom_command(
    OUTPUT ${CYTHON_CPP_FILE}
    COMMAND ${CYTHON_EXECUTABLE} -3 --cplus ${WORKDIR}/pylibreoffice/py_office.pyx -o ${CYTHON_CPP_FILE}
    DEPENDS ${WORKDIR}/pylibreoffice/py_office.pyx
    COMMENT "Generating C++ code from Cython pyx file"
)

add_library(py_office SHARED ${CYTHON_CPP_FILE} ${OFFICE_SRCS})
set_target_properties(py_office PROPERTIES PREFIX "")

target_include_directories(py_office PRIVATE ${Python3_INCLUDE_DIRS})



################################# 生成 demo 程序 #################################
file(GLOB TEST_SRCS "${WORKDIR}/src/main.cxx")
add_executable(pyoffice_demo ${TEST_SRCS})

target_link_libraries(pyoffice_demo PRIVATE office)
target_link_libraries(pyoffice_demo PRIVATE dl)

# 安装 demo 程序
install(TARGETS pyoffice_demo
    RUNTIME DESTINATION bin
)

############################### pybind11 模块 ####################################
find_package(pybind11 REQUIRED)
pybind11_add_module(pybind11_office src/pybind_office.cpp src/office.cxx)



