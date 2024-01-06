import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QGridLayout, QPushButton, QVBoxLayout, QWidget

class QuestionButtonGroup(QGroupBox):
    problem_button_click = pyqtSignal(int)
    def __init__(self,number):
        super().__init__()
        self.number=number
        self.initUI()

    def initUI(self):
        self.setTitle("选择题")
        self.grid_layout = QGridLayout()
        self.populate_buttons(self.number)  # 填充按钮，这里示例创建了20个按钮


    def populate_buttons(self, num_buttons):
        num_columns = 10
        num_rows = (num_buttons + num_columns - 1) // num_columns

        for i in range(num_buttons):
            button = QPushButton(f"{i+1}")
            button.setFixedSize(100, 30)
            button.clicked.connect(self.show_current_qustion)
            self.grid_layout.addWidget(button, i // num_columns, i % num_columns)

        self.setLayout(self.grid_layout)

    # 点击按钮，发送题号切换信号
    def show_current_qustion(self):
        button = self.sender()  # 获取发出信号的按钮对象
        button_text = button.text()
        self.problem_button_click.emit(int(button_text))
        print(f"Button clicked: {button_text}")
