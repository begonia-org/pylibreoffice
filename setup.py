import logging
import site
from skbuild import cmaker, setup
from setuptools import find_packages
import subprocess
import os
import sys
import sysconfig
import pybind11


def main():
    # build_lib = os.path.abspath(self.build_lib)
    # os.makedirs(build_lib, exist_ok=True)
    python_include_dir = sysconfig.get_path('include')
    # 获取 Cython 的可执行文件路径
    python_bin_dir = sysconfig.get_path("scripts")  # 获取 Python 的 bin 目录
    cython_executable = os.path.join(python_bin_dir, "cython")
    os.environ["CYTHON_EXECUTABLE"] = cython_executable
    pybind11_dir = pybind11.get_cmake_dir()
    site_packages = site.getsitepackages()
    print(f"site_packages: {site_packages}")
    cmake_args = [
        f"-DPython3_EXECUTABLE={sys.executable}",
        f"-DPython3_INCLUDE_DIRS={python_include_dir}",
        f"-DCYTHON_EXECUTABLE={cython_executable}",
        f"-Dpybind11_DIR={pybind11_dir}",
        f"-DLIBRARY_OUTPUT_PATH={site_packages[0]}/pylibreoffice",
    ]
    setup(
        name="pylibreoffice",
        version="0.1.2",
        author="vforfreedom",
        url="https://github.com/begonia-org/pylibreoffice",
        platforms=["Linux"],
        project_urls={
            "Source": "https://github.com/begonia-org/pylibreoffice",
            "Tracker": "https://github.com/begonia-org/pylibreoffice/issues",
            "Documentation": "https://github.com/begonia-org/pylibreoffice",
        },
        description="A Python library for handling Microsoft Office documents, \
        built with [LibreOfficeKit](https://docs.libreoffice.org/libreofficekit.html).",

        zip_safe=False,
        packages=find_packages(exclude=["tests", "tests.*", "*.egg-info", "*.egg-info.*", "__pycache__", "_skbuild"]),
        package_data={
            # 指定要打包的文件
            "pylibreoffice": ["*.pyx", "*.so", "liboffice.so", "**/*.so"],
        },
        include_package_data=True,  # 启用 MANIFEST.in
        cmake_args=cmake_args,
        cmake_source_dir=".",
    )


if __name__ == "__main__":
    main()
