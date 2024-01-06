import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QSpacerItem, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建垂直布局管理器
        layout = QVBoxLayout()

        # 添加部件到布局
        layout.addWidget(QPushButton("Button 1"))


        # 创建垂直空间
        spacer = QSpacerItem(20, 10)  # 第一个参数是宽度，第二个参数是高度

        # 添加垂直空间到布局
        layout.addItem(spacer)
        layout.addWidget(QPushButton("Button 2"))

        # 创建部件并设置布局
        widget = QWidget()
        widget.setLayout(layout)

        # 将部件设置为主窗口的中心部分
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())