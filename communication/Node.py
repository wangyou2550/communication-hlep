from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QListWidget, QHBoxLayout, QPushButton, QStackedWidget, \
    QTextEdit, QWidget, QDesktopWidget, QMenu, QAction


class NodeDialog(QDialog):
    def __init__(self, node_id,node_name, parent=None):
        super().__init__(parent)
        self.node_id=node_id
        self.node_name=node_name
        self.initUI()
        self.resize_dialog()

    def resize_dialog(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.availableGeometry(self)
        target_width = int(screen_rect.width() * 0.8)
        target_height = int(screen_rect.height() * 0.8)
        self.setGeometry(screen_rect.x(), screen_rect.y(), target_width, target_height)

    def initUI(self):
        self.setWindowTitle(self.node_name)
        vbox= QVBoxLayout()
        buttons=QWidget()
        hbox=QHBoxLayout(buttons)
        self.step_menu=self.createMenu("步骤")
        self.image_menu=self.createMenu("图片")
        self.relation_node_menu=self.createMenu("关联知识点")
        self.step_menu.triggered[QAction].connect(self.stepOperate)
        self.image_menu.triggered[QAction].connect(self.imageOperate)
        self.relation_node_menu.triggered[QAction].connect(self.relationNodeOperate)

        hbox.addWidget(self.step_menu,10)
        hbox.addWidget(self.image_menu,10)
        hbox.addWidget(self.relation_node_menu,10)
        buttons.setLayout(hbox)
        stepWidget=QWidget()
        hbox2 = QHBoxLayout(stepWidget)
        self.step_list_widget=QListWidget()
        self.image_stack_widget=QStackedWidget(self)
        self.relation_node_list_widget = QListWidget()
        hbox2.addWidget(self.step_list_widget,10)
        hbox2.addWidget(self.image_stack_widget,80)
        hbox2.addWidget(self.relation_node_list_widget,10)
        stepWidget.setLayout(hbox2)
        self.comment_widget=QTextEdit(self)
        vbox.addWidget(buttons,10)
        vbox.addWidget(stepWidget,80)
        vbox.addWidget(self.comment_widget,10)
        self.setLayout(vbox)

    def createMenu(self,text):
        menu=QMenu(text)
        menu.addAction("新建")
        menu.addAction("编辑")
        menu.addAction("删除")
        return menu

    def stepOperate(self,q):
        if q.text =="新建":
            print(q.text)
        if q.text =="编辑":
            print(q.text)
        if q.text =="删除":
            print(q.text)


    def imageOperate(self,q):
        if q.text =="新建":
            print(q.text)
        if q.text =="编辑":
            print(q.text)
        if q.text =="删除":
            print(q.text)

    def relationNodeOperate(self,q):
        if q.text == "新建":
            print(q.text)
        if q.text == "编辑":
            print(q.text)
        if q.text == "删除":
            print(q.text)


