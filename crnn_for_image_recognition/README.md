# 让CRNN支持图像识别 CRNN For Image Recognition

如果我们把图像中的物体看成是一个个字符，那么图像识别任务不就是文字识别任务吗？

#### 使用说明
+ 由于PASCAL VOC数据集规模较小（约1.66万张图片），导致模型泛化能力不足
+ 目前只支持640像素以内的图片

#### 推理测试
<pre>
运行环境：
  Ubuntu18+
安装依赖：
  pip install ort==1.0.5

下载 https://github.com/myhub/tr/releases/download/2.8.1/crnn_for_image_recognition_v1_0.zip 文件后解压
执行 python test.py 即可
</pre>

#### 参考项目
+ https://github.com/myhub/tr/tree/master/crnn_for_text_with_multiple_lines

