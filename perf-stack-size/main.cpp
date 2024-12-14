#include <iostream>

// 一个示例的计算操作
long long heavyComputation(int n) {
    long long result = 0;
    for (int i = 0; i < n; ++i) {
        result += i * i; // 示例计算：求和平方
    }
    return result;
}

// 递归函数
void recursiveFunction(int current, int maxDepth) {
    if (current > maxDepth) {
        return;
    }

    // 递归调用
    recursiveFunction(current + 1, maxDepth);

    // 在最后一次和倒数第二次递归时进行大量计算
    if (current == maxDepth || current == maxDepth - 1 || current == 1 || current == 10) {
        std::cout << "进行大量计算，当前深度: " << current << std::endl;
        long long result = heavyComputation(100000000); // 示例计算
        std::cout << "计算结果: " << result << std::endl;
    }
}

int main() {
    int i = 128; // 设置递归深度
    recursiveFunction(1, i);
    return 0;
}
