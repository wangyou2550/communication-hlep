from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QListWidget, QWidget, QStackedWidget, QVBoxLayout

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
        self.stepVo=HttpTool.get(PathConstant.GET_STEP+"/"+str(step_id))
        self.title=self.stepVo["step"]["name"]
        self.setupUi()
        self.setWindowModality(Qt.ApplicationModal)

    def setupUi(self):
        hbox = QHBoxLayout(self)
        # self.image_widget=ImageDisplayWidget(self.stepVo["step"]["imageSrc"])
        self.image_widget=ImageViewer(self.stepVo["step"]["imageSrc"])
        vbox=QVBoxLayout()
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