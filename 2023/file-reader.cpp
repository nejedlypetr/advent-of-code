#include <iostream>
#include <fstream>
#include <vector>

static bool readFile(const std::string& fileName, std::vector<std::string>& lines) {
    std::ifstream in{"../" + fileName};

    if (!in.is_open()) {
        std::cerr << "Cannot open file " << fileName << std::endl;
        return false;
    }

    std::string str;
    try {
        while (std::getline(in, str)) {
            lines.push_back(str);
        }
    } catch (const std::exception& e) {
        std::cerr << "Exception while reading from file " << fileName << ": " << e.what() << std::endl;
        return false;
    }

    return true;
}
