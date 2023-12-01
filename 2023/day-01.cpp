// Advent of Code 2023
// Day 1: Trebuchet?!
// https://adventofcode.com/2023/day/1

#include <string>
#include <vector>

#include "file-reader.cpp"

const std::string FILE_NAME = "day-01-input.txt";

void replaceDigitsWithWords(std::string& line, const std::vector<std::string>& digits) {
    for (int i = 0; i < digits.size(); ++i) {
        std::string substring = std::to_string(i);
        size_t position = line.find(substring);

        while (position != std::string::npos) {
            line.replace(position, substring.length(), digits.at(i));
            position = line.find(substring, position + digits.at(i).length());
        }
    }
}

size_t findFirstDigit(std::string& str, std::vector<std::string>& digits) {
    size_t digit = 0;
    size_t position = std::string::npos;

    for (size_t i = 0; i < digits.size(); ++i) {
        size_t substringPosition = str.find(digits.at(i));
        if (substringPosition != std::string::npos && substringPosition < position) {
            position = substringPosition;
            digit = i;
        }
    }

    return digit;
}

size_t findLastDigit(std::string& str, std::vector<std::string>& digits) {
    size_t digit = 0;
    size_t position = 0;

    for (size_t i = 0; i < digits.size(); ++i) {
        size_t substringPosition = str.find(digits.at(i));

        while (substringPosition != std::string::npos) {
            if (substringPosition > position) {
                position = substringPosition;
                digit = i;
            }
            substringPosition = str.find(digits.at(i), substringPosition + 1);
        }
    }

    return digit;
}

int main() {
    std::vector<std::string> lines{};
    if (!readFile(FILE_NAME, lines)) return EXIT_FAILURE;

    size_t sum = 0;
    std::vector<std::string> digits = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for (std::string line : lines) {
        replaceDigitsWithWords(line, digits);

        size_t firstDigit = findFirstDigit(line, digits);
        size_t lastDigit = findLastDigit(line, digits);

        sum += firstDigit * 10 + lastDigit;
    }

    std::cout << "PUZZLE RESULT: " << sum;
    return EXIT_SUCCESS;
}