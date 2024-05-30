cmake_minimum_required(VERSION 3.10)
project(MathLibExample)

# 编译数学库
add_library(math_lib SHARED math_lib.cpp)
target_include_directories(math_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# 编译调用库的主程序
add_executable(main main.cpp)
target_link_libraries(main math_lib)

# 设置RPATH
set_target_properties(main PROPERTIES
    INSTALL_RPATH "$ORIGIN/../lib"
    RPATH "$ORIGIN/../lib")

# 设置输出目录
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR}/lib)