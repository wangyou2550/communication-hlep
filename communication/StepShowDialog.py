from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QListWidget

from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.ImageDisplayWidget import ImageDisplayWidget
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools


class StepShowDialog(QDialog):
    def __init__(self,step_id):
        super().__init__()
        self.step_id=step_id
        self.stepVo=RequestTools.get_method(PathConstant.GET_STEP+"/"+str(step_id))
        self.setupUi()
        self.setWindowModality(Qt.ApplicationModal)

    def stepUi(self):
        hbox = QHBoxLayout(self)
        image_widget=ImageDisplayWidget(self.stepVo["step"]["imageSrc"])
        self.relation_step_list=QListWidget()
        self.relation_step_list.itemClicked.connect(self.step_clicked)
        self.addStepItem(self.stepVo["relationSteps"])
        hbox.addItem(image_widget,80)
        hbox.addItem(self.relation_step_list,20)
        self.setLayout(hbox)
        self.resize(800,800)

    def step_clicked(self,item):
        # 显示另外一个dialog
        dialog=StepShowDialog(item.id)
        dialog.exec_()

    def addStepItem(self,steps):
        self.relation_step_list.clear()
        if steps:
            for step in steps:
                self.addItem(StepListWidgetItem(step["relationStepId"],step["relationStepName"],None))