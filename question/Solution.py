from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QScrollArea

from component.CrudButtons import CrudButtons
from config.GlobalConstant import GlobalConstant
from myreqeust.HttpTool import HttpTool
from myreqeust.ImageDisplayWidget import ImageDisplayWidget
from myreqeust.PathConstant import PathConstant
from question.Hint import Hint
from question.SolutionDialog import SolutionDialog


class Solution(QMainWindow):
    def __init__(self,question_id):
        super().__init__()
        # 题的序号
        self.question_id = question_id
        self.solution=HttpTool.get(PathConstant.QUERY_SOLUTION+str(question_id))
        self.hint=Hint(question_id)
        self.initUI()
    def initUI(self):
        # 垂直布局,提示占比30%，新增按钮，显示图片的label
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.hint,30)
        if GlobalConstant.IS_ADMIN:
            self.curdButtons=CrudButtons('答案')
            self.curdButtons.button_add.clicked.connect(self.add_solution)
            self.main_layout.addWidget(self.curdButtons, 10)
        # 创建答案显示部分
        if "imageSrc" in self.solution:
            self.solution_widget = ImageDisplayWidget(self.solution["imageSrc"])
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

        self.show()
    def add_solution(self):
        dialog=SolutionDialog(self.question_id)
        dialog.exec_()