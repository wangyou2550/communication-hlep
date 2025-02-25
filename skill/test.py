import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView, QScrollArea, QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor


class KnowledgePointManager(QWidget):
    def __init__(self):
        super().__init__()
        self.knowledge_points = []  # 存储知识点数据
        self.isShow = True  # 控制新增和修改按钮显示
        self.initUI()
        self.mock_data()  # 生成模拟数据

    def initUI(self):
        self.setWindowTitle('知识点管理')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # 搜索区域
        search_layout = QHBoxLayout()
        search_label = QLabel('搜索:')
        search_label.setFont(QFont('Arial', 14))
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText('输入知识点名称搜索...')
        self.search_input.setStyleSheet(
            "background-color: #f0f0f0; border: 1px solid #d0d0d0; padding: 5px; font-size: 14px;")
        self.search_button = QPushButton('搜索', self)
        self.search_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 5px 10px; border: none; border-radius: 4px; font-size: 14px;")
        self.search_button.clicked.connect(self.search_knowledge_points)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # 新增和修改按钮
        button_layout = QHBoxLayout()
        self.add_button = QPushButton('新增', self)
        self.add_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 5px 10px; border: none; border-radius: 4px; font-size: 14px;")
        self.add_button.clicked.connect(self.add_knowledge_point)
        self.edit_button = QPushButton('修改', self)
        self.edit_button.setStyleSheet(
            "background-color: #2196F3; color: white; padding: 5px 10px; border: none; border-radius: 4px; font-size: 14px;")
        self.edit_button.clicked.connect(self.edit_knowledge_point)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.edit_button)

        # 控制新增和修改按钮的显示
        if self.isShow:
            layout.addLayout(button_layout)

        # 表格
        self.table = QTableWidget(self)
        self.table.setColumnCount(6)  # 修正为 6 列
        self.table.setHorizontalHeaderLabels(['ID', '名称', '出题类型数量', '真题数量', '习题数量', '操作'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setFont(QFont('Arial', 14))  # 设置表格字体大小

        # 设置表格样式
        self.table.setStyleSheet("QTableWidget {background-color: #f0f0f0; color: #333; font-size: 14px;}"
                                 "QTableWidget::item {padding: 5px;}"
                                 "QTableWidget::item:selected {background-color: #e0e0e0;}")

        # 设置操作列的宽度
        # self.table.setColumnWidth(5, 200)
        # 设置列宽
        default_column_width = 100  # 其他列的默认宽度
        self.table.setColumnWidth(0, default_column_width)  # ID 列
        self.table.setColumnWidth(1, default_column_width)  # 名称列
        self.table.setColumnWidth(2, default_column_width)  # 出题类型数量列
        self.table.setColumnWidth(3, default_column_width)  # 真题数量列
        self.table.setColumnWidth(4, default_column_width)  # 习题数量列
        self.table.setColumnWidth(5, default_column_width * 3)  # 操作列宽度为其他列的 3 倍

        # 添加滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table)

        layout.addLayout(search_layout)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

    def mock_data(self):
        # 生成模拟数据
        for i in range(1, 40):  # 生成 20 个知识点
            point = {
                'id': i,
                'name': f'知识点 {i}',
                'question_type_count': random.randint(1, 10),
                'real_question_count': random.randint(1, 10),
                'exercise_count': random.randint(1, 10)
            }
            self.knowledge_points.append(point)
        self.populate_table()  # 填充表格

    def search_knowledge_points(self):
        name = self.search_input.text()
        self.populate_table(name)

    def populate_table(self, search_name=''):
        self.table.setRowCount(0)  # 清空表格
        for point in self.knowledge_points:
            if search_name in point['name']:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(str(point['id'])))
                self.table.setItem(row_position, 1, QTableWidgetItem(point['name']))
                self.table.setItem(row_position, 2, QTableWidgetItem(str(point['question_type_count'])))
                self.table.setItem(row_position, 3, QTableWidgetItem(str(point['real_question_count'])))
                self.table.setItem(row_position, 4, QTableWidgetItem(str(point['exercise_count'])))
                # 设置行高
                self.table.setRowHeight(row_position, 50)
                # 添加操作按钮
                query_button = QPushButton('查询', self)
                query_button.setStyleSheet(
                    "background-color: #2196F3; color: white; padding: 5px 5px; border: none; border-radius: 10px; font-size: 14px;")
                edit_button = QPushButton('编辑', self)
                edit_button.setStyleSheet(
                    "background-color: #4CAF50; color: white; padding: 5px 5px; border: none; border-radius: 10px; font-size: 14px;")
                delete_button = QPushButton('删除', self)
                delete_button.setStyleSheet(
                    "background-color: #f44336; color: white; padding: 5px 5px; border: none; border-radius: 10px; font-size: 14px;")

                # 设置按钮的大小
                query_button.setFixedSize(60, 30)
                edit_button.setFixedSize(60, 30)
                delete_button.setFixedSize(60, 30)

                query_button.clicked.connect(lambda checked, id=point['id']: self.query_knowledge_point(id))
                edit_button.clicked.connect(lambda checked, id=point['id']: self.edit_knowledge_point(id))
                delete_button.clicked.connect(lambda checked, id=point['id']: self.delete_knowledge_point(id))

                # 将按钮添加到表格单元格
                button_layout = QHBoxLayout()
                button_layout.addWidget(query_button)
                button_layout.addWidget(edit_button)
                button_layout.addWidget(delete_button)

                # 创建一个 widget 来包含按钮
                button_widget = QWidget()
                button_widget.setLayout(button_layout)
                self.table.setCellWidget(row_position, 5, button_widget)

    def query_knowledge_point(self, id):
        QMessageBox.information(self, '查询知识点', f'查询知识点 ID: {id} 功能尚未实现')

    def add_knowledge_point(self):
        QMessageBox.information(self, '新增知识点', '新增知识点功能尚未实现')

    def edit_knowledge_point(self, id):
        QMessageBox.information(self, '编辑知识点', f'编辑知识点 ID: {id} 功能尚未实现')

    def delete_knowledge_point(self, id):
        self.knowledge_points = [kp for kp in self.knowledge_points if kp['id'] != id]
        self.populate_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KnowledgePointManager()
    ex.show()
    sys.exit(app.exec_())