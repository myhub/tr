import os, sys, random
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

char_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(26):
    char_table += chr(i + ord('a'))
char_table += [' ', '+', '-', '*', '/', "="]

net = ort.Ort(
    model_path=model_path,
    input_names=["INPUT__0"],
    output_names=["OUTPUT__0", "OUTPUT__1"],
)

SIZE = 48

for _ in range(5):
    a1 = random.randint(0, 999)
    a2 = random.randint(0, 999)
    print(f"a1 * a2 = {a1*a2}")
    ain = f"{str(a1)} * {str(a2)} = "
    ain = [char_table.index(_) + 1 for _ in ain]
    ain = [0]*(SIZE - len(ain)) + ain

    ain = np.asarray(ain, dtype=np.int32)[None, :]

    prob, inx = net.run([ain])
    print("-- ", end="")
    pre = None
    for e in inx[0]:
        e = int(e)
        if e != 0 and e != pre: 
            print(char_table[e-1], end="")
        pre = e
    print()

       