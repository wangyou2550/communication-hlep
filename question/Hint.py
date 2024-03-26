#题目提示
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog

from communication.StepSearchDialog import StepSearchDialog
from communication.StepShowDialog import StepShowDialog
from component.ButtonGroup import ButtonGroup
from component.CrudButtons import CrudButtons
from component.DifficlutLable import DifficultLables
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
from question.RelQuetionDialog import RelQuetionDialog
from question.RelationSectionStepDialog import RelationSectionStepDialog


class Hint(QWidget):
    add_dialog_signal = pyqtSignal(QDialog)
    add_question_signal=pyqtSignal(int,int)
    def __init__(self,question_id):
        super().__init__()
        # 题的序号
        self.question_id = question_id
        self.hint=HttpTool.get(PathConstant.QUERY_HINT+str(question_id))

        self.initUI()
    def initUI(self):
        # 垂直布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # 增删查改按钮
        self.create_crud_buttos()
        #增加标签
        # self.create_difficluty_label()
        # 增加type
        if self.hint:
            self.create_type_buttons(self.hint["relSections"])
            # 增加知识点清单列表
            self.create_khnowledge_buttons(self.hint["relSteps"])
            # 增加相似题目清单列表
            self.create_simulate_question_buttons(self.hint["relQuestions"])




    def create_difficluty_label(self):
        self.difficulty_label=DifficultLables(3,1)
        self.main_layout.addWidget(self.difficulty_label)


    def create_crud_buttos(self):
        # self.section_crud_buttons = CrudButtons('标签')
        self.step_crud_buttons = CrudButtons('知识点')
        self.question_crud_buttons = CrudButtons('相似题')
        # self.section_crud_buttons.button_add.clicked.connect(self.add_rel_section)
        self.step_crud_buttons.button_add.clicked.connect(self.add_rel_step)
        self.question_crud_buttons.button_add.clicked.connect(self.add_rel_question)
        # self.main_layout.addWidget(self.section_crud_buttons)
        self.main_layout.addWidget(self.step_crud_buttons)
        self.main_layout.addWidget(self.question_crud_buttons)

    def create_type_buttons(self,data):
        self.type_buttons=ButtonGroup('类型',data)
        self.type_buttons.button_click.connect(self.show_rel_section)
        self.main_layout.addWidget(self.type_buttons)

    def create_khnowledge_buttons(self,data):
        self.step_buttons=ButtonGroup('知识点',data)
        self.step_buttons.button_click.connect(self.show_rel_step)
        self.main_layout.addWidget(self.step_buttons)

    def create_simulate_question_buttons(self,data):
        self.question_buttons=ButtonGroup('相似题',data)
        self.question_buttons.button_click.connect(self.show_rel_question)
        self.main_layout.addWidget(self.question_buttons)

    # def add_rel_section(self):
    #     print(1)
    def add_rel_step(self):
        # dialog=RelationSectionStepDialog(self.question_id)
        dialog=StepSearchDialog(self.question_id,0)
        dialog.exec_()

    def add_rel_question(self):
        dialog=RelQuetionDialog(self.question_id)
        dialog.exec_()
    def show_rel_section(self,id):
        print(id)

    @pyqtSlot(str)
    def show_rel_step(self,id):
        dialog=StepShowDialog(id)
        dialog.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        self.add_dialog_signal.emit(dialog)

    @pyqtSlot(str)
    def show_rel_question(self,id):
        #获取题的章节，sort,新建一个Question,然后将添加到table
        for question in self.hint["relQuestions"]:
            if id==str(question["id"]):
                # rel_question=Question(question["chapter"],question["sort"]-1)
                self.add_question_signal.emit(question["chapter"],question["sort"]-1)

        print(id)

    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)

