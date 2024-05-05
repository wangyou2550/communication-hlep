from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QListWidget, QWidget, QStackedWidget, QVBoxLayout, QPushButton

from communication.FeedbackDialog import Feedback_Dialog
from component.ImageViewer import ImageViewer
from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.HttpTool import HttpTool
from myreqeust.ImageDisplayWidget import ImageDisplayWidget
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools


class StepShowDialog(QDialog):
    add_dialog_signal = pyqtSignal(QDialog)
    def __init__(self,step_id):
        super().__init__()
        self.step_id=step_id
        self.feedback_value = 0
        self.favorite_value = 0
        self.stepVo=HttpTool.get(PathConstant.GET_STEP+"/"+str(step_id))
        self.title=self.stepVo["step"]["name"]
        self.setupUi()
        self.setWindowModality(Qt.ApplicationModal)

    def setupUi(self):
        hbox = QHBoxLayout(self)
        # self.image_widget=ImageDisplayWidget(self.stepVo["step"]["imageSrc"])
        self.image_widget=ImageViewer(self.stepVo["step"]["imageSrc"])
        vbox=QVBoxLayout()
        vbox.addLayout(self.create_feed_favorite_button(), 10)
        self.relation_step_list=QListWidget()
        self.relation_step_list.itemClicked.connect(self.step_clicked)
        self.related_step_list = QListWidget()
        self.related_step_list.itemClicked.connect(self.step_clicked)
        self.addStepItem(self.stepVo["relationSteps"])
        self.addRelatedStepItem(self.stepVo["relatedSteps"])
        vbox.addWidget(self.relation_step_list)
        vbox.addWidget(self.related_step_list)
        hbox.addWidget(self.image_widget,80)
        hbox.addLayout(vbox,20)
        # hbox.addWidget(self.relation_step_list,20)
        self.setLayout(hbox)
        self.resize(800,800)

    def update_step_feedback_favorite(self,step):
        if step["feedback"]:
            self.feedback_value = step["feedback"]
        else:
            self.feedback_value =0
        if step["favorite"]:
            self.favorite_value = step["favorite"]
        else:
            self.favorite_value =0
        self.updateButtons()
    def create_feed_favorite_button(self):
        layout = QHBoxLayout()

        self.feedback_button = QPushButton()
        self.feedback_button.clicked.connect(self.feedbackClicked)
        layout.addWidget(self.feedback_button)

        self.favorite_button = QPushButton()
        self.favorite_button.clicked.connect(self.favoriteClicked)
        layout.addWidget(self.favorite_button)
        self.update_step_feedback_favorite(self.stepVo["step"])

        # self.updateButtons()
        return layout
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
        data={}
        data["stepId"]=self.step_id
        data["feedback"]=self.feedback_value
        # //取消反馈，直接点击就可以
        if self.feedback_value==0:
            HttpTool.post(PathConstant.ADD_STEP_FEEDBACK_FAVORITE, data)
        else:
            feedDialog=Feedback_Dialog(data,1)
            feedDialog.exec_()
        self.updateButtons()

    def favoriteClicked(self):
        self.favorite_value = 1-self.favorite_value
        data={}
        data["stepId"]=self.step_id
        data["favorite"]=self.favorite_value
        HttpTool.post(PathConstant.ADD_STEP_FEEDBACK_FAVORITE, data)
        self.updateButtons()
    def step_clicked(self,item):
        # 显示另外一个dialog
        dialog=StepShowDialog(item.id)
        dialog.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        self.add_dialog_signal.emit(dialog)
        # dialog.exec_()

    def addStepItem(self,steps):
        self.relation_step_list.clear()
        if steps:
            for step in steps:
                self.relation_step_list.addItem(StepListWidgetItem(step["relationStepName"],step["relationStepId"],None))
    def addRelatedStepItem(self,steps):
        self.related_step_list.clear()
        if steps:
            for step in steps:
                self.related_step_list.addItem(StepListWidgetItem(step["name"],step["id"],None))

    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)