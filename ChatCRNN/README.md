# ChatCRNN

本项目暂无任何实用价值，仅用于测试Transformer的推理能力，算法细节可参考：<br>
https://www.zhihu.com/question/605567747/answer/3441552623

<table>
<tr><th>任务</th><th>状态</th><th>说明</th></tr>
<tr><td>三位整数乘法</td>

<td>
测试精度约为99.994%
</td>

<td>
不依赖CoT、编程等任何辅助方式<br>
Transformer层数：7<br>

[训练数据集](./dataset_m3.py)
[测试代码](https://github.com/myhub/tr/releases/download/2.8.1/ChatCRNN_m3.zip)

</td>

</tr>
<tr><td>四位整数乘法</td>


<td>
测试精度约为99.949%
</td>

<td>
不依赖CoT、编程等任何辅助方式<br>
Transformer层数：7<br>

[训练数据集](./dataset_m4.py)
[测试代码](https://github.com/myhub/tr/releases/download/2.8.1/ChatCRNN_m4.zip)

</td>

</tr>
<tr><td>数数<br>
https://www.zhihu.com/question/632647147
</td>
<td>测试精度约为99.981%</td>
<td>
不依赖CoT、编程等任何辅助方式<br>
Transformer层数：7<br>

[训练数据集](./dataset_count.py)
[测试代码](https://github.com/myhub/tr/releases/download/2.8.1/ChatCRNN_count.zip)

</td>

</tr>
</table>

#### 实验总结
TransformerEncoder+CTCLoss组合已经在多行文本识别、图像识别、多位整数乘法、数数等不同任务上表现出了很强的适应性。<br>

在语音识别领域，TransformerEncoder+CTCLoss组合也有着广泛的应用：
https://huggingface.co/learn/audio-course/chapter3/ctc



