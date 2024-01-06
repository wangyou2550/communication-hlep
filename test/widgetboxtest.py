import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QLabel, QDockWidget, QScrollArea


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Widget Box Example')
        self.setGeometry(100, 100, 600, 400)

        self.setup_ui()

    def setup_ui(self):
        # 创建主窗口的布局
        main_layout = QVBoxLayout()

        # 创建左侧的 Widget Box
        widget_box = QDockWidget('Widget Box', self)
        widget_box.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)

        # 创建 Widget Box 内部的 QScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # 创建 QScrollArea 内部的 QListWidget
        list_widget = QListWidget()
        # scroll_area.setWidget(list_widget)

        # 添加元素到 QListWidget
        for i in range(20):
            item = QListWidgetItem(f'Item {i}')
            list_widget.addItem(item)

        # 将 QScrollArea 添加到 Widget Box
        # widget_box.setWidget(scroll_area)

        # 将 Widget Box 添加到主窗口的布局中
        self.addDockWidget(1, widget_box)

        # 创建右侧的部件
        widget_label = QLabel('Right Widget')

        # 设置右侧部件的布局
        main_layout.addWidget(widget_label)
        main_layout.addWidget(list_widget)

        # 创建主窗口的中心部件
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        scroll_area.setWidget(central_widget)

        # 设置主窗口的中心部件
        self.setCentralWidget(scroll_area)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())