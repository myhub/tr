# tr - Text Recognition 

## 开发中，暂时只完成单行文本识别

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口

#### 新版本说明
+ 采用类似Transformer层替代部分LSTM层，进一步加快模型收敛速度

#### Requirements
+ python3，需要安装numpy
+ 支持Linux系统，暂不支持macOS/Windows

#### Install
<pre>pip install tr==2.7.1 -i https://pypi.tuna.tsinghua.edu.cn/simple

<!--
模型下载：https://github.com/myhub/tr/releases/tag/2.6.1
说明：采用不同技术方案训练的模型精度速度有差异，可以按需下载，下载后替换crnn.bin文件即可
-->
</pre>

#### Test
<pre>
python3 test_crnn_simple.py     # 文本行识别  
python3 test_crnn_pyqt5.py      # 截图识别  
</pre>

#### Python Example
<pre>import tr
crnn = tr.CRNN()                                # 初始化文本行识别网络
chars, scores = crnn.run("imgs/line.png")       # 识别文本行
print("".join(chars))                           # 打印结果
</pre>


#### 关联项目
+ 若需要Web端调用，推荐参考<a href="https://github.com/alisen39/TrWebOCR">TrWebOCR</a>

