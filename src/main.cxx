#include "office.hpp"

int main(int argc, char *argv[])
{
    office::Office office("/usr/lib/libreoffice/program");
    office.saveAs("/data/work/office-converter/tests/data/en.doc", "/data/work/office-converter/tests/data/test_en.pdf", "pdf");
    office.saveAs("/data/work/office-converter/tests/data/test.xls", "/data/work/office-converter/tests/data/test_xls_cpp.pdf", "pdf");
    return 0;
}