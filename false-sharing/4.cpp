#include <iostream>
#include <chrono>
#include <thread>
#include <vector>

const int NUM_THREADS = 4;
const int NUM_ITERATIONS = 10000000;

struct Data {
    int value; // 初始化为0
};

Data data[NUM_THREADS]; // 数组，存放每个线程的数据

void increment(int index) {
    for (int i = 0; i < NUM_ITERATIONS; ++i) {
        data[index].value++; // 存在伪共享问题
    }
}

int main() {
    std::vector<std::thread> threads;
    data[0].value = 0;
    data[1].value = 0;
    data[2].value = 0;
    data[3].value = 0;
    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < NUM_THREADS; ++i) {
        threads.emplace_back(increment, i);
    }

    for (auto& thread : threads) {
        thread.join();
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    std::cout << "Execution time: " << duration.count() << " seconds" << std::endl;

    return 0;
}