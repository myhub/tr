# coding: utf-8
import tr
from pathlib import Path
import os
os.chdir(Path(__file__).parent)


import codecs, sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

if __name__ == '__main__':
    crnn = tr.CRNN()
    chars, scores = crnn.run("imgs/line.png")
    print("".join(chars)) 
    
    try:
        import cv2
        chars, scores = crnn.run(cv2.imread("imgs/line.png", 0))
        print("".join(chars)) 
    except:
        pass
   