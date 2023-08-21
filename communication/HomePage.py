from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QTreeWidget, QTabWidget
from PyQt5.uic.properties import QtWidgets
from myqt.QTreeWidgetItem import QTreeWidgetItem

from utils.JSONUtil import JSONUtil
from communication.Section import Section



class Home_Page(QWidget):
    def __init__(self):
        super().__init__()
        self.menuData = JSONUtil.readJsonFile('communication/KnowledgeNode.json')
        self.initUI()

    # 递归遍历知识点
    def recursive_node_traversal(self, data, item):
        if data:
            for node in data:
                node_item = QTreeWidgetItem(item, node["sort"] + node["name"], node["id"],node["pid"])
                self.recursive_node_traversal(node["child"], node_item)

    # 知识点点击事件
    def on_node_clicked(self, item, column):
        # 根据id获取知识点的内容
        print(item.id)
        if item.childCount()==0:
            # 小节
            section=Section()
            self.tab_widget.addTab(section,item.name)
            # 设置为当前页面
            self.tab_widget.setCurrentWidget(section)

    def creatMenu(self, menuData):
        menu = QTreeWidget(self)
        # 添加树节点
        menu.headerItem().setText(0, menuData["className"])
        # 树节点点击事件
        menu.itemClicked.connect(self.on_node_clicked)
        for chapter in menuData["chapter"]:
            chapter_item = QTreeWidgetItem(menu, chapter["name"] + chapter["alias"], chapter["id"],0)
            self.recursive_node_traversal(chapter["node"], chapter_item)
        return menu

    def initUI(self):
        hbox = QHBoxLayout(self)
        menu=self.creatMenu(self.menuData)
        hbox.addWidget(menu, 20)

        # 创建一个弹性空间
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox.addItem(spacer)

        # 创建TableWidget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.closeTable)


        widget2 = QWidget(self)
        widget2.setStyleSheet("background-color: blue;")
        self.tab_widget.addTab(widget2,"首页")
        hbox.addWidget(self.tab_widget, 80)

        self.setLayout(hbox)

        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Horizontal Layout with Automatic Resizing')
        self.show()



# 移除Tbalwwidget中的table
    def closeTable(self,index):
        if index> 0:
            self.tab_widget.removeTab(index)
        else:
            pass