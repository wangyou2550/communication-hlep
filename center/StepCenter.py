from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog

from center.Pagination import Pagination
from center.QueryForm import QueryForm
from center.StepTableWidget import StepTableWidget


class StepCenter(QWidget):
    add_dialog_signal = pyqtSignal(QDialog)
    def __init__(self,type):
        super().__init__()
        self.type=type

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.query=QueryForm(self.type)
        self.table=StepTableWidget(self.type)
        self.table.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        self.query.querySignal.connect(self.table.handleQuerySignal)
        self.page=Pagination()
        self.page.pageSignal.connect(self.query.executeQuery)
        self.table.totalSignal.connect(self.page.updateTotal)
        layout.addWidget(self.query,20)
        layout.addWidget(self.table,70)
        layout.addWidget(self.page,10)
        self.setLayout(layout)
    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)