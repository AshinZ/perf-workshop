
  #include <iostream>
  #include <thread>
  #include <unistd.h>

  void alloc() {
    for (int i = 0; i < 100000; ++i) {
      int* a = (int*)malloc(4);
    }
  }

  int main() {
    sleep(1);
    std::thread t1 {&alloc};
    std::thread t2 {&alloc};
    t1.join();
    t2.join();
    sleep(10);
    return 0;
  }
