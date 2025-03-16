原文地址：[你真的会用差分火焰图吗](https://mp.weixin.qq.com/s/rij6Gls7Ar6gNcVnh9HJpA)


文件用途:
- diff1: diff1文件
- diff2: 样本数不一致
- diff3: 调用栈新增/缺失
- diff4: 调用栈更名
- diff1-2: diff1和diff2直接diff的结果，只有一种颜色
- diff1-2-n: diff1和diff2的归一对比结果
- diff1-3-n: diff1和diff3的归一对比结果
- diff1-4-n: diff1和diff4的归一对比结果
- *.svg: 对应diff结果的火焰图
- flamegraph.pl: 生成火焰图脚本 - https://github.com/brendangregg/FlameGraph
- difffolded.pl: 对比脚本 - https://github.com/brendangregg/FlameGraph