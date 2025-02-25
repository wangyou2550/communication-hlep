from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QListWidget, QHBoxLayout, QPushButton, QStackedWidget, \
    QTextEdit, QWidget, QDesktopWidget, QMenu, QAction, QGridLayout, QFileDialog

from communication.FeedbackDialog import Feedback_Dialog
from communication.RelationStepDialog import RelationStepDialog
from communication.StepDialog2 import StepDialog
import requests

from communication.StepSearchDialog import StepSearchDialog
from component.ImageViewer import ImageViewer
from component.ZoomableGraphicsView import ZoomableGraphicsView
from config.GlobalConstant import GlobalConstant
from myqt.StepListWidget import StepListWidget
from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.HttpTool import HttpTool
from myreqeust.ImageDisplayWidget import ImageDisplayWidget
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools
from skill.QuestionImageWidget import QuestionImageWidget


# 展示题目的，左侧题目名称列表，右侧题目图片和解答图片
class SkillQuestionDialog(QDialog):
    add_dialog_signal = pyqtSignal(QDialog)
    def __init__(self, skill_id, parent=None):
        super().__init__(parent)
        self.skill_id=skill_id
        url = PathConstant.GET_SKILL_QUESTION_BY_ID.replace("{id}", str(self.skill_id))
        self.questions=HttpTool.get(url)
        self.initUI()
        self.resize_dialog()

    def resize_dialog(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.availableGeometry(self)
        target_width = int(screen_rect.width() )
        target_height = int(screen_rect.height() )
        self.setGeometry(screen_rect.x(), screen_rect.y(), target_width, target_height)
        # 获取屏幕的几何信息
        screen_geo = QDesktopWidget().screenGeometry()

        # 获取 QDialog 的几何信息
        dialog_geo = self.frameGeometry()

        # 将 QDialog 移动到屏幕的中心
        self.move(int((screen_geo.width() - dialog_geo.width()) / 2), int((screen_geo.height() - dialog_geo.height()) / 2))


    def initUI(self):
        self.setWindowTitle('题')

        vbox= QVBoxLayout()
        stepWidget=QWidget()
        self.hbox2 = QHBoxLayout(stepWidget)
        self.question_list_widget=self.createQuestionList()

        self.createImageStackWidget()
        self.hbox2.addWidget(self.question_list_widget,10)
        # self.hbox2.addWidget(self.image_stack_widget,80)
        self.hbox2.addWidget(self.image_widget,90)
        stepWidget.setLayout(self.hbox2)
        vbox.addWidget(stepWidget)
        self.setLayout(vbox)

    def createImageStackWidget(self):
        # self.image_stack_widget = QStackedWidget(self)
        self.image_widget = QStackedWidget(self)
        # 预加载第一张图片
        if self.questions:
            self.current_step_id =self.questions[0]["id"]
            self.image_widget = QuestionImageWidget(self.questions[0])


    def createQuestionList(self):
        question_list_widget = QListWidget()
        if self.questions:
            for question in self.questions:
                question_list_widget.addItem(StepListWidgetItem(question["name"],question["id"],''))
        question_list_widget.currentRowChanged.connect(self.image_display)
        return question_list_widget


    # 显示图片
    def image_display(self,i):
        self.hbox2.removeItem(self.hbox2.itemAt(1))
        self.image_widget.deleteLater()
        self.image_widget = QuestionImageWidget(self.questions[i])
        self.hbox2.insertWidget(1,self.image_widget,90)
