import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QSpacerItem, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Button List Example')
        self.setGeometry(100, 100, 200, 200)

        self.setup_ui()

    def setup_ui(self):
        # 创建主窗口的布局
        layout = QVBoxLayout()

        # 创建按钮列表
        button_list = []

        # 创建按钮，并将其添加到按钮列表中
        for i in range(5):
            button = QPushButton(f'Button {i+1}')
            button_list.append(button)
            layout.addWidget(button)

        # 创建占位符
        spacer_item = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_item)

        # 创建按钮收起按钮
        collapse_button = QPushButton('Collapse All')
        collapse_button.clicked.connect(lambda: self.collapse_buttons(button_list))
        layout.addWidget(collapse_button)

        # 设置主窗口的中心部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def collapse_buttons(self, button_list):
        for button in button_list:
            button.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())