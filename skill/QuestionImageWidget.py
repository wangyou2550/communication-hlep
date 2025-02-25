import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QScrollBar

from component.ImageViewer import ImageViewer


class QuestionImageWidget(QWidget):
    def __init__(self,question):
        super().__init__()
        self.question=question

        # 创建一个垂直布局
        layout = QVBoxLayout(self)

        # 创建一个QScrollArea
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  # 使得内容自动调整大小
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 始终显示垂直滚动条

        # 创建一个包含两个子QWidget的容器
        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)

        # 创建第一个子QWidget
        widget1 = ImageViewer(self.question["questionImageSrc"])
        # widget1 = QLabel("This is Widget 1\n" * 20)  # 高度很高的QWidget
        container_layout.addWidget(widget1)

        # 创建第二个子QWidget
        # widget2 = QLabel("This is Widget 2\n" * 20)  # 高度很高的QWidget
        widget2 = ImageViewer(self.question["solutionImageSrc"])
        container_layout.addWidget(widget2)

        # 将容器设置为滚动区域的内容
        scroll_area.setWidget(container_widget)

        # 将滚动区域添加到主布局
        layout.addWidget(scroll_area)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuestionImageWidget(1)
    window.resize(400, 300)  # 设置窗口大小
    window.setWindowTitle("Scrollable QWidget Example")
    window.show()
    sys.exit(app.exec_())