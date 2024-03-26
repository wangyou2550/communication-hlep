from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QListWidget, QDialog

from communication.StepShowDialog import StepShowDialog
from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools


class StepListWidget(QListWidget):
    add_dialog_signal=pyqtSignal(QDialog)
    def __init__(self, steps):
        super().__init__()
        self.steps = steps
        self.addStepItem(steps)
        self.itemClicked.connect(self.step_clicked)

    def step_clicked(self,item):
        # 显示另外一个dialog
        dialog=StepShowDialog(item.id)
        dialog.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        self.add_dialog_signal.emit(dialog)
        # dialog.exec_()

    def addStepItem(self,steps):
        self.clear()
        if steps:
            for step in steps:
                self.addItem(StepListWidgetItem(step["relationStepName"],step["relationStepId"],None))

    def addRelatedStepItem(self, steps):
        self.clear()
        if steps:
            for step in steps:
                self.addItem(StepListWidgetItem(step["name"], step["id"], None))
    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)