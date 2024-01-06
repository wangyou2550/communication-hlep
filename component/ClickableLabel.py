from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import  QLabel
class ClickableLabel(QLabel):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        self.clicked.emit()

    clicked = pyqtSignal()