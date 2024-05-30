原文地址：[消失的八字节-bcc memleak修复经历分享](https://mp.weixin.qq.com/s/my-HAe_K6_Iiot3cjGUN1g)


文件用途:
- main.cpp: 测试文件
- memleak.py: 修复前的py文件
- memleak-done.py: 修复后的文件


运行：
```shell
# 编译test.cpp
g++ -g -o test test.cpp -lpthread
# 运行memleak
python3 memleak.py -c ./test --combined-only
# 追踪模式运行memleak
python3 memleak.py -c ./test --combined-only -t
```