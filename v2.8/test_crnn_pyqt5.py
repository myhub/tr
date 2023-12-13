#!/usr/bin/env python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import numpy as np
import PIL.Image
import tr

class Main(QDialog):
    @staticmethod
    def QPixmapToArray(pixmap):
        size = pixmap.size()
        w = size.width()
        h = size.height()

        qimg = pixmap.toImage()
        b = qimg.bits()
        b.setsize(w*h*4)
        img = np.frombuffer(b, np.uint8).reshape((h, w, 4))

        img = PIL.Image.fromarray(img).convert("L")
        img = np.array(img)
        return img

    def __init__(self):
        super().__init__()

        # self.crnn = tr.CRNN(model_path="model_crnn.onnx")
        self.crnn = tr.CRNN()
        self.textEdit = QPlainTextEdit(self)
        
        font = QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.resize(640, 240)
        self.setWindowTitle("请使用飞书、微信等软件进行截图，只支持单行文本识别 v2.8")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        layout = QGridLayout(self)
        layout.addWidget(self.textEdit, 1, 0)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.task)
        self.timer.start(200)
    
    def task(self):
        clipboard = QApplication.clipboard()
        pixmap = clipboard.pixmap()
        if pixmap.width() * pixmap.height() <= 0: return

        img = self.QPixmapToArray(pixmap)
        chars, _ = self.crnn.run(img)
        txt = "".join(chars)

        clipboard.setText(txt)
        self.textEdit.appendPlainText(txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



