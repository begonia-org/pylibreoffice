cmake_minimum_required(VERSION 3.10)
project(pyoffice)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
# 根据构建类型设置输出目录
set(WORKDIR "${CMAKE_CURRENT_SOURCE_DIR}")

set(LIBREOFFICE_DIR "${WORKDIR}/../core/include")

# 设置编译器
set(CMAKE_CXX_COMPILER "g++")

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 设置编译选项
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -Wall -W -Wno-shadow -Wno-unused-parameter -Wpointer-arith -Wcast-align")

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
include_directories(${Python3_INCLUDE_DIRS})
find_program(CYTHON_EXECUTABLE cython REQUIRED)
message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
message(STATUS "Python3_INCLUDE_DIRS: ${Python3_INCLUDE_DIRS}")
message(STATUS "Python3_LIBRARIES: ${Python3_LIBRARIES}")
message(STATUS "Python3_SITEARCH is: ${Python3_SITEARCH}")
# 查找 LibreOfficeKit 的头文件
find_path(LIBREOFFICE_INCLUDE_DIR LibreOfficeKit/LibreOfficeKit.hxx
          PATHS /usr/include /usr/local/include /opt/libreoffice/include ${LIBREOFFICE_DIR}
          PATH_SUFFIXES LibreOfficeKit)

# 查找 LibreOfficeKit 的库文件
find_library(LIBREOFFICE_LIBRARY libmergedlo.so
             PATHS /usr/lib /usr/local/lib /opt/libreoffice/lib "/usr/lib/libreoffice/program/" "/usr/lib64/libreoffice/program/")

# 检测是否找到头文件和库
if (LIBREOFFICE_INCLUDE_DIR AND LIBREOFFICE_LIBRARY)
    message(STATUS "LibreOfficeKit found:")
    message(STATUS "  Include directory: ${LIBREOFFICE_INCLUDE_DIR}")
    message(STATUS "  Library: ${LIBREOFFICE_LIBRARY}")
else()
    message(FATAL_ERROR "LibreOfficeKit not found. Please install libreoffice-dev.")
endif()

include_directories(${LIBREOFFICE_INCLUDE_DIR}, ${LIBREOFFICE_DIR})

#################################生成office库#################################
# 指定 src/ 下的源文件
file(GLOB OFFICE_SRCS "${WORKDIR}/src/*.cxx")
list(APPEND OFFICE_SRCS
)


# 创建共享库
add_library(office SHARED ${OFFICE_SRCS})
# 设置共享库的输出路径
set_target_properties(office PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${WORKDIR}/pyoffice
)
####################编译生成cython模块####################
# 生成py_office.cpp

# 定义 Cython 生成的 .cpp 文件路径
set(CYTHON_CPP_FILE "${WORKDIR}/src/py_office.cpp")

# 使用 Cython 将 .pyx 文件转换为 .cpp 文件
add_custom_command(
    OUTPUT ${CYTHON_CPP_FILE}
    COMMAND ${CYTHON_EXECUTABLE} -3 --cplus ${WORKDIR}/pyoffice/py_office.pyx -o ${CYTHON_CPP_FILE}
    DEPENDS ${WORKDIR}/pyoffice/py_office.pyx
    COMMENT "Generating C++ code from Cython pyx file"
)

# 创建 Cython 共享库
add_library(py_office SHARED ${CYTHON_CPP_FILE})
# 设置输出路径
set_target_properties(py_office PROPERTIES PREFIX "")
set_target_properties(py_office PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${WORKDIR}/pyoffice"
)

# 链接库到共享库
target_include_directories(py_office PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(py_office PRIVATE ${Python3_LIBRARIES} office)

#################################生成demo程序#################################
# 指定测试程序的源文件
file(GLOB TEST_SRCS "${WORKDIR}/src/main.cxx")

# 创建可执行文件
add_executable(pyoffice_demo ${TEST_SRCS})
# 设置可执行文件的输出路径
set_target_properties(pyoffice_demo PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${WORKDIR}"
)

# 链接库到可执行文件
target_link_libraries(pyoffice_demo PRIVATE office)




