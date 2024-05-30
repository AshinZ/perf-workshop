原文地址：[没有调试信息如何perf script](https://mp.weixin.qq.com/s/qbxv0yDOLnnNJBQX1COs6g)


文件用途:
- main.cpp: 源文件
- math_lib.cpp: 第三方库模拟文件
- math_lib.h: 第三方库头文件
- CmakeLists.txt: Cmakelist
- lib-alpine: 已经准备好的lib库，可以在启动alpine后使用该lib库

编译：
```shell
mkdir build & cd build
cmake ..
make
```


