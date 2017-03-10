project(RTD-example)
cmake_minimum_required(VERSION 3.2)

include_directories(src)
add_library(rtdexample myclass.cpp myclass.h)