import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Paged List Example")

        self.table = QTableWidget()
        self.populate_table(1)  # 初始化时显示第一页数据

        self.page_combo = QComboBox()
        self.page_combo.currentIndexChanged.connect(self.change_page)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.page_combo)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.populate_pages()  # 填充分页控件

    def populate_table(self, page):
        # 模拟数据填充，这里只是示例，您可以根据实际情况进行修改
        data = [f"Item {i}" for i in range(1 + (page - 1) * 10, page * 10 + 1)]
        self.table.setRowCount(len(data))
        for i, item in enumerate(data):
            table_item = QTableWidgetItem(item)
            self.table.setItem(i, 0, table_item)

    def populate_pages(self):
        total_pages = 5  # 总页数，这里只是示例，您可以根据实际情况进行修改
        self.page_combo.clear()
        self.page_combo.addItems([str(i) for i in range(1, total_pages + 1)])

    def change_page(self, index):
        page = self.page_combo.currentText()
        self.populate_table(int(page))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())