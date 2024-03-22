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
    raise Exception("install ort first by pip install ort==1.0.5")

os.chdir(Path(__file__).parent)

model_path = "crnn_plus.bin"
assert Path(model_path).exists()

voc_class_names="""
    aeroplane bicycle bird boat bottle
    bus car cat chair cow diningtable
    dog horse motorbike person pottedplant
    sheep sofa train tvmonitor
""".strip().split()

char_table = []

for class_name in voc_class_names:
    char_table.append(f"<{class_name}>")
    char_table.append(f"</{class_name}>")

net = ort.Ort(
    model_path=model_path,
    input_names=["INPUT__0"],
    output_names=["OUTPUT__0", "OUTPUT__1"],
)

SIZE = 640

test_dir = Path("./imgs/")

img_list = list(Path(test_dir).glob("*.png"))
img_list += list(Path(test_dir).glob("*.jpg"))
img_list.sort()

for img_path in img_list:
    print(img_path)
    try:
        img = cv2.imread(str(img_path), cv2.IMREAD_COLOR)
        img = img[:,:,::-1].transpose((2,0,1))
    except:
        img = PIL.Image.open(str(img_path)).convert("RGB")
        img = np.asarray(img, dtype=np.uint8)
        img = img.transpose((2,0,1))

    h, w = img.shape[-2:]
    assert max(h, w) <= SIZE, f"the current version only support image size within {SIZE}px"
    pad_w = SIZE - w
    pad_h = SIZE - h
    img = np.pad(img, [(0, 0), (0, pad_h), (0, pad_w)], 
                'constant',
                constant_values = (128,))
    img = img[None, :, :] 
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
