from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess
import os
import sys
import sysconfig


# 自定义 build_ext，调用 CMake 构建
class CMakeBuild(build_ext):
    def run(self):
        # 确保 CMake 可用
        try:
            subprocess.check_call(["cmake", "--version"])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        # 构建每个扩展
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):

        cmake_args = [
            f"-DPython3_EXECUTABLE={sys.executable}",
            f"-DPython3_LIBRARIES={sysconfig.get_config_var('LIBDIR')}",
        ]
        # build_args = []

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        nproc = os.cpu_count()
        # 执行 CMake 和构建
        subprocess.check_call(["cmake", "../../"] +
                              cmake_args, cwd=self.build_temp)
        subprocess.check_call(["make", "-j", f"{nproc}"], cwd=self.build_temp)


# 定义扩展模块，指向 CMakeLists.txt 所在目录
extensions = [
    Extension(
        "pyoffice.py_office",  # Python 模块名
        sources=[],            # 不需要提供 .pyx 或 .cpp，因为由 CMake 管理
    )
]

# 配置 setup
setup(
    name="pyoffice",
    version="0.1.0",
    author="vforfreedom",
    description="A Python library for handling Microsoft Office documents, \
        built with [LibreOfficeKit](https://docs.libreoffice.org/libreofficekit.html).",
    ext_modules=extensions,
    cmdclass={
        "build_ext": CMakeBuild,
    },
    zip_safe=False,
)
