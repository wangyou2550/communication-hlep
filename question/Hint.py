#题目提示
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from component.ButtonGroup import ButtonGroup
from component.CrudButtons import CrudButtons
from component.DifficlutLable import DifficultLables


class Hint(QWidget):
    def __init__(self,serial_number):
        super().__init__()
        # 题的序号
        self.serial_number = serial_number

        self.initUI()
    def initUI(self):
        # 垂直布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # 增删查改按钮
        self.create_crud_buttos()
        #增加标签
        self.create_difficluty_label()
        # 增加type
        self.create_type_buttons()
        #增加知识点清单列表
        self.create_khnowledge_list()
        #增加相似题目清单列表
        self.create_simulate_question()


    def create_difficluty_label(self):
        self.difficulty_label=DifficultLables(3,1)
        self.main_layout.addWidget(self.difficulty_label)


    def create_crud_buttos(self):
        self.khnowledge_crud_buttons = CrudButtons()
        self.simulate_crud_buttons = CrudButtons()
        self.main_layout.addWidget(self.khnowledge_crud_buttons)
        self.main_layout.addWidget(self.simulate_crud_buttons)

    def create_type_buttons(self):
        self.type_buttons=ButtonGroup("题目类型",[])

