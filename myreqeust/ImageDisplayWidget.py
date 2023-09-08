import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QSlider, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageDisplayWidget(QWidget):
    def __init__(self, image_path,parent=None):
        super(ImageDisplayWidget, self).__init__(parent)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.set_image(image_path)
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setMinimum(1)
        self.scale_slider.setMaximum(10)
        self.scale_slider.setValue(5)
        self.scale_slider.setTickInterval(1)
        self.scale_slider.setTickPosition(QSlider.TicksBelow)
        self.scale_slider.valueChanged.connect(self.scale_image)
        # self.layout.addWidget(self.scale_slider)
        self.setLayout(self.layout)

    def scale_image(self, scale_value):
        scale_factor = scale_value / 5.0  # Convert scale value to a factor between 0.2 and 2.0
        self.scale_image2(scale_factor)

    def set_image(self, image_path):
        response = requests.get(image_path)
        if response.status_code == 200:
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

    def scale_image2(self, scale_factor):
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(self.image_label.pixmap().scaled(
            int(self.image_label.width() * scale_factor),
            int(self.image_label.height() * scale_factor),
            Qt.KeepAspectRatio
        ))
