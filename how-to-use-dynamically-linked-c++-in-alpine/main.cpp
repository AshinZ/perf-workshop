// main.cpp
#include <iostream>
#include "math_lib.h"

int main() {
    int result = add(5, 3);
    std::cout << "5 + 3 = " << result << std::endl;

    result = subtract(10, 4);
    std::cout << "10 - 4 = " << result << std::endl;

    return 0;
}