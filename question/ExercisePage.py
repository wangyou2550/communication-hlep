from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QTreeWidget, QTabWidget, QWidget

from myqt.QTreeWidgetItem import QTreeWidgetItem
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools
from question.Question import Question


class ExercisePage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        # 创建siderbar,放章节
        self.menuData = RequestTools.get_method(PathConstant.GET_CHAPTER_LIST)
        hbox = QHBoxLayout(self)
        menu = self.creatMenu(self.menuData)
        hbox.addWidget(menu, 20)
        # 创建TableWidget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.closeTable)

        widget2 = QWidget(self)
        widget2.setStyleSheet("background-color: blue;")
        self.tab_widget.addTab(widget2, "首页")
        hbox.addWidget(self.tab_widget, 80)
        self.setLayout(hbox)
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Horizontal Layout with Automatic Resizing')
        self.show()
    def creatMenu(self, menuData):
        menu = QTreeWidget(self)
        # 添加树节点
        menu.headerItem().setText(0, "通信原理")
        # 树节点点击事件
        menu.itemClicked.connect(self.on_node_clicked)
        for chapter in menuData:
            chapter_item = QTreeWidgetItem(menu, chapter["name"], chapter["id"],0)
            # self.showSection(chapter["sections"],chapter_item)
            # self.recursive_node_traversal(chapter["sections"], chapter_item)
        return menu

        # 移除Tbalwwidget中的table
    def closeTable(self, index):
        if index > 0:
            self.tab_widget.removeTab(index)
        else:
             pass


        # 知识点点击事件
    def on_node_clicked(self, item, column):
        # 根据id获取知识点的内容
        print(item.id)
        question=Question(item.id)
        self.tab_widget.addTab(question,item.name)
        # 设置为当前页面
        self.tab_widget.setCurrentWidget(question)

