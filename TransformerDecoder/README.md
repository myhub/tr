# TransformerDecoder

本项目暂无任何实用价值，仅用于测试TransformerDecoder的推理能力，算法细节可参考：<br>
https://www.zhihu.com/question/605567747/answer/3441552623

测试环境: *Ubuntu 18+*

<table>
<tr><th>任务</th><th>状态</th><th>说明</th></tr>
<tr><td>三位整数乘法</td>

<td>
测试精度约为99.991%
</td>

<td>
不依赖CoT、编程等任何辅助方式<br>
Transformer层数：7<br>

[训练数据集](./dataset_m3.py)
[测试代码](https://github.com/myhub/models/releases/download/1.0/GPT_m3.zip)

</td>

</tr>

<tr><td>数数

[问题描述](https://www.zhihu.com/question/632647147/answer/3446033605)

</td>
<td>测试精度约为99.974%</td>
<td>
统计字符串中字母的个数<br>
按“single character”分词<br>
不依赖CoT、编程等任何辅助方式<br>
Transformer层数：7<br>

[训练数据集](./dataset_count.py)
[测试代码](https://github.com/myhub/models/releases/download/1.0/GPT_count.zip)

</td>

</tr>


<tr><td>数数

[问题描述](https://www.zhihu.com/question/632647147/answer/3446033605)

</td>
<td>测试精度约为99.937%</td>
<td>
统计字符串中字母的个数<br>
按“single word”分词<br>
不依赖CoT、编程等任何辅助方式<br>
Transformer层数：7<br>

[训练数据集](./dataset_count_word.py)
[测试代码](https://github.com/myhub/models/releases/download/1.0/GPT_count_word.zip)

</td>

</tr>

</table>

#### 路径规划
1. [基于Transformer的路径规划 - 第一篇 探索](https://zhuanlan.zhihu.com/p/695503967)
2. [基于Transformer的路径规划 - 第二篇 合成数据](https://zhuanlan.zhihu.com/p/697518598)
3. [基于Transformer的路径规划 - 第三篇 Attention Is All You Need](https://zhuanlan.zhihu.com/p/698148082)
4. [基于Transformer的路径规划 - 第四篇 GPT模型优化](https://zhuanlan.zhihu.com/p/699122636)
5. [基于Transformer的路径规划 - 第五篇 GPT生成策略_解码方法优化](https://zhuanlan.zhihu.com/p/699367747)
