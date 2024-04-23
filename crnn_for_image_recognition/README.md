# 让CRNN支持图像识别 CRNN For Image Recognition

一句话：如果我们把图像中的物体看成是一个个字符，那么图像识别任务不就是文字识别任务吗？<br>

模型工程师往往需要处理各种各样的任务，通常不同的任务需要用到不同的模型，对企业而言模型越多意味着越高的研发成本。因此当我发现CRNN+Transformer能够很好地识别多行文本时，我就在想同样的模型能否处理更多的任务？我首先想到的是目标检测，不过我很快发现CTCLoss不太适合回归类任务，于是我就将目标瞄准了图像识别任务。

#### 使用说明
+ 由于PASCAL VOC数据集规模较小（约1.66万张图片），导致模型泛化能力不足
+ 目前只支持640像素以内的图片

<!-- #### 推理测试
<pre>
运行环境：
  Ubuntu18+
安装依赖：
  pip install ort==1.2.1

下载 https://github.com/myhub/tr/releases/download/2.8.1/crnn_for_image_recognition_v1_0.zip 文件后解压
执行 python test.py 即可
</pre> -->

#### 参考项目
+ https://github.com/myhub/tr/tree/master/crnn_for_text_with_multiple_lines

