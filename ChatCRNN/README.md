# ChatCRNN

本项目暂无任何实用价值，仅用于测试Transformer的推理能力，算法细节可参考：<br>
https://www.zhihu.com/question/605567747/answer/3441552623

<table>
<tr><th>任务</th><th>状态</th><th>说明</th></tr>
<tr><td>三位整数乘法</td><td>完美解决</td><td>不依赖CoT、编程等任何辅助方式

[训练数据集](./dataset_m3.py)
[测试代码](https://github.com/myhub/tr/releases/download/2.8.1/ChatCRNN_m3.zip)

</td></tr>
<tr><td>四位整数乘法</td><td>待验证</td><td>不依赖CoT、编程等任何辅助方式</td></tr>
<tr><td>逻辑运算
<ul>
<li>A=2,B=A-1,C=max(A, B),B+A-C=?</li>
<li>B=A+1,C=max(A, B),A=5,min(B,C)+A=?</li>
</ul>
</td><td>待验证</td><td>不依赖CoT、编程等任何辅助方式</td></tr>
</table>

**状态说明**<br>
完美解决：指推理精度达到100%
