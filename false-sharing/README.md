原文地址：[伪共享问题初探：根源与检测](https://mp.weixin.qq.com/s/9MVZ4OudBvhFx5XghPx0Tw)


文件用途:
- 4.cpp: 存在伪共享源文件
- 64.cpp: 修复后源文件

编译：
```shell
g++ -g -o 4 -O0 -fno-omit-frame-pointer -lpthread 4.cpp
g++ -g -o 64 -O0 -fno-omit-frame-pointer -lpthread 64.cpp
```

