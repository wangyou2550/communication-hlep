import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView


class StepTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建表格
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)  # 设置列数，包括查询按钮所在列
        self.tableWidget.setHorizontalHeaderLabels(["ID", "名称", "评论", "查询"])  # 设置列标题

        # 设置表格样式
        # self.tableWidget.setStyleSheet(
        #     "QTableWidget { border: 1px solid #ccc; border-collapse: collapse; }"
        #     "QTableWidget::item { padding: 10px; }"
        #     "QHeaderView::section { background-color: #f0f0f0; border: 1px solid #ccc; }"
        #     "QPushButton { background-color: #4CAF50; color: white; border: none; padding: 5px 10px; font-size: 12px; }"
        #     "QPushButton:hover { background-color: #45a049; }"
        # )

        # 设置表格列宽自动调整
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 隐藏第一列
        self.tableWidget.setColumnHidden(0, True)

        # 添加数据按钮
        self.add_data_button = QPushButton("添加数据")
        self.add_data_button.clicked.connect(self.addData)

        layout.addWidget(self.tableWidget)
        layout.addWidget(self.add_data_button)

        self.setLayout(layout)

    def addData(self):
        # 模拟添加数据
        data = [
            {"id": 1, "name": "Item 1", "value": 10},
            {"id": 2, "name": "Item 2", "value": 20},
            {"id": 3, "name": "Item 3", "value": 30}
        ]

        # 清空表格
        self.tableWidget.setRowCount(0)

        # 将数据显示在表格中
        for row, item in enumerate(data):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item['id'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item['name']))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item['value'])))

            # 创建查询按钮
            query_button = QPushButton("查询")
            query_button.clicked.connect(lambda _, row=row: self.queryData(row))
            self.tableWidget.setCellWidget(row, 3, query_button)

    def queryData(self, row):
        # 获取行号为 row 的第一列的 ID 值
        id_item = self.tableWidget.item(row, 0)
        if id_item:
            id_value = id_item.text()
            print("查询到的 ID:", id_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StepTableWidget()
    window.show()
    sys.exit(app.exec_())
