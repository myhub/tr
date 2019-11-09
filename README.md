# tr - Text Recognition 
Tested under Python3 with *Ubuntu 16.04* and *Ubuntu 18.04*

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口

#### 说明
由于时间有限，暂停Windows版本的维护，将专心开发Linux版本<br>
当前版本为测试版，不适合在实际项目中使用

#### Requirements
<pre>pip install numpy Pillow opencv-python
</pre>
#### Install
+ 安装方法一
<pre>git clone https://github.com/myhub/tr.git
cd ./tr
sudo python setup.py install
</pre>
+ 安装方法二
<pre>pip install git+https://github.com/myhub/tr.git@master
</pre>
+ 测试是否安装成功
<pre>python test.py
python test_angle.py
</pre>

#### How To Use?
<pre>import tr

# detect text lines, return list of (x, y, width, height)
print(tr.detect("imgs/web.png"))

# detect text lines with angle, return list of (cx, cy, width, height, angle)
print(tr.detect("imgs/id_card.jpeg", tr.FLAG_ROTATED_RECT))

# recognize text line, return (text, confidence)
print(tr.recognize("imgs/line.png"))

# detect and recognize text lines, return list of ((x, y, width, height), text, confidence)
print(tr.run("imgs/name_card.jpg"))

# detect and recognize text lines with angle, return list of ((cx, cy, width, height, angle), text, confidence)
print(tr.run_angle("imgs/id_card.jpeg"))
</pre>

#### TODO
- [x] 检测带角度的文本框
- [x] 识别部分支持带角度的文本框
- [ ] 优化识别部分代码
- [ ] 支持表格检测
- [ ] 识别英文空格
- [ ] 支持GPU/手机端

#### 效果展示
<img src="imgs/output/id_card/1.png" />
<img src="imgs/output/id_card/2.png" />
<hr>
<img src="imgs/output/name_card/1.png" />
<img src="imgs/output/name_card/2.png" />