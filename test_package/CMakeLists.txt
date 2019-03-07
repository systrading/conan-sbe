cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

#add_custom_target(generate-stubs
#        COMMAND java -Dsbe.target.language=CPP -Dsbe.target.namespace="aeron::bridge::protocol" -jar /opt/fairtide/tools/sbe/lib/sbe-all.jar $HERE/external/fairtideservice/sbe/ft_serv/feed_handler.xml)
#
add_executable(example example.cpp)


# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
