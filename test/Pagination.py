import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox


class Pagination(QWidget):
    def __init__(self, total_pages=1):
        super().__init__()

        self.total_pages = total_pages  # 总页数
        self.current_page = 1  # 当前页码

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        # 上一页按钮
        self.prev_button = QPushButton("上一页")
        self.prev_button.clicked.connect(self.prevPage)
        layout.addWidget(self.prev_button)

        # 页码标签
        self.page_label = QLabel(f"Page {self.current_page} / {self.total_pages}")  # 页码标签
        layout.addWidget(self.page_label)

        # 下一页按钮
        self.next_button = QPushButton("下一页")
        self.next_button.clicked.connect(self.nextPage)
        layout.addWidget(self.next_button)

        # 页数选择下拉菜单
        self.page_combo = QComboBox()
        self.page_combo.addItems([str(i) for i in range(1, self.total_pages + 1)])
        self.page_combo.setCurrentIndex(self.current_page - 1)
        self.page_combo.currentIndexChanged.connect(self.changePage)
        layout.addWidget(self.page_combo)

        # 设置布局
        self.setLayout(layout)

    def prevPage(self):
        """上一页按钮点击事件"""
        if self.current_page > 1:
            self.current_page -= 1
            self.updatePageLabel()
            self.page_combo.setCurrentIndex(self.current_page - 1)

    def nextPage(self):
        """下一页按钮点击事件"""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.updatePageLabel()
            self.page_combo.setCurrentIndex(self.current_page - 1)

    def changePage(self, index):
        """页数选择下拉菜单改变事件"""
        self.current_page = index + 1
        self.updatePageLabel()

    def updatePageLabel(self):
        """更新页码标签"""
        self.page_label.setText(f"Page {self.current_page} / {self.total_pages}")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 添加分页控件
        pagination = Pagination(total_pages=1000)
        layout.addWidget(pagination)

        self.setLayout(layout)
        self.setWindowTitle("Pagination Example")
        self.setGeometry(100, 100, 300, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
