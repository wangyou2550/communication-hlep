import sys

import requests
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent, QPixmap, QPainter, QTransform


class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setMouseTracking(True)

        # 设置背景图像
        image_url="http://39.105.200.100:30997/images/冲激函数的性质.png"
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap_item = QGraphicsPixmapItem(pixmap)
            scene.addItem(pixmap_item)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    scene = QGraphicsScene()
    view = ZoomableGraphicsView(scene)

    view.show()
    sys.exit(app.exec_())