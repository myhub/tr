# coding: utf-8
from tr import *
from PIL import Image, ImageDraw, ImageFont


if __name__ == "__main__":
    img_path = "imgs/name_card.jpg"

    img_pil = Image.open(img_path)

    try:
        if hasattr(img_pil, '_getexif'):
            # from PIL import ExifTags
            # for orientation in ExifTags.TAGS.keys():
            #     if ExifTags.TAGS[orientation] == 'Orientation':
            #         break
            orientation = 274
            exif = dict(img_pil._getexif().items())
            if exif[orientation] == 3:
                img_pil = img_pil.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img_pil = img_pil.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img_pil = img_pil.rotate(90, expand=True)
    except:
        pass

    MAX_SIZE = 1600
    if img_pil.height > MAX_SIZE or img_pil.width > MAX_SIZE:
        scale = max(img_pil.height / MAX_SIZE, img_pil.width / MAX_SIZE)

        new_width = int(img_pil.width / scale + 0.5)
        new_height = int(img_pil.height / scale + 0.5)
        img_pil = img_pil.resize((new_width, new_height), Image.BICUBIC)

    print(img_path, img_pil.width, img_pil.height)

    color_pil = img_pil.convert("RGB")
    gray_pil = img_pil.convert("L")

    rect_arr = detect(gray_pil, FLAG_RECT)

    img_draw = ImageDraw.Draw(color_pil)
    colors = ['red', 'green', 'blue', "purple"]

    for i, rect in enumerate(rect_arr):
        x, y, w, h = rect
        for xy in [(x, y, x+w, y), (x+w, y, x+w, y+h), (x+w, y+h, x, y+h), (x, y+h, x, y)]:
            img_draw.line(xy=xy, fill=colors[i % len(colors)], width=2)

    color_pil.show()
    color_pil.save("~color_pil.png")

    blank_pil = Image.new("L", img_pil.size, 255)
    blank_draw = ImageDraw.Draw(blank_pil)

    results = run(gray_pil)
    for i, line in enumerate(results):
        x, y, w, h = line[0]
        txt = line[1]
        print(i, txt)
        font = ImageFont.truetype("msyh.ttf", max(int(h * 0.6), 14))
        blank_draw.text(xy=(x, y), text=txt, font=font)

    blank_pil.show()
    blank_pil.save("~blank_pil.png")

