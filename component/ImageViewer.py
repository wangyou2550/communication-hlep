import math
import sys
import requests
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage, QPainter, QFont, QColor
from PyQt5.QtCore import Qt

from config.GlobalConstant import GlobalConstant
from myreqeust.HttpTool import HttpTool


class ImageViewer(QGraphicsView):
    def __init__(self, image_url,parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # 加载图片
        image_data = requests.get(image_url).content
        image = QImage()
        image.loadFromData(image_data)

        # 显示图片
        self.pixmap = QPixmap.fromImage(image)
        self.image_item = self.scene.addPixmap(self.pixmap)
        # 获取水印文字
        # self.add_watermark(HttpTool.user["userName"]+str(HttpTool.user["phonenumber"]))

        # 设置初始缩放因子
        self.scale_factor = 1.0


    def set_image(self, image_url):
        # 请求图片数据
        response = requests.get(image_url)
        image_data = response.content

        # 加载图片
        image = QImage()
        image.loadFromData(image_data)
        # 移除之前的 QPixmap
        # if self.pixmap is not None:
        #     self.scene.removeItem(self.image_item)
        # 创建新的 QPixmap
        self.pixmap = QPixmap.fromImage(image)
        self.image_item.setPixmap(self.pixmap)
        self.add_watermark(HttpTool.user["userName"]+str(HttpTool.user["phonenumber"]))

        # # 更新图片显示
        # if not self.pixmap.isNull():
        #     self.image_item = self.scene.addPixmap(self.pixmap)
        #     self.fitInView(self.image_item, Qt.AspectRatioMode.KeepAspectRatio)

    def add_watermark(self, text):
        painter = QPainter(self.pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置水印文字的字体和颜色
        font = QFont("Arial", 12)
        color = QColor(0, 0, 255)
        color.setAlphaF(0.2)  # 设置透明度
        painter.setFont(font)
        painter.setPen(color)

        # 计算水印文字的位置
        text_width = painter.fontMetrics().width(text)
        text_height = painter.fontMetrics().height()
        text_x = (self.pixmap.width() - text_width) // 2
        text_y = (self.pixmap.height() - text_height) // 2
        x_spacing = (self.pixmap.width() - text_width * math.sqrt(2)) / 3
        y_spacing = (self.pixmap.width() - text_width * math.sqrt(2)) / 3

        watermark_ratio = 0.5
        watermark_coords = self.calculateWatermarkCoords(self.pixmap.width(), self.pixmap.height(), watermark_ratio)

        # 在图片上绘制水印文字
        if not GlobalConstant.IS_ADMIN:
            for x, y in watermark_coords:
                painter.save()
                painter.translate(x, y)
                painter.rotate(45)
                painter.drawText(0, 0, text)
                painter.restore()
            # painter.end()
            # painter.drawText(text_x, text_y, text)
        font = QFont("Arial", 20)
        painter.drawText(self.pixmap.width() - painter.fontMetrics().width("北邮考研"), text_height, "北邮考研")
        painter.drawText(self.pixmap.width() - painter.fontMetrics().width("Q:3792836192"), 2 * text_height,
                         "Q:3792836192")
        painter.drawText(self.pixmap.width() - painter.fontMetrics().width("Q群:3792836192"), self.pixmap.height()-text_height,
                         "Q群:781889541")
        painter.end()

        # 更新图片显示
        self.image_item.setPixmap(self.pixmap)

    def calculateWatermarkCoords(self, image_width, image_height, watermark_ratio):
        """
        计算在图片上均匀分布12个水印的坐标,水印大小根据图片尺寸自动调整。

        参数:
            image_width (int): 图片的宽度,单位为像素。
            image_height (int): 图片的高度,单位为像素。
            watermark_ratio (float): 水印大小相对于图片尺寸的比例,取值范围为0到1。

        返回:
            list: 一个包含12个元组的列表,每个元组包含一个水印的(x, y)坐标。
        """
        watermark_coords = []

        # 计算水印的实际大小
        watermark_size = min(image_width, image_height) * watermark_ratio

        # 计算水印之间的间距
        x_spacing = (image_width - watermark_size * math.cos(math.radians(45))) / 3
        y_spacing = (image_height - watermark_size * math.sin(math.radians(45))) / 3

        # 计算12个水印的坐标
        for i in range(3):
            for j in range(4):
                x = j * x_spacing + watermark_size * math.cos(math.radians(45)) / 2
                y = i * y_spacing + watermark_size * math.sin(math.radians(45)) / 2
                watermark_coords.append((int(x), int(y)))

        return watermark_coords

    def wheelEvent(self, event):
        # 获取滚轮滚动的角度
        angle = event.angleDelta().y()

        # 根据滚动角度调整缩放因子
        if angle > 0:
            self.scale_factor *= 1.1
        else:
            self.scale_factor *= 0.9

        # 根据新的缩放因子重新计算图片大小
        new_width = int(self.pixmap.width() * self.scale_factor)
        new_height = int(self.pixmap.height() * self.scale_factor)
        scaled_pixmap = self.pixmap.scaled(new_width, new_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)

        # 更新图片显示
        self.image_item.setPixmap(scaled_pixmap)

        # 调用父类的方法处理滚轮事件
        super().wheelEvent(event)


