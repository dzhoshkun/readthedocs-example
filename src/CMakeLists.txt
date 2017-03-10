project(RTD-example)
cmake_minimum_required(VERSION 3.2)

include_directories(src)
add_library(rtdexample myclass.cpp myclass.h)

set(DOXYFILE_IN ${CMAKE_CURRENT_SOURCE_DIR}/../doc/Doxyfile.in)
set(DOXYFILE ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)
configure_file(${DOXYFILE_IN} ${DOXYFILE} @ONLY)
