# tr - Text Recognition 

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口

编译环境: *Ubuntu 16.04*

#### 为什么开发tr？
我刚开发tr时，网上只有[chineseocr](https://github.com/chineseocr/chineseocr)、 [tesseract](https://github.com/tesseract-ocr/tesseract)等少数开源OCR。tr发布后，又诞生了几款优秀的开源OCR。tr也基本上完成了自己的使命，会转为一个研究型项目，追求技术的先进性而不是实用性。

#### 暂停维护说明
在研究OCR的过程中，我发现了更有趣的Transformer技术，这是一种有希望单个算法解决绝大部分深度学习任务（包括OCR）的技术。未来的算法工程师可能不再需要学习各种各样的算法，只需要学习一款算法即可。后续我们将暂停维护本项目，重点研究Transformer技术

#### 免责声明
最近看到一些半开源/闭源免费软件被用户投诉举报，甚至追究法律责任的案例，感觉有必要加入免责声明：
+ 本软件存在风险，包括但不限于闪退、内存泄漏，所有风险由用户承担
+ 若在软件使用过程中出现异常导致损失，用户承担全部责任

#### 更新说明
+ c++接口支持
+ 添加python2支持
+ 去除opencv-python、Pillow依赖，降低部署难度
+ 支持多线程
<!-- + 支持GPU -->
<!-- + 取消对Windows系统的支持 -->

#### Requirements
+ python2/python3，需要安装numpy
+ 不支持Windows、CentOS 6、ARM

#### GPU版本安装说明
**由于新型号的显卡需要更高版本的CUDA，GPU版本暂时只支持旧型号的显卡。**<br>
如果对速度有要求，推荐安装GPU版本<br>
要使用GPU版本，复制tr_gpu文件夹里面的文件到tr文件夹<br>
注意: 需要先安装CUDA 10.1以及cuDNN 7.6.5。<br>
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
