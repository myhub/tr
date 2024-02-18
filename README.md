# tr - Text Recognition 

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口

编译环境: *Ubuntu 16.04*

-----------------------------------------
#### 近期开发方向
+ 多行文本识别 CRNN For Text With Multiple Lines<br>
将CRNN与Transformer Encoder/Decoder相结合，从而使CRNN支持多行文本的识别，标注时不再需要标注文本行的边界框。适用于弯曲文本识别等场景。<br>
实验结果：在384*384大小的图片上，精度已经非常接近甚至超过先检测文本行再识别的两阶段方案，推理速度更快。<br>
抢鲜体验：[crnn_for_text_with_multiple_lines](https://github.com/myhub/tr/tree/master/crnn_for_text_with_multiple_lines)


+ OCR-free Document Understanding<br>
目前端到端文档理解（不需要先进行文本行检测、识别）虽然精度有待提升，不过我还是觉得很有前途的，可以一个模型实现文字、图表、公式等内容的提取。<br>
技术讨论：[discussions](https://github.com/myhub/tr/discussions/165)

-----------------------------------------
#### 新版本体验
https://github.com/myhub/tr/tree/master/v2.8
+ 采用当前流行的YOLO系列主干网络
+ 加入轻量级Transformer Encoder结构提升模型根据上下文纠错的能力
+ 降低对真实样本的依赖，训练集仅仅包含100多个真实样本

**Install 安装:**
<pre>
pip install tr==2.8.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
说明： 不同版本的精度有差异，新版本精度不一定更高
旧版本安装：
+ pip install tr==2.8.1

Windows 64位系统安装：
pip install tr==2.8.6 -i https://pypi.org/simple/
</pre>

**Example 代码示例:**
<pre>
import tr
crnn = tr.CRNN()                                # 初始化文本行识别网络
chars, scores = crnn.run("imgs/line.png")       # 识别文本行
print("".join(chars))                           # 打印结果
</pre>

**GUI 截图识别**
<pre>
# 需要安装PyQt5，PIL依赖
python -m tr.gui
</pre>
-----------------------------------------
<!--
#### v2.6版本体验
+ 采用当前流行的YOLO系列主干网络
<br>https://github.com/myhub/tr/tree/master/v2.6
-->

<!-- #### 新版本体验v2.7
+ 采用Attention层替代部分LSTM层，进一步加快模型收敛速度
+ 删除部分人工标注样本，仅保留200多个真实样本，进一步降低人工智能中的人工成分
+ 不使用任何语料库进行样本合成，不具备根据上下文推断不清晰字符的能力
<br>https://github.com/myhub/tr/tree/master/v2.7 -->

#### 更新说明
+ c++接口支持
+ 添加python2支持
+ 去除opencv-python、Pillow依赖，降低部署难度
+ 支持多线程
+ 支持GPU
+ 取消对Windows系统的支持

#### Requirements
+ python2/python3，需要安装numpy
+ 不支持Windows、CentOS 6、ARM

#### GPU版本安装说明
如果对速度有要求，推荐安装GPU版本<br>
要使用GPU版本，复制tr_gpu文件夹里面的文件到tr文件夹<br>
注意: 需要先安装CUDA 10.1以及cuDNN 7.6.5<br>
<br>
若不想安装CUDA/cuDNN，可以使用docker部署
<pre>docker pull mcr.microsoft.com/azureml/onnxruntime:v1.3.0-cuda10.1-cudnn7
sudo nvidia-docker run -v /path/to/tr:/path/to/tr --rm -it mcr.microsoft.com/azureml/onnxruntime:v1.3.0-cuda10.1-cudnn7
</pre>

#### Install
+ 安装方法一
<pre>git clone https://github.com/myhub/tr.git
cd ./tr
sudo python setup.py install
</pre>
+ 安装方法二
<pre>sudo pip install git+https://github.com/myhub/tr.git@master
</pre>

#### Test
<pre>
python2 demo.py               # python2兼容测试
python3 test.py               # 可视化测试
python3 test-multi-thread.py  # 多线程测试
python3 test_crnn_pyqt5.py    # 截图识别
</pre>

#### 关联项目
+ 若需要Web端调用，推荐参考<a href="https://github.com/alisen39/TrWebOCR">TrWebOCR</a>


#### Python Example
<pre>import tr

# detect text lines, return list of (cx, cy, width, height, angle)
print(tr.detect("imgs/web.png", tr.FLAG_RECT))

# detect text lines with angle, return list of (cx, cy, width, height, angle)
print(tr.detect("imgs/id_card.jpeg", tr.FLAG_ROTATED_RECT))

# recognize text line, return (text, confidence)
print(tr.recognize("imgs/line.png"))

# detect and recognize text lines with angle, return list of ((cx, cy, width, height, angle), text, confidence)
print(tr.run("imgs/id_card.jpeg"))
</pre>

#### C++ Example
<pre>tr_init(0, 0, "crnn.bin", NULL);

#define MAX_WIDTH		512
int unicode[MAX_WIDTH];
float prob[MAX_WIDTH]; 

auto ws = tr_recognize(0, (void *)"line.png", 0, 0, 0, unicode, prob, MAX_WIDTH);

tr_release(0);
</pre>

#### 效果展示
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/id_card/1.png" />
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/id_card/2.png" />
<hr>
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/name_card/1.png" />
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/name_card/2.png" />
