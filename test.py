# coding: utf-8
import tr
import sys, cv2, time, os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

_BASEDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(_BASEDIR)

def test():
    print("recognize", tr.recognize("imgs/line.png"))
    img_path = "imgs/id_card.jpeg"
    # img_path = "imgs/name_card.jpg"

    img_pil = Image.open(img_path)

    print(img_pil.size)
    color_pil = img_pil.convert("RGB")
    gray_pil = img_pil.convert("L")

    img_draw = ImageDraw.Draw(color_pil)
    colors = ['red', 'green', 'blue', "purple"]

    t = time.time()
    n = 1
    for _ in range(n):
        tr.detect(gray_pil, flag=tr.FLAG_RECT)
    print("time", (time.time() - t) / n)

    results = tr.run(gray_pil, flag=tr.FLAG_ROTATED_RECT)

    for i, rect in enumerate(results):
        cx, cy, w, h, a = tuple(rect[0])
        print(i, "\t", rect[1], rect[2])
        box = cv2.boxPoints(((cx, cy), (w, h), a))
        box = np.int0(np.round(box))

        for p1, p2 in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            img_draw.line(xy=(box[p1][0], box[p1][1], box[p2][0], box[p2][1]), fill=colors[i % len(colors)], width=2)

    color_pil.show()


if __name__ == "__main__":
    test()
