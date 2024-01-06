import sys
from PyQt5.QtWidgets import  QMainWindow, QHBoxLayout, QPushButton, QWidget, QLabel


class CrudButtons(QMainWindow):
    def __init__(self,text):
        self.text=text
        super().__init__()

        # 创建水平布局管理器
        layout = QHBoxLayout()

        # 创建按钮并添加到布局中
        # 创建标签
        label = QLabel(self.text, self)

        # 设置标签的样式
        label.setStyleSheet("background-color: blue; color: white;")
        self.button_add = QPushButton("增加")
        self.button_edit = QPushButton("编辑")
        self.button_query = QPushButton("查询")
        self.button_delete = QPushButton("删除")
        layout.addWidget(label)

        layout.addWidget(self.button_add)
        layout.addWidget(self.button_edit)
        layout.addWidget(self.button_query)
        layout.addWidget(self.button_delete)

        # 创建部件并设置布局
        widget = QWidget()
        widget.setLayout(layout)

        # 将部件设置为主窗口的中心部分
        self.setCentralWidget(widget)