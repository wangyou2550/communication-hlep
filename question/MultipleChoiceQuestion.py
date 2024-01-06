import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QLabel, \
    QDockWidget, QScrollArea, QPushButton, QHBoxLayout

from component.CrudButtons import CrudButtons
from myreqeust.ImageDisplayWidget import ImageDisplayWidget
from question.ChoiceButton import ChoiceButton
from question.Problem import Problem
from question.QuestionButtonGroup import QuestionButtonGroup


class MultipleChoiceQuestion(QMainWindow):
    set_problem_index = pyqtSignal(int)
    def __init__(self,questions,chapter_id,current_index):
        super().__init__()
        self.questions=questions
        if self.questions:
            self.question=questions[current_index]
        self.chapter_id=chapter_id
        self.current_index=current_index
        # 题的序号列表
        # 题的答案
        # 题的做题记录
        # 题的解析
        # 题的关联知识点
        # 类似题推荐
        self.initUI()
    def initUI(self):
        # 创建主窗口的布局
        self.main_layout = QVBoxLayout()
        #创建题目的增删查改
        self.question_crud_buttons = CrudButtons('题目')
        self.question_crud_buttons.button_add.clicked.connect(self.add_question)
        self.main_layout.addWidget(self.question_crud_buttons)
        if self.questions:
            # 创建单选题主题部分
            self.question_widget = ImageDisplayWidget(self.question["imageSrc"])
            self.main_layout.addWidget(self.question_widget)
            # 选项
            self.add_choice_radio_button()

            #创建上一步，下一步按钮
            self.create_up_next_button()

            #创建题号box
            self.qustionGroupBox=QuestionButtonGroup(self.calculate_question_count())
            self.qustionGroupBox.problem_button_click.connect(self.jump_to_question)
            self.main_layout.addWidget(self.qustionGroupBox)

        # 创建主窗口的中心部件
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)


        # 创建左侧的 Widget Box  QScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(central_widget)
        # 设置主窗口的中心部件
        self.setCentralWidget(scroll_area)

        self.show()

    def jump_to_question(self,question_number):
        if question_number <= 0 or question_number > self.calculate_question_count():
            print("题号无效，请输入有效的题号范围：1-10")
        else:
            index=self.calculate_question_number(question_number)
            if self.current_index==index:
                return
            else:
                self.current_index=index
            self.set_problem_index.emit(self.current_index)
            self.question=self.questions[self.current_index]
            #更新主题部分
            self.question_widget.set_image(self.question["imageSrc"])
            #更新选项
            self.update_choice_radio_button()

    #计算题目的序号
    def calculate_question_number(self,question_number):
        # 使用 enumerate() 遍历列表并获取元素索引
        for index, item in enumerate(self.questions):
            if item["sort"]<=question_number and question_number<(item["sort"]+item["choiceNum"]):
                return index


    # 计算题的数量
    def calculate_question_count(self):
        count=0
        if self.questions:
            for question in self.questions:
                count+=question["choiceNum"]
        return count
    def add_choice_radio_button(self):
        if self.question["problemType"] == '0':
            self.createChoiceRadioButton(list(range(self.question["sort"], self.question["sort"] + self.question["choiceNum"])))

# 创建前后一题按钮
    def create_up_next_button(self):
        # 创建上一题按钮
        prev_button = QPushButton("上一题", self)
        prev_button.clicked.connect(self.previous_question)
        # 创建下一题按钮
        next_button = QPushButton("下一题", self)
        next_button.clicked.connect(self.next_question)
        self.prev_next_layout=QHBoxLayout()
        self.prev_next_layout.addWidget(prev_button)
        self.prev_next_layout.addWidget(next_button)
        # 创建一个容纳布局的小部件
        self.prev_next_widget = QWidget()
        self.prev_next_widget.setLayout(self.prev_next_layout)
        self.main_layout.addWidget(self.prev_next_widget)
# 创建题号
    def createChoiceRadioButton(self,serial_number_list):
        self.choice_button_list_widget=QWidget()
        self.choice_button_list_layout=QVBoxLayout()
        for serial_number in serial_number_list:
            self.choice_button_list_layout.addWidget(ChoiceButton(serial_number))
        self.choice_button_list_widget.setLayout(self.choice_button_list_layout)
        self.main_layout.addWidget(self.choice_button_list_widget)
    # 更换题的索引，重新渲染题的内容
    def previous_question(self):
        if self.current_index!=0:
            self.current_index=self.current_index-1
            self.set_problem_index.emit(self.current_index)
            self.question=self.questions[self.current_index]
            #更新主题部分
            self.question_widget.set_image(self.question["imageSrc"])
            #更新选项
            self.update_choice_radio_button()


        # 更新选项
    def update_choice_radio_button(self):
        if self.question["problemType"] != "0":
            self.remove_all_widget(self.choice_button_list_layout)
        else:
            # 移除组件
            self.remove_all_widget(self.choice_button_list_layout)
            # 重新渲染
            for serial_number in list(range(self.question["sort"], self.question["sort"] + self.question["choiceNum"])):
                self.choice_button_list_layout.addWidget(ChoiceButton(serial_number))


    def remove_all_widget(self,layout):
        # 移除布局中的所有小部件
        while layout.count():
            widget = layout.takeAt(0).widget()
            layout.removeWidget(widget)
            widget.deleteLater()

    # "点击了下一题按钮"
    def next_question(self):
        if self.question and self.current_index!=(len(self.questions)-1):
            self.current_index=self.current_index+1
            self.set_problem_index.emit(self.current_index)
            self.question=self.questions[self.current_index]
            #更新主题部分
            self.question_widget.set_image(self.question["imageSrc"])
            #更新选项
            self.update_choice_radio_button()

    def add_question(self):
        problem_dialog=Problem(self.chapter_id)
        problem_dialog.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultipleChoiceQuestion(None)
    sys.exit(app.exec_())


