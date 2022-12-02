import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pip.ui', self)
        self.fl = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.fl:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.fl = True
        self.repaint()

    def draw_circle(self, qp):
        size = random.randint(5, 600)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(random.randint(0, 800), random.randint(0, 600), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

