import sys
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QDialog

from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools
from question.Hint import Hint
from question.MultipleChoiceQuestion import MultipleChoiceQuestion
from question.Solution import Solution


class SidebarButton(QPushButton):

    def __init__(self, text):
        super().__init__(text)
        self.setFixedHeight(50)
        self.setStyleSheet('QPushButton { background-color: gray; }'
                           'QPushButton:hover { background-color: green; }')


class Question(QMainWindow):
    add_dialog_signal = pyqtSignal(QDialog)
    add_question_signal = pyqtSignal(int,int)
    def __init__(self,chapter_id,current_index=0):
        super().__init__()
        self.chapter_id=chapter_id
        data={}
        data["chapter"]=chapter_id
        self.questions = HttpTool.get(PathConstant.QUERY_QUESTION_LIST ,data)
        self.current_question_index=current_index

        # 设置主窗口的整体布局
        self.layout = QHBoxLayout()

        # 创建侧边栏部件
        sidebar = QWidget()
        sidebar.setFixedWidth(int(self.width() * 0.2))  # 设置侧边栏宽度为主窗口宽度的 20%
        sidebar.setStyleSheet('background-color: #F0F0F0;')

        # 创建侧边栏按钮
        button_titles = ['题目', '提示', '评论', '题解', '做题记录']
        button_functions = [self.show_title, self.show_hint, self.show_comments, self.show_solution, self.show_record]
        sidebar_layout = QVBoxLayout()

        for title, func in zip(button_titles, button_functions):
            button = SidebarButton(title)
            button.clicked.connect(func)
            sidebar_layout.addWidget(button)

        sidebar.setLayout(sidebar_layout)

        # 创建右侧显示区域
        self.content_area = QWidget()
        self.content_area.setStyleSheet('background-color: white;')

        # 设置主窗口布局
        self.layout.addWidget(sidebar)
        # self.layout.addWidget(QWidget())  # 占位部件，用于显示 widget2 或 widget3
        self.layout.addWidget(self.content_area)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)
        self.show()
        self.show_title()

    def show_title(self):
        if len(self.questions)==0:
            content_widget = MultipleChoiceQuestion(None,self.chapter_id,self.current_question_index)
            # 删除占位部件并添加新的部件
            self.layout.itemAt(1).widget().deleteLater()
            self.layout.addWidget(content_widget)

        else:
            content_widget = MultipleChoiceQuestion(self.questions,self.chapter_id,self.current_question_index)
            content_widget.set_problem_index.connect(self.set_current_problem_index)
            # 删除占位部件并添加新的部件
            self.layout.itemAt(1).widget().deleteLater()
            self.layout.addWidget(content_widget)

    def show_hint(self):
        if len(self.questions)!=0:
            content_widget=Hint(self.questions[self.current_question_index]["id"])
            content_widget.add_dialog_signal.connect(self.show_dialog_in_table_widget)
            content_widget.add_question_signal.connect(self.show_question_in_table_widget)
            # 删除占位部件并添加新的部件
            self.layout.itemAt(1).widget().deleteLater()
            self.layout.addWidget(content_widget)
    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)
    @pyqtSlot(int,int)
    def show_question_in_table_widget(self, chapterId,index):
        self.add_question_signal.emit(chapterId,index)
    def show_comments(self):
        self.show_content_widget('评论')

    def show_solution(self):
        if len(self.questions) != 0:
            content_widget = Solution(self.questions[self.current_question_index]["id"])
            # 删除占位部件并添加新的部件
            self.layout.itemAt(1).widget().deleteLater()
            self.layout.addWidget(content_widget)

    def show_record(self):
        self.show_content_widget('题解')

    def show_content_widget(self,text):
        content_widget = MultipleChoiceQuestion()
        # 删除占位部件并添加新的部件
        self.layout.itemAt(1).widget().deleteLater()
        self.layout.addWidget(content_widget)

    @pyqtSlot(int)
    def set_current_problem_index(self,current_index):
        self.current_question_index=current_index


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Question()
    window.setWindowTitle("Sidebar Demo")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())