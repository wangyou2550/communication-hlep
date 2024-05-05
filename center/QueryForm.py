import sys

from PyQt5.QtCore import QDate, pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QDateEdit

from config.GlobalConstant import GlobalConstant
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant


class QueryForm(QWidget):
    querySignal=pyqtSignal(dict)
    def __init__(self,type=1):
        super().__init__()
        self.type=type
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 水平布局，包含章节和名称输入框
        section_layout = QHBoxLayout()
        section_label = QLabel("章节:")
        self.section_combo = QComboBox()
        self.section_combo.addItem("")  # 默认章节为空
        if self.type==1 or self.type==2:
            self.section_combo.addItems(["章节1", "章节2", "章节3","章节4", "章节5", "章节6", "章节7","章节8", "章节9", "章节10","章节11"])

        section_layout.addWidget(section_label)
        section_layout.addWidget(self.section_combo)
        layout.addLayout(section_layout)

        name_label = QLabel("题目名称:")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("请输入名称")
        section_layout.addWidget(name_label)
        section_layout.addWidget(self.name_edit)

        # 水平布局，包含开始时间和结束时间选择框
        time_layout = QHBoxLayout()
        start_label = QLabel("开始时间:")
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDate(QDate.currentDate().addMonths(-1))  # 设置为当前日期的前一个月
        time_layout.addWidget(start_label)
        time_layout.addWidget(self.start_date_edit)

        end_label = QLabel("结束时间:")
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QDate.currentDate())  # 设置为当前日期
        # 查询按钮
        self.query_button = QPushButton("查询")
        self.query_button.clicked.connect(self.executeQuery2)

        time_layout.addWidget(end_label)
        time_layout.addWidget(self.end_date_edit)
        time_layout.addWidget(self.query_button)
        layout.addLayout(time_layout)


        # 设置布局
        self.setLayout(layout)

    def executeQuery2(self):
        self.executeQuery(1)
    @pyqtSlot(int)
    def executeQuery(self,pageNum):
        # 获取查询条件
        data={}
        if self.section_combo.currentIndex()!=0:
            data["chapterId"]= self.section_combo.currentIndex()
        data["name"] = self.name_edit.text()
        data["startTime"] = self.start_date_edit.date()
        data["endTime"] = self.end_date_edit.date()
        data["pageSize"] = GlobalConstant.PAGE_SIZE
        data["pageNum"] = pageNum

        # 这里可以根据获取的查询条件执行相应的查询操作
        if self.type==1:
            data["feedback"]=1
            res = HttpTool.get(PathConstant.QUERY_STEP_PAGE, data)
            self.querySignal.emit(res)
            # 查询知识点反馈
        if self.type==2:
            data["favorite"]=1
            res = HttpTool.get(PathConstant.QUERY_STEP_PAGE, data)
            self.querySignal.emit(res)
        if self.type==3:
            # 查询知识点反馈
            data["feedback"]=1
            res = HttpTool.get(PathConstant.QUERY_PROBLEM_PAGE, data)
            self.querySignal.emit(res)
        if self.type==4:
            data["favorite"] = 1
            res = HttpTool.get(PathConstant.QUERY_PROBLEM_PAGE, data)
            self.querySignal.emit(res)
        if self.type==5:
            data["exercise"] = 1
            res = HttpTool.get(PathConstant.QUERY_PROBLEM_PAGE, data)
            self.querySignal.emit(res)





class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 添加查询表单
        query_form = QueryForm()
        layout.addWidget(query_form)

        self.setLayout(layout)
        self.setWindowTitle("Query Form Example")
        self.setGeometry(100, 100, 400, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
