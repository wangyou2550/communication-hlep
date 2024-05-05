from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QComboBox

from communication.FeedbackDialog import Feedback_Dialog
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant


class FFE_Widget(QWidget):

    def __init__(self,data=None,problem_id=0):
        super().__init__()
        self.data=data
        self.problem_id=problem_id
        self.feedback_value = 0
        self.favorite_value = 0
        self.initUI()

    def initUI(self):
       self.create_feed_favorite_button()
    def create_feed_favorite_button(self):
        layout = QHBoxLayout()

        self.feedback_button = QPushButton()
        self.feedback_button.clicked.connect(self.feedbackClicked)
        layout.addWidget(self.feedback_button)

        self.favorite_button = QPushButton()
        self.favorite_button.clicked.connect(self.favoriteClicked)
        layout.addWidget(self.favorite_button)
        self.comboBox = QComboBox()
        self.comboBox.addItem("没做")
        self.comboBox.addItem("错误")
        self.comboBox.addItem("正确")
        self.comboBox.currentIndexChanged.connect(self.onComboBoxIndexChanged)
        layout.addWidget(self.comboBox)

        self.update_step_feedback_favorite(self.data)
        self.setLayout(layout)

    def updateButtons(self):
        if self.feedback_value == 0:
            self.feedback_button.setText('反馈')
            self.feedback_button.setStyleSheet("background-color: green;")
        else:
            self.feedback_button.setText('已反馈')
            self.feedback_button.setStyleSheet("background-color: red;")

        if self.favorite_value == 0:
            self.favorite_button.setText('收藏')
            self.favorite_button.setStyleSheet("background-color: green;")
        else:
            self.favorite_button.setText('已收藏')
            self.favorite_button.setStyleSheet("background-color: red;")

    def feedbackClicked(self):
        self.feedback_value = 1-self.feedback_value
        if self.data:
            self.data["problemId"] = self.problem_id
            self.data["feedback"] = self.feedback_value
        else:
            self.data["feedback"] = self.feedback_value

        # //取消反馈，直接点击就可以
        if self.feedback_value==0:
            HttpTool.post(PathConstant.ADD_PROBLEM_FEEDBACK_FAVORITE, self.data)
        else:
            feedDialog=Feedback_Dialog(self.data,2)
            feedDialog.exec_()
        self.updateButtons()

    # 标记题是否做了
    def onComboBoxIndexChanged(self, index):
        if self.data:
            self.data["problemId"] = self.problem_id
            self.data["exercise"] = index
        else:
            self.data["exercise"] = index

        # //取消反馈，直接点击就可以
        if index != 1:
            HttpTool.post(PathConstant.ADD_PROBLEM_FEEDBACK_FAVORITE, self.data)
        else:
            feedDialog = Feedback_Dialog(self.data, 3)
            feedDialog.exec_()

    def favoriteClicked(self):
        self.favorite_value = 1-self.favorite_value
        if self.data:
            self.data["problemId"] = self.problem_id
            self.data["favorite"] = self.favorite_value
        else:
            self.data["favorite"] = self.favorite_value
        HttpTool.post(PathConstant.ADD_PROBLEM_FEEDBACK_FAVORITE, self.data)
        self.updateButtons()

    def update_step_feedback_favorite(self,step):
        self.data=step
        if self.data:
            if step["feedback"]:
                self.feedback_value = step["feedback"]
            else:
                self.feedback_value =0
            if step["favorite"]:
                self.favorite_value = step["favorite"]
            else:
                self.favorite_value =0
            if step["exercise"]:
                self.comboBox.blockSignals(True)  # 禁用信号
                self.comboBox.setCurrentIndex(int(step["exercise"]))
                self.comboBox.blockSignals(False)  #啓動信号
            else:
                self.comboBox.setCurrentIndex(0)
        self.updateButtons()