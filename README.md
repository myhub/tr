# tr - Offline OCR
Tested under *Ubuntu 16.04* and *Ubuntu 18.04*

一款针对扫描文档的离线文本识别SDK，核心代码全部采用C++开发，并提供Python接口
 
#### Install
<pre>git clone https://github.com/myhub/tr.git
cd ./tr
sudo python setup.py install

or pip install git+https://github.com/myhub/tr.git@master
</pre>

#### How To Use
<pre>
import tr

# detect text lines, return list of (x, y, w, h)
print(tr.detect("imgs/web.png"))

# recognize text line, return (text, confidence)
print(tr.recognize("imgs/line.png"))

# detect and recognize, return list of ((x, y, w, h), text, confidence)
print(tr.run("imgs/name_card.jpg"))
</pre>

#### Example
https://github.com/myhub/tr/blob/master/test.ipynb
