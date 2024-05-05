from PyQt5.QtWidgets import QWidget, QVBoxLayout

from component.FeedbackFavoriteError import FFE_Widget
from component.ImageViewer import ImageViewer
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
from question.ChoiceButton import ChoiceButton


class SimpleQuestion(QWidget):
    def __init__(self,question):
        super().__init__()
        # 题的序号
        self.question = question

        self.initUI()
    def initUI(self):
        self.main_layout = QVBoxLayout()
        if self.question:
            # 创建反馈，收藏框
            self.ffe_widget=FFE_Widget(HttpTool.get(PathConstant.GET_PROBLEM_FEEDBACK_FAVORITE+str(self.question["id"])),self.question["id"])
            self.main_layout.addWidget(self.ffe_widget,10)
            # 创建单选题主题部分
            # self.question_widget = ImageDisplayWidget(self.question["imageSrc"])
            self.question_widget = ImageViewer(self.question["imageSrc"])
            self.main_layout.addWidget(self.question_widget,70)
            # 选项
            self.add_choice_radio_button()
        self.setLayout(self.main_layout)
    def add_choice_radio_button(self):
        if self.question["problemType"] == '0':
            self.createChoiceRadioButton(list(range(self.question["sort"], self.question["sort"] + self.question["choiceNum"])))


    def createChoiceRadioButton(self,serial_number_list):
        self.choice_button_list_widget=QWidget()
        self.choice_button_list_layout=QVBoxLayout()
        for serial_number in serial_number_list:
            self.choice_button_list_layout.addWidget(ChoiceButton(serial_number))
        self.choice_button_list_widget.setLayout(self.choice_button_list_layout)
        self.main_layout.addWidget(self.choice_button_list_widget)