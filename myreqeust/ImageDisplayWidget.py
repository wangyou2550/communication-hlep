import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QSlider, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QPainter, QFont, QColor
from PyQt5.QtCore import Qt

from config.GlobalConstant import GlobalConstant
from myreqeust.HttpTool import HttpTool


class ImageDisplayWidget(QWidget):


    def __init__(self, image_path,parent=None):
        super().__init__(parent)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        #关闭图片显示
        self.set_image(image_path)
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setMinimum(10)
        self.scale_slider.setMaximum(12)
        self.scale_slider.setValue(10)
        self.scale_slider.setTickInterval(1)
        self.scale_slider.setTickPosition(QSlider.TicksBelow)
        self.scale_slider.valueChanged.connect(self.scale_image)
        # layout.addWidget(self.scale_slider)
        self.setLayout(layout)

    def scale_image(self, scale_value):
        scale_factor = scale_value / 10.0  # Convert scale value to a factor between 1and 1.2
        self.scale_image2(scale_factor)
    # 渲染图片
    def set_image(self, image_path):
        response = requests.get(image_path)
        if response.status_code == 200:
            image_data = response.content
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(image_data)
            self.image_label.setPixmap(self.pixmap)
            self.add_watermark(HttpTool.user["userName"]+str(HttpTool.user["phonenumber"]))
            # self.image_label.setScaledContents(True)

    def add_watermark(self, text):
        painter = QPainter(self.pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置水印文字的字体和颜色
        font = QFont("Arial", 20)
        color = QColor(0, 0, 255)
        color.setAlphaF(0.2)  # 设置透明度
        painter.setFont(font)
        painter.setPen(color)

        # 计算水印文字的位置
        text_width = painter.fontMetrics().width(text)
        text_height = painter.fontMetrics().height()
        text_x = (self.pixmap.width() - text_width) // 2
        text_y = (self.pixmap.height() - text_height) // 2

        # 在图片上绘制水印文字
        if not GlobalConstant.IS_ADMIN:
            painter.drawText(text_x, text_y, text)
        painter.drawText(self.pixmap.width() - painter.fontMetrics().width("北邮考研"), text_height, "北邮考研")
        painter.drawText(self.pixmap.width() - painter.fontMetrics().width("Q:3792836192"), 2 * text_height,
                         "Q:3792836192")
        painter.drawText(self.pixmap.width() - painter.fontMetrics().width("25群:3792836192"), self.pixmap.height()-text_height,
                         "25群:781889541")
        painter.end()

        # 更新图片显示
        self.image_label.setPixmap(self.pixmap)
    def scale_image2(self, scale_factor):
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(self.image_label.pixmap().scaled(
            int(self.image_label.width() * scale_factor),
            int(self.image_label.height() * scale_factor),
            Qt.KeepAspectRatio
        ))


