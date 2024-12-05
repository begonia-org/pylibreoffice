# pylibreoffice

A Python library for handling Microsoft Office documents, built with [LibreOfficeKit](https://docs.libreoffice.org/libreofficekit.html).

## Features

- Convert Microsoft Office documents to PDF

## Installation
### Requirements
- Python 3.10 or higher

- LibreOffice 7.2 or higher
```bash
sudo apt-get install -y libreoffice libreoffice-dev libreoffice-dev-doc
```

- The fonts used in the document must be installed on the system.For example,use Chinese, on Ubuntu, you can install the fonts by running the following command:
```bash
sudo apt-get install -y fonts-wqy-zenhei fonts-wqy-microhei xfonts-intl-chinese ttf-wqy-zenhei ttf-wqy-microhei language-pack-zh-hans language-pack-zh-hant && \
sudo dpkg-reconfigure locales && \
sudo update-locale LANG=zh_CN.UTF-8
```

```bash
pip install pylibreoffice
```

## Example

```python
from pylibreoffice.core import PyOffice


class Example:
    def __init__(self):
        self.office = PyOffice("/usr/lib/libreoffice/program/")

    def doc(self):
        # Convert the doc file to pdf
        print(self.office.save_as("./test.doc", "./test.pdf", "pdf"))

    def xls(self):
        # Convert the xls file to pdf
        print(self.office.save_as("./test.xls", "./test_xls.pdf", "pdf"))


if __name__ == '__main__':
    ex = Example()
    ex.xls()
    ex.doc()
```