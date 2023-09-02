# 小节py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QSizePolicy, \
    QSpacerItem, QTableView, QTreeWidget, QCheckBox

from communication.SectionDialog import SectionDialog
from myqt.QTreeWidgetItem import QTreeWidgetItem
from myqt.InfoButton import InfoButton
from utils.JSONUtil import JSONUtil
from communication.Node import NodeDialog
from myreqeust.RequestTools import RequestTools
from myreqeust.PathConstant import PathConstant
class Section(QWidget):
    def __init__(self,section_id):
        super().__init__()
        self.section_pid = section_id
        self.section = RequestTools.get_method(PathConstant.GET_SECTION_CHILD + str(section_id))
        self.chapter_id=self.section["chapterId"]
        self.initUI()

    def initUI(self):
        # 当前pid，id
        self.node_id=-1
        vbox = QVBoxLayout(self)
        # 创建搜索框
        self.createHBox1()
        # self.nodes=JSONUtil.readJsonFile('communication/node.json')

        self.createKnowledgeNodeTableWidget()


        # # 创建一个弹性空间
        # spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.hbox2.addItem(spacer)
        self.create_operation_button()
        vbox.addWidget(self.search_widget,10)
        vbox.addWidget(self.opertion_widget,10)
        vbox.addWidget(self.node_table_widget,80)
        self.setLayout(vbox)

        # 创建操作按钮
    def create_operation_button(self):
        self.opertion_widget=QWidget()
        hbox3 = QHBoxLayout(self.opertion_widget)
        self.add_push_button = QPushButton(self)
        self.add_push_button.setText("新增根节点")
        self.add_child_button=QPushButton(self)
        self.add_child_button.setText("新增子节点")
        self.edit_push_button = QPushButton(self)
        self.edit_push_button.setText("编辑")
        self.delete_push_button = QPushButton(self)
        self.delete_push_button.setText("删除")
        hbox3.addWidget(self.add_push_button)
        hbox3.addWidget(self.add_child_button)
        hbox3.addWidget(self.edit_push_button)
        hbox3.addWidget(self.delete_push_button)
        self.add_push_button.clicked.connect(self.add_node)
        self.add_child_button.clicked.connect(self.add_child_node)
        self.edit_push_button.clicked.connect(self.edit_node)
        self.delete_push_button.clicked.connect(self.delete_node)
        self.opertion_widget.setLayout(hbox3)

# 创建搜索框
    def createHBox1(self):
        self.search_widget=QWidget()
        self.hbox = QHBoxLayout(self.search_widget)
        self.chapter_lable=QLabel(self)
        self.chapter_lable.setText("章")
        self.chapter_combo_box = QComboBox(self)
        self.section_lable = QLabel(self)
        self.section_lable.setText("节")
        self.name_lable = QLabel(self)
        self.name_lable.setText("名称")
        self.section_line_edit =QLineEdit(self)
        self.name_line_edit = QLineEdit(self)
        self.search_push_button = QPushButton(self)
        self.search_push_button.setText("搜索")
        self.hbox.addWidget(self.chapter_lable,10)
        self.hbox.addWidget(self.chapter_combo_box,10)
        self.hbox.addWidget(self.section_lable,10)
        self.hbox.addWidget(self.section_line_edit,20)
        self.hbox.addWidget(self.name_lable,10)
        self.hbox.addWidget(self.name_line_edit,20)
        self.hbox.addWidget(self.search_push_button,20)
        self.search_widget.setLayout(self.hbox)

    def recursive_section_traversal(self, data, item):
        if data:
            for node in data:
                child = QTreeWidgetItem(item,  str(node["id"]), node["id"], node["pid"])
                checkbox = QCheckBox()
                checkbox.setCheckable(True)
                checkbox.setChecked(False)
                self.node_table_widget.setItemWidget(child, 1, checkbox)
                sort_lable = QLabel()
                sort_lable.setText(str(node["sort"]))
                self.node_table_widget.setItemWidget(child, 2, sort_lable)
                name_lable = QLabel()
                name_lable.setText(node["name"])
                self.node_table_widget.setItemWidget(child, 3, name_lable)
                importance_lable = QLabel()
                importance_lable.setText(node["importance"])
                self.node_table_widget.setItemWidget(child, 4, importance_lable)
                difficulty_lable = QLabel()
                difficulty_lable.setText(node["difficulty"])
                self.node_table_widget.setItemWidget(child, 5, difficulty_lable)
                button = InfoButton("查看", node["id"], node["name"])
                button.clicked.connect(self.get_node)
                self.node_table_widget.setItemWidget(child, 6, button)
                self.recursive_section_traversal(node["childList"], child)


# 创建知识点树形列表
    def createKnowledgeNodeTableWidget(self):
        self.node_table_widget =QTreeWidget()
        self.node_table_widget.itemClicked.connect(self.on_node_clicked)
        self.node_table_widget.setColumnCount(7)
        self.node_table_widget.setHeaderLabels(["id", "学习", "章节","名称","难度","重要程度","查看"])
        self.recursive_section_traversal(self.section["childList"],self.node_table_widget)


    def get_node(self):
        sender = self.sender()
        if isinstance(sender, InfoButton):
            print(sender.id)
            node_dialog=NodeDialog(sender.id,sender.name)
            node_dialog.exec_()
            node_dialog.setWindowState(self.windowState() | Qt.WindowMaximized)




    def add_node(self):
        dialog=SectionDialog(self.section_pid,self.chapter_id)
        dialog.exec_()


    def add_child_node(self):
        dialog=SectionDialog(self.node_id,self.chapter_id)
        dialog.exec_()


    def edit_node(self):
        print(self.node_id)

    def delete_node(self):
        RequestTools.delete_method(PathConstant.DELETE_SECTION+"/"+str(self.node_id))
# 点击section-node触发的函数
    def on_node_clicked(self,item):
        self.node_id=item.id
        self.node_pid=item.parent_id
        self.node_name=item.name