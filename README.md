# tr - Text Recognition 
Tested under Python2/Python3 with *Ubuntu 16.04* and *Ubuntu 18.04*

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口

#### 说明
+ 添加python2支持
+ 去除python-opencv、Pillow依赖，降低部署难度

<br>
授权协议：<a href="https://github.com/myhub/tr/blob/master/LICENSE">GNU Affero General Public License v3.0</a>
<br><br>
如果喜欢本软件，打开支付宝扫一扫，您的赞助是我们开发的最大动力<br>
<a href="https://gitee.com/microic/tr/raw/master/zfb.png"><img alt="点击查看图片" width="256" src="https://gitee.com/microic/tr/raw/master/zfb.png" /></a>
<br>已有4人共赞助46元～


<!--
#### TODO
- [x] 检测带角度的文本框
- [x] 识别部分支持带角度的文本框
- [ ] 优化识别部分代码
- [ ] 支持表格检测
- [ ] 识别英文空格
- [ ] 支持GPU/手机端
-->

#### Requirements
<pre>pip install numpy
</pre>
#### Install
<pre>git clone https://github.com/myhub/tr.git
cd ./tr
python demo.py
</pre>


#### 关联项目
+ 若需要Web端调用，推荐参考<a href="https://github.com/alisen39/TrWebOCR">TrWebOCR</a>


#### How To Use?
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


#### 效果展示
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/id_card/1.png" />
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/id_card/2.png" />
<hr>
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/name_card/1.png" />
<img src="https://gitee.com/microic/tr/raw/master/imgs/output/name_card/2.png" />
