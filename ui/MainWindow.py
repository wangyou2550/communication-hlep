from PyQt5.QtWidgets import QMainWindow, QAction, QLabel

from communication.HomePage import Home_Page


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建工具栏
        toolbar = self.addToolBar("Toolbar")

        # 创建首页按钮并添加到工具栏
        home_action = QAction("首页", self)
        home_action.triggered.connect(self.showHomeWidget)
        toolbar.addAction(home_action)

        # 创建知识点按钮并添加到工具栏
        knowledge_action = QAction("知识点", self)
        knowledge_action.triggered.connect(self.showKnowledgeWidget)
        toolbar.addAction(knowledge_action)

        # 创建习题按钮并添加到工具栏
        exercises_action = QAction("习题", self)
        exercises_action.triggered.connect(self.showExercisesWidget)
        toolbar.addAction(exercises_action)

        # 创建真题按钮并添加到工具栏
        past_papers_action = QAction("真题", self)
        past_papers_action.triggered.connect(self.showPastPapersWidget)
        toolbar.addAction(past_papers_action)

        # 创建模拟卷按钮并添加到工具栏
        mock_exam_action = QAction("模拟卷", self)
        mock_exam_action.triggered.connect(self.showMockExamWidget)
        toolbar.addAction(mock_exam_action)

        # 创建技巧按钮并添加到工具栏
        tips_action = QAction("技巧", self)
        tips_action.triggered.connect(self.showTipsWidget)
        toolbar.addAction(tips_action)
        self.showHomeWidget()

        self.setWindowTitle("北邮通信原理")

    def showHomeWidget(self):
        # 创建一个初始的 widget
        self.widget = QLabel("欢迎使用主页面")
        self.setCentralWidget(self.widget)

    def showKnowledgeWidget(self):
        self.knowledge_wiget=Home_Page()
        self.setCentralWidget(self.knowledge_wiget)

    def showExercisesWidget(self):
        self.widget.setText("习题小部件")

    def showPastPapersWidget(self):
        self.widget.setText("真题小部件")

    def showMockExamWidget(self):
        self.widget.setText("模拟卷小部件")

    def showTipsWidget(self):
        self.widget.setText("技巧小部件")
