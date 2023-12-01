cmake_minimum_required(VERSION 3.12)
project(AoC2023)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)

# Add the main file-reader.cpp to the project
add_library(file_reader file-reader.cpp)

# Collect all source files in the project directory
file(GLOB SOURCE_FILES *.cpp)

# Exclude file-reader.cpp from the list of source files
list(FILTER SOURCE_FILES EXCLUDE REGEX "file-reader.cpp")

# Create an executable for each source file
foreach(SOURCE_FILE ${SOURCE_FILES})
    get_filename_component(EXECUTABLE_NAME ${SOURCE_FILE} NAME_WE)
    add_executable(${EXECUTABLE_NAME} ${SOURCE_FILE})
    target_link_libraries(${EXECUTABLE_NAME} PRIVATE file_reader)
endforeach()