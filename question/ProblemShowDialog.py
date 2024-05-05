from PyQt5.QtCore import pyqtSignal, Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPushButton, QVBoxLayout, QStackedWidget, QTabWidget

from component.FeedbackFavoriteError import FFE_Widget
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
from question.SimpleQuestion import SimpleQuestion
from question.Solution import Solution


class ProblemShowDialog(QDialog):
    add_dialog_signal = pyqtSignal(QDialog)
    def __init__(self,problem_id):
        super().__init__()
        self.problem_id=problem_id
        self.problem=HttpTool.get(PathConstant.ADD_QUESTION+"/"+str(problem_id))
        self.title=self.problem["name"]
        self.setupUi()
        self.setWindowModality(Qt.ApplicationModal)

    def setupUi(self):
        self.vbox = QVBoxLayout(self)
        self.simpleQuestion=SimpleQuestion(self.problem)
        self.solution = Solution(self.problem_id)
        self.solution.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.closeTable)
        self.tab_widget.addTab(self.simpleQuestion,"题目")
        self.tab_widget.addTab(self.solution,"答案")
        self.vbox.addWidget(self.tab_widget)

        self.setLayout(self.vbox)
    # def showQuestion(self):
    #     self.vbox.itemAt(1).widget().deleteLater()
    #     self.vbox.addWidget(SimpleQuestion(self.problem),90)
    #
    # def showAnswer(self):
    #
    #     self.vbox.itemAt(1).widget().deleteLater()
    #     self.vbox.addWidget(Solution(self.problem_id),90)

    def closeTable(self,index):
        if index> 1:
            self.tab_widget.removeTab(index)
        else:
            pass

    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self,dialog):
        self.tab_widget.addTab(dialog,dialog.title)
        # 设置为当前页面
        self.tab_widget.setCurrentWidget(dialog)

