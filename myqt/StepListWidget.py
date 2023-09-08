from PyQt5.QtWidgets import QListWidget

from communication.StepShowDialog import StepShowDialog
from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools


class StepListWidget(QListWidget):
    def __init__(self, steps):
        super().__init__()
        self.steps = steps
        self.addStepItem(steps)
        self.itemClicked.connect(self.step_clicked)

    def step_clicked(self,item):
        # 显示另外一个dialog
        dialog=StepShowDialog(item.id)
        dialog.exec_()

    def addStepItem(self,steps):
        self.clear()
        if steps:
            for step in steps:
                self.addItem(StepListWidgetItem(step["relationStepName"],step["relationStepId"],None))
