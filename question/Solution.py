from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QScrollArea, QDialog

from communication.StepShowDialog import StepShowDialog
from component.CrudButtons import CrudButtons
from component.FeedbackFavoriteError import FFE_Widget
from component.ImageViewer import ImageViewer
from config.GlobalConstant import GlobalConstant
from myreqeust.HttpTool import HttpTool
from myreqeust.ImageDisplayWidget import ImageDisplayWidget
from myreqeust.PathConstant import PathConstant
from question.Hint import Hint
from question.SolutionDialog import SolutionDialog


class Solution(QMainWindow):
    add_dialog_signal = pyqtSignal(QDialog)
    def __init__(self,question_id):
        super().__init__()
        # 题的序号
        self.question_id = question_id
        self.solution=HttpTool.get(PathConstant.QUERY_SOLUTION+str(question_id))
        self.hint=Hint(question_id)
        self.hint.step_buttons.button_click.connect(self.show_rel_step)
        self.initUI()
    def initUI(self):
        # 垂直布局,提示占比30%，新增按钮，显示图片的label
        self.main_layout = QVBoxLayout()
        self.ffe_widget = FFE_Widget(
            HttpTool.get(PathConstant.GET_PROBLEM_FEEDBACK_FAVORITE + str(self.question_id)),self.question_id)
        self.main_layout.addWidget(self.ffe_widget, 10)

        self.main_layout.addWidget(self.hint,20)
        if GlobalConstant.IS_ADMIN:
            self.curdButtons=CrudButtons('答案')
            self.curdButtons.button_add.clicked.connect(self.add_solution)
            self.main_layout.addWidget(self.curdButtons, 10)
        # 创建答案显示部分
        if "imageSrc" in self.solution:
            self.solution_widget = ImageDisplayWidget(self.solution["imageSrc"])
            # self.solution_widget = ImageViewer(self.solution["imageSrc"])
            self.main_layout.addWidget(self.solution_widget)
        self.main_layout




        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        # 创建左侧的 Widget Box  QScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(central_widget)
        # 设置主窗口的中心部件
        self.setCentralWidget(scroll_area)

        # self.show()

    @pyqtSlot(str)
    def show_rel_step(self, id):
        dialog = StepShowDialog(id)
        dialog.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        self.add_dialog_signal.emit(dialog)
    def add_solution(self):
        dialog=SolutionDialog(self.question_id)
        dialog.exec_()

    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)