#!/usr/bin/bash

# Build the project
echo "Building the project..."
python3.6 setup.py sdist bdist_wheel
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:pylibreoffice/
auditwheel repair dist/pylibreoffice-0.1.0-cp36-cp36m-linux_x86_64.whl -w dist && mv wheelhouse/* dist/ && rm -rf wheelhouse && rm -rf dist/*-linux_x86_64.whl
