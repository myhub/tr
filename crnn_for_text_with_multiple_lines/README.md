# 多行文本识别 CRNN For Text With Multiple Lines<br>

一句话：不再需要进行文本行位置的标注，真正的端到端OCR，大大降低标注和开发人员的工作量。
----
主流的OCR技术都会包含文本行检测+文本行识别两个环节，这套方案缺点包括：
+ 标注和模型开发工作量都很大
+ 文本行识别的精度会受到文本行检测精度的影响，整体误差会累积
+ 由于文本行识别模型一般会将文本行从原图中切割出来后进行识别，因此会丢失很多上下文信息从而影响精度

所以我想如果CRNN能够支持多行文本的识别，那么在一些场景下就不需要做文本行检测了。由于模型结构跟CRNN相比几乎没啥修改（仅仅添加了Transformer Encoder来提升模型对全局上下文的学习能力），损失函数也使用CTCLoss，训练代码跟CRNN也相同，所以还是属于CRNN。

#### 测试
<pre>
下载https://github.com/myhub/tr/releases/download/2.8.1/crnn_plus_v1_0.zip文件后解压

python test.py

运行环境：
Ubuntu18+
安装依赖：
pip install ort==1.0.5
</pre>




