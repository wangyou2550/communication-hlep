from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QFont, QBrush, QPainterPath, QColor, QPainter, QPixmap
from PyQt5.QtCore import Qt, QRectF

class WatermarkView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)
        self.setScene(QGraphicsScene(self))

        self.watermarkText = "Watermark"  # 水印文本
        self.watermarkFont = QFont("Arial", 40)  # 水印字体
        self.watermarkColor = QColor(200, 200, 200, 100)  # 水印颜色

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # 创建水印文本项
        watermarkItem = QGraphicsTextItem(self.watermarkText)
        watermarkItem.setFont(self.watermarkFont)
        watermarkItem.setDefaultTextColor(self.watermarkColor)
        watermarkItem.setOpacity(0.5)

        # 调整水印文本项的位置
        textWidth = watermarkItem.boundingRect().width()
        textHeight = watermarkItem.boundingRect().height()
        xPos = (self.width() - textWidth) / 2
        yPos = (self.height() - textHeight) / 2
        watermarkItem.setPos(xPos, yPos)

        # 在视图场景中添加水印文本项
        self.scene().addItem(watermarkItem)

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    view = WatermarkView(window)
    window.setCentralWidget(view)
    window.setGeometry(100, 100, 400, 300)
    window.show()
    app.exec_()