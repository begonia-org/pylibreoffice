#include "office.hpp"
// #include <lok/Office.hxx>
// #include <lok/Document.hxx>
namespace office
{
    Office::Office(const std::string &bin_dir)
    {
        office = lok::lok_cpp_init(bin_dir.c_str());
        // 设置选项
        office->setOption("EmbedStandardFonts", "true");
        office->setOption("PrintArea", "A1:Z50");
        office->setOption("ReduceImageResolution", "false");
        office->setOption("UseLosslessCompression", "true");
        office->setOption("headless", "true");
        office->setOption("nocrashreport", "true");
    }
    Office::~Office()
    {
        if (office)
        delete office;
        office = nullptr;
    }
    bool Office::release()
    {
        if (office){
         delete office;

        }
        office = nullptr;
        return true;
    }
    bool Office::saveAs(const std::string &input_file, const std::string &output_file, const std::string &format)
    {
        lok::Document *document = office->documentLoad(input_file.c_str(), nullptr);
        if (!document)
        {
            return false;
        }
        bool ret = document->saveAs(output_file.c_str(), format.c_str(), nullptr);
        delete document;
        document = nullptr;
        return ret;
    }
} // namespace office
