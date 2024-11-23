#ifndef OFFICE_HPP
#define OFFICE_HPP

#include <string>
#include <memory>

#include "LibreOfficeKit/LibreOfficeKit.hxx"
namespace office{
class Office {
public:
    Office(const std::string& bin_dir);
    ~Office();

    bool saveAs(const std::string &input_file, const std::string& output_file, const std::string& format);

private:
    lok::Office *office = nullptr;
};
} // namespace office


#endif // OFFICE_HPP