# pyoffice

A Python library for handling Microsoft Office documents, built with [LibreOfficeKit](https://docs.libreoffice.org/libreofficekit.html).

## Features

- Convert Microsoft Office documents to PDF

## Installation
### Requirements
- Python 3.10 or higher

- LibreOffice 7.2 or higher

- The fonts used in the document must be installed on the system.For example,use Chinese, on Ubuntu, you can install the fonts by running the following command:
```bash
sudo apt-get install -y fonts-wqy-zenhei fonts-wqy-microhei xfonts-intl-chinese ttf-wqy-zenhei ttf-wqy-microhei language-pack-zh-hans language-pack-zh-hant && \
sudo dpkg-reconfigure locales && \
sudo update-locale LANG=zh_CN.UTF-8
```

```bash
pip install pyoffice
```

## Example

```python
from pyoffice.py_office import PyOffice

if __name__ == '__main__':
    # The path to the installed LibreOffice or the LibreOfficeKit library.
    office = PyOffice("/usr/lib/libreoffice/program/")
    # Convert the doc file to pdf
    print(office.save_as("./test.doc", "./test.pdf", "pdf"))
```