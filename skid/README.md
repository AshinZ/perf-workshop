原文地址：[眼见为虚-perf skid问题简介](https://mp.weixin.qq.com/s/PPd4hbLPgAYOleJN9QZbeg)


文件用途:
- main.cpp: 测试文件

编译：
```shell
g++ -g -O0 -o test main.cpp
```

采集：
```shell
perf record -e br_inst_retired.all_branches ./test
perf record -e br_inst_retired.all_branches:ppp ./test
```
