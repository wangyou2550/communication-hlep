import sys

from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, \
    QHeaderView, QScrollArea, QDialog

from communication.StepShowDialog import StepShowDialog
from config.GlobalConstant import GlobalConstant
from question.ProblemShowDialog import ProblemShowDialog


class StepTableWidget(QWidget):
    totalSignal = pyqtSignal(int)
    add_dialog_signal = pyqtSignal(QDialog)
    def __init__(self,type=1):
        super().__init__()
        self.type=type
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建表格
        self.tableWidget = QTableWidget()
          # 设置列数，包括查询按钮所在列
        if self.type==1 or self.type==2:
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(["ID", "名称", "评论", "查询"])  # 设置列标题
        else:
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(["ID", "名称", "评论","错误原因", "查询"])  # 设置列标题

        # 设置表格样式
        # self.tableWidget.setStyleSheet(
        #     "QTableWidget { border: 1px solid #ccc; border-collapse: collapse; }"
        #     "QTableWidget::item { padding: 10px; }"
        #     "QHeaderView::section { background-color: #f0f0f0; border: 1px solid #ccc; }"
        #     "QPushButton { background-color: #4CAF50; color: white; border: none; padding: 5px 10px; font-size: 12px; }"
        #     "QPushButton:hover { background-color: #45a049; }"
        # )

        # 设置表格列宽自动调整
        # 创建 QScrollArea
        scroll_area = QScrollArea()
        # 将 QTableWidget 添加到 QScrollArea 中
        scroll_area.setWidget(self.tableWidget)
        # 设置 QScrollArea 的调整策略，使其自动适应布局的宽度
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # self.tableWidget.setMinimumSize(int(layout.sizeHint().width()))

        # 隐藏第一列
        self.tableWidget.setColumnHidden(0, True)

        # 添加数据按钮
        # self.add_data_button = QPushButton("添加数据")
        # self.add_data_button.clicked.connect(self.addData)

        layout.addWidget(self.tableWidget)
        # layout.addWidget(self.add_data_button)

        self.setLayout(layout)

    def addData(self,data):
        # 模拟添加数据
        # data = [
        #     {"id": 1, "name": "Item 1", "value": 10},
        #     {"id": 2, "name": "Item 2", "value": 20},
        #     {"id": 3, "name": "Item 3", "value": 30}
        # ]

        # 清空表格
        self.tableWidget.setRowCount(0)

        # 将数据显示在表格中
        for row, item in enumerate(data):
            self.tableWidget.insertRow(row)


            if item['comment']:
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item['comment'])))

            # 创建查询按钮
            query_button = QPushButton("查询")
            query_button.clicked.connect(lambda _, row=row: self.queryData(row))
            if self.type<2:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item['id'])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(item['name']))
                self.tableWidget.setCellWidget(row, 3, query_button)
            else:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item['problemId'])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(item['problemName']))
                if item['exercise']:
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(str(item['exercise'])))
                self.tableWidget.setCellWidget(row, 4, query_button)

    def queryData(self, row):
        # 获取行号为 row 的第一列的 ID 值
        id_item = self.tableWidget.item(row, 0)
        if id_item:
            id_value = id_item.text()
            if self.type==1 or self.type==2:
                dialog = StepShowDialog(int(id_value))
                dialog.add_dialog_signal.connect(self.show_dialog_in_table_widget)
                self.add_dialog_signal.emit(dialog)
            if self.type>2:
                dialog = ProblemShowDialog(int(id_value))
                dialog.add_dialog_signal.connect(self.show_dialog_in_table_widget)
                self.add_dialog_signal.emit(dialog)


    @pyqtSlot(dict)
    def handleQuerySignal(self, data):
        self.addData(data["rows"])
        self.totalSignal.emit(self.divide_and_ceil(data["total"],GlobalConstant.PAGE_SIZE))

    def divide_and_ceil(self,a, b):
        quotient, remainder = divmod(a, b)
        if remainder > 0:
            quotient += 1
        return quotient

    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StepTableWidget()
    window.show()
    sys.exit(app.exec_())
