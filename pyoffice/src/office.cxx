#include "office.hpp"

namespace office
{
    Office::Office(const std::string &bin_dir)
    {
        printf("bin_dir: %s\n", bin_dir.c_str());
        office = lok::lok_cpp_init(bin_dir.c_str());
    }
    Office::~Office()
    {
        delete office;
    }
    bool Office::saveAs(const std::string &input_file, const std::string &output_file, const std::string &format)
    {
        lok::Document *document = office->documentLoad(input_file.c_str(), nullptr);
        if (!document)
        {
            printf("documentLoad failed %s\n",office->getError());
            return false;
        }
        
        bool ret = document->saveAs(output_file.c_str(), format.c_str(), nullptr);
        printf("saveAs: %d\n", ret);
        delete document;
        return ret;
    }
} // namespace office
