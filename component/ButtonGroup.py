from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QPushButton, QVBoxLayout, QWidget

from base.IdButton import IdButton


class ButtonGroup(QGroupBox):
    button_click = pyqtSignal(str)
    def __init__(self,text,data):
        super().__init__()
        self.text=text
        self.data=data
        self.initUI()

    def initUI(self):
        self.setTitle(self.text)
        self.grid_layout = QGridLayout()
        if self.data:
            self.populate_buttons(self.data)  # 填充按钮，这里示例创建了20个按钮


    def populate_buttons(self, data):
        num_buttons=len(data)
        num_columns = 2
        num_rows = (num_buttons + num_columns - 1) // num_columns

        for i in range(num_buttons):
            button = IdButton(data[i]["name"],data[i]["id"])
            button.setFixedSize(100, 30)
            button.clicked.connect(self.show_current_qustion)
            self.grid_layout.addWidget(button, i // num_columns, i % num_columns)
        self.setLayout(self.grid_layout)

    def show_current_qustion(self):
        button = self.sender()  # 获取发出信号的按钮对象
        self.button_click.emit(str(button.id))

