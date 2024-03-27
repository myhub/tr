import os, sys
try: import cv2 
except: pass
try: import PIL.Image 
except: pass
import numpy as np
from pathlib import Path

try:
    import ort
except:
    raise Exception("install ort first by pip install ort==1.2.1")

os.chdir(Path(__file__).parent)

model_path = "crnn_plus.bin"
assert Path(model_path).exists()

char_table = Path("char_table.txt").read_text()
net = ort.Ort(
    model_path=model_path,
    input_names=["INPUT__0"],
    output_names=["OUTPUT__0", "OUTPUT__1"],
)

SIZE = 384

test_dir = Path("./imgs/")

img_list = list(Path(test_dir).glob("*.png"))
img_list += list(Path(test_dir).glob("*.jpg"))
img_list.sort()

for img_path in img_list:
    print(img_path)
    try:
        img = cv2.imread(str(img_path), 0)
    except:
        img = PIL.Image.open(str(img_path)).convert("L")
        img = np.asarray(img, dtype=np.uint8)

    h, w = img.shape
    assert max(h, w) <= SIZE, f"the current version only support image size within {SIZE}px"
    pad_w = SIZE - w
    pad_h = SIZE - h
    img = np.pad(img, [(0, pad_h), (0, pad_w)], 
                'constant',
                constant_values = (128,))
    img = img[None, None, :, :] 
    img = np.asarray(img, dtype="float32") / 255

    prob, inx = net.run([img])

    print("-- ", end="")
    pre = None
    for e in inx[0]:
        e = int(e)
        if e != 0 and e != pre: 
            print(char_table[e-1], end="")
        pre = e
    print()
