from setuptools import find_packages, setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess
import os
import sys
import sysconfig

# try:
#     from Cython.Build import cythonize
# except ImportError:
#     subprocess.check_call([sys.executable, "-m", "pip", "install","-i","https://mirrors.aliyun.com/pypi/simple/", "Cython"])
#     from Cython.Build import cythonize
# # 自定义 build_ext，调用 CMake 构建


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
        build_lib = os.path.abspath(self.build_lib)
        os.makedirs(build_lib, exist_ok=True)
        python_include_dir = sysconfig.get_path('include')
        # 获取 Cython 的可执行文件路径
        python_bin_dir = sysconfig.get_path("scripts")  # 获取 Python 的 bin 目录
        cython_executable = os.path.join(python_bin_dir, "cython")
        os.environ["CYTHON_EXECUTABLE"] = cython_executable
     
        cmake_args = [
            f"-DPython3_EXECUTABLE={sys.executable}",
            f"-DPython3_INCLUDE_DIRS={python_include_dir}",
            f"-DCYTHON_EXECUTABLE={cython_executable}",
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={build_lib}",  # 指定动态库输出目录
        ]
        # build_args = []

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        nproc = os.cpu_count()
        project_root = os.path.abspath(os.path.dirname(__file__))
        cmake_source_dir = project_root  # 假设 CMakeLists.txt 在项目根目录
        # print(f"Library output directory: {self.build_lib}")

        # 执行 CMake 和构建
        subprocess.check_call(["cmake", cmake_source_dir] +
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
    url="https://github.com/begonia-org/pyoffice",
    platforms=["Linux"],
    project_urls={
        "Source": "https://github.com/begonia-org/pyoffice",
        "Tracker": "https://github.com/begonia-org/pyoffice/issues",
        "Documentation": "https://github.com/begonia-org/pyoffice",
    },
    description="A Python library for handling Microsoft Office documents, \
        built with [LibreOfficeKit](https://docs.libreoffice.org/libreofficekit.html).",
    ext_modules=extensions,
    cmdclass={
        "build_ext": CMakeBuild,
    },
    zip_safe=False,
    packages=find_packages(),
    package_data={
        "pyoffice": ["*.pyx", "*.so", "liboffice.so"],  # 指定要打包的文件
    },
    include_package_data=True,  # 启用 MANIFEST.in
    requires=[
        "Cython",
        "pybind11"
    ],
    install_requires=[
        "Cython",
        "pybind11"
    ],
)
