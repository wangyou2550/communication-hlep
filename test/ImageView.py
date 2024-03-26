import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage, QPainter, QFont, QColor
from PyQt5.QtCore import Qt, QBuffer, QIODevice
from PIL import Image, ImageDraw, ImageFont
import requests
from PyQt5.QtCore import QByteArray
import io
class ImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # 加载图片
        image_url = "http://39.105.200.100:30997/images/sinc函数.png"  # 替换为实际的图片URL
        image_data = requests.get(image_url).content
        image = QImage()
        image.loadFromData(image_data)

        # 显示图片
        self.pixmap = QPixmap.fromImage(image)
        self.image_item = self.scene.addPixmap(self.pixmap)
        self.add_watermark2("友哥微信：13547517519")

        # 设置初始缩放因子
        self.scale_factor = 1.0

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

    def add_watermark(self, text):
        # 获取图片的字节数据
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        self.pixmap.toImage().save(buffer, "PNG")

        # 使用PIL库加载图片
        pil_image = Image.open(io.BytesIO(byte_array.data()))

        # 创建水印文字的图像
        watermark_image = Image.new("RGBA", pil_image.size)
        draw = ImageDraw.Draw(watermark_image)
        font = ImageFont.truetype("arial.ttf", 50)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_position = ((pil_image.width - text_width) // 2, (pil_image.height - text_height) // 2)
        draw.text(text_position, text, font=font, fill=(0, 255, 255, 128))

        # 将水印图像叠加到原始图像上
        watermarked_image = Image.alpha_composite(pil_image.convert("RGBA"), watermark_image)

        # 将PIL Image转换为QPixmap
        qimage = QImage(watermarked_image.tobytes("raw", "RGBA"), watermarked_image.width, watermarked_image.height,
                        QImage.Format_RGBA8888)
        self.pixmap = QPixmap.fromImage(qimage)

        # 更新图片显示
        self.image_item.setPixmap(self.pixmap)

    def add_watermark2(self, text):
        painter = QPainter(self.pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置水印文字的字体和颜色
        font = QFont("Arial", 12)
        color = QColor(0, 0, 255)
        color.setAlphaF(0.1)  # 设置透明度
        painter.setFont(font)
        painter.setPen(color)

        # 计算水印文字的位置
        text_width = painter.fontMetrics().width(text)
        text_height = painter.fontMetrics().height()
        text_x = (self.pixmap.width() - text_width) // 2
        text_y = (self.pixmap.height() - text_height) // 2

        # 在图片上绘制水印文字
        painter.drawText(text_x, text_y, text)
        painter.drawText(self.pixmap.width() -painter.fontMetrics().width("北邮考研"), text_height, "北邮考研")
        painter.drawText(self.pixmap.width() -painter.fontMetrics().width("Q:1297503417"), 2*text_height, "Q:1297503417")

        painter.end()

        # 更新图片显示
        self.image_item.setPixmap(self.pixmap)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    viewer = ImageViewer()
    viewer.show()

    sys.exit(app.exec_())