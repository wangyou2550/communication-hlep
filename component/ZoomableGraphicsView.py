import sys

import requests
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent, QPixmap, QPainter, QTransform, QImage


class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, image_url,parent=None):
        scene=QGraphicsScene()
        super().__init__(scene, parent)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setMouseTracking(True)

        # 设置背景图像
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            # pixmap = QPixmap()
            # pixmap.loadFromData(image_data)
            # # pixmap_item = QGraphicsPixmapItem(pixmap)
            # # scene.addItem(pixmap_item)
            # # 创建QGraphicsPixmapItem并添加到场景中
            # pixmap_item = scene.addPixmap(pixmap)
            # self.setSceneRect(pixmap_item.boundingRect())
            image = QImage()
            image.loadFromData(image_data)

            # 创建QGraphicsPixmapItem并添加到场景中
            self.image_item = scene.addPixmap(self.convert_qimage_to_qpixmap(image))
            self.setSceneRect(self.image_item.boundingRect())
    def convert_qimage_to_qpixmap(self, qimage):
        # pixmap = QPixmap(qimage.width(), qimage.height(), QImage.Format_ARGB32)
        # painter = QPainter(pixmap)
        # painter.drawImage(0, 0, qimage)
        # painter.end()
        # return pixmap
        pixmap = QPixmap.fromImage(qimage)
        return pixmap
    def wheelEvent(self, event: QWheelEvent):
        zoom_in_factor = 1.2
        zoom_out_factor = 1 / zoom_in_factor

        # 获取滚轮滚动的角度
        angle = event.angleDelta().y()

        # 根据滚动角度缩放视图
        if angle > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor

        self.scale(zoom_factor, zoom_factor)


