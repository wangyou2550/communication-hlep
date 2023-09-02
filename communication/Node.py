from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QListWidget, QHBoxLayout, QPushButton, QStackedWidget, \
    QTextEdit, QWidget, QDesktopWidget, QMenu, QAction, QGridLayout


class NodeDialog(QDialog):
    def __init__(self, section_id,section_name, parent=None):
        super().__init__(parent)
        self.section_id=section_id
        self.section_name=section_name
        self.initUI()
        self.resize_dialog()

    def resize_dialog(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.availableGeometry(self)
        target_width = int(screen_rect.width() * 0.8)
        target_height = int(screen_rect.height() * 0.8)
        self.setGeometry(screen_rect.x(), screen_rect.y(), target_width, target_height)

    def initUI(self):
        self.setWindowTitle(self.section_name)
        vbox= QVBoxLayout()
        # buttons=QWidget()
        #
        # hbox=QHBoxLayout(buttons)
        # self.step_menu=self.createMenu("步骤")
        # self.image_menu=self.createMenu("图片")
        # self.relation_node_menu=self.createMenu("关联知识点")
        # self.step_menu.triggered[QAction].connect(self.stepOperate)
        # self.image_menu.triggered[QAction].connect(self.imageOperate)
        # self.relation_node_menu.triggered[QAction].connect(self.relationNodeOperate)
        #
        # hbox.addWidget(self.step_menu,10)
        # hbox.addWidget(self.image_menu,10)
        # hbox.addWidget(self.relation_node_menu,10)
        # buttons.setLayout(hbox)
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
        vbox.addWidget(self.createButtons(),15)
        vbox.addWidget(stepWidget,70)
        vbox.addWidget(self.comment_widget,15)
        self.setLayout(vbox)



# 获取buttons工具栏
    def createButtons(self):
        buttons = QWidget()
        grid = QGridLayout(buttons)
        names = ['步骤新增', '步骤编辑', '步骤删除',
                '图片新增', '图片新增', '图片新增',
                '关联新增', '关联新增', '关联新增']

        positions = [(i, j) for i in range(3) for j in range(3)]
        for position, name in zip(positions, names):
            if name == '':
                continue

            button = QPushButton(name)
            button.clicked.connect(self.buttonClick)
            grid.addWidget(button, *position)
        buttons.setLayout(grid)
        return buttons

    def buttonClick(self):
        sender = self.sender()  # 获取发送信号的对象
        button_text = sender.text()  # 获取按钮的文本
        print(button_text)




