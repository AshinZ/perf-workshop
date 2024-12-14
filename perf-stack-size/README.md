原文地址：[调用栈过深导致的火焰图错误该如何解决](https://mp.weixin.qq.com/s/WjdipzzUQU-rE_DyLAjnlQ)

文件用途:
- main.cpp: 源文件
- stackcollapse-perf.pl: 栈折叠文件
- flamegraph.pl: 生成火焰图

编译：
g++ -g -o main -fno-omit-frame-pointer main.cpp

数据收集：
perf record -g -F 200 ./main
perf script > perf.unfold
 ./stackcollapse-perf.pl perf.unfold > perf.folded
 ./flamegraph.pl perf.folded > perf.svg
