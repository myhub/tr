# coding: utf-8
import tr
import os

_BASEDIR = os.path.dirname(os.path.abspath(__file__))

def test():
    os.chdir(_BASEDIR)
    print("recognize", tr.recognize("imgs/line.png"))
    txt = tr.run("imgs/line.png")[0][1]
    print(txt)
    

if __name__ == "__main__":
    test()
