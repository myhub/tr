# tr - Text Recognition 

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口

编译环境: *Ubuntu 16.04*

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
