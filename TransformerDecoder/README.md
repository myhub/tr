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
[测试代码](https://github.com/myhub/tr/releases/download/2.8.2/GPT_m3.zip)

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
[测试代码](https://github.com/myhub/tr/releases/download/2.8.2/GPT_count.zip)

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
[测试代码](https://github.com/myhub/tr/releases/download/2.8.2/GPT_count_word.zip)

</td>

</tr>

</table>

#### 问题记录
+ 在一些NLP任务（例如小说续写）上效果较差
+ 当batch_size过大（例如超过64）时模型难以收敛，过小的batch_size导致模型训练效率降低
+ 训练不稳定，容易发生梯度爆炸

