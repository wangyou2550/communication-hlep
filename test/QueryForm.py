import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QDateEdit


class QueryForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 水平布局，包含章节和名称输入框
        section_layout = QHBoxLayout()
        section_label = QLabel("章节:")
        self.section_combo = QComboBox()
        self.section_combo.addItem("")  # 默认章节为空
        self.section_combo.addItems(["章节1", "章节2", "章节3"])
        section_layout.addWidget(section_label)
        section_layout.addWidget(self.section_combo)
        layout.addLayout(section_layout)

        name_label = QLabel("题目名称:")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("请输入名称")
        section_layout.addWidget(name_label)
        section_layout.addWidget(self.name_edit)

        # 水平布局，包含开始时间和结束时间选择框
        time_layout = QHBoxLayout()
        start_label = QLabel("开始时间:")
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDate(QDate.currentDate().addMonths(-1))  # 设置为当前日期的前一个月
        time_layout.addWidget(start_label)
        time_layout.addWidget(self.start_date_edit)

        end_label = QLabel("结束时间:")
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QDate.currentDate())  # 设置为当前日期
        # 查询按钮
        self.query_button = QPushButton("查询")
        self.query_button.clicked.connect(self.executeQuery)

        time_layout.addWidget(end_label)
        time_layout.addWidget(self.end_date_edit)
        time_layout.addWidget(self.query_button)
        layout.addLayout(time_layout)


        # 设置布局
        self.setLayout(layout)

    def executeQuery(self):
        # 获取查询条件
        section = self.section_combo.currentText()
        name = self.name_edit.text()
        start_date = self.start_date_edit.date().toString("yyyy-MM-dd")
        end_date = self.end_date_edit.date().toString("yyyy-MM-dd")

        # 这里可以根据获取的查询条件执行相应的查询操作
        print("查询条件:")
        print("章节:", section)
        print("名称:", name)
        print("开始时间:", start_date)
        print("结束时间:", end_date)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 添加查询表单
        query_form = QueryForm()
        layout.addWidget(query_form)

        self.setLayout(layout)
        self.setWindowTitle("Query Form Example")
        self.setGeometry(100, 100, 400, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
