import tr

# detect text lines, return list of (x, y, w, h)
print(tr.detect("imgs/web.png"))

# recognize text line, return (text, confidence)
print(tr.recognize("imgs/line.png"))

# detect and recognize, return list of ((x, y, w, h), text, confidence)
print(tr.run("imgs/name_card.jpg"))