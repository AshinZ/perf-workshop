// g++ -g -O0 -o test main.cpp
// perf record -e br_inst_retired.all_branches ./test
// perf record -e br_inst_retired.all_branches:ppp ./test
#include<iostream>

int main() {
    for (int i = 0; i < 999999999; ++i) {
        asm volatile("nop");
        asm volatile("nop");
        asm volatile("nop");
        asm volatile("nop");

        asm volatile("nop");
        asm volatile("nop");
        asm volatile("nop");
        asm volatile("nop");

        asm volatile("nop");
        asm volatile("nop");
        asm volatile("nop");
        asm volatile("nop");
    }
    return 0;
}