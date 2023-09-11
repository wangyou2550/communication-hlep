from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QListWidget, QHBoxLayout, QPushButton, QStackedWidget, \
    QTextEdit, QWidget, QDesktopWidget, QMenu, QAction, QGridLayout, QFileDialog

from communication.RelationStepDialog import RelationStepDialog
from communication.StepDialog2 import StepDialog
import requests

from myqt.StepListWidget import StepListWidget
from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.ImageDisplayWidget import ImageDisplayWidget
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools


class NodeDialog(QDialog):
    add_dialog_signal = pyqtSignal(QDialog)
    def __init__(self, section_id,section_name, parent=None):
        super().__init__(parent)
        self.section_id=section_id
        self.section_name=section_name
        self.current_step_id=0
        self.section=RequestTools.get_method(PathConstant.ADD_SECTION+"/"+str(section_id))
        self.initUI()
        self.resize_dialog()

    def resize_dialog(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.availableGeometry(self)
        target_width = int(screen_rect.width() )
        target_height = int(screen_rect.height() )
        self.setGeometry(screen_rect.x(), screen_rect.y(), target_width, target_height)
        # 获取屏幕的几何信息
        screen_geo = QDesktopWidget().screenGeometry()

        # 获取 QDialog 的几何信息
        dialog_geo = self.frameGeometry()

        # 将 QDialog 移动到屏幕的中心
        self.move(int((screen_geo.width() - dialog_geo.width()) / 2), int((screen_geo.height() - dialog_geo.height()) / 2))


    def initUI(self):
        self.setWindowTitle(self.section_name)
        vbox= QVBoxLayout()
        stepWidget=QWidget()
        hbox2 = QHBoxLayout(stepWidget)
        self.step_list_widget=self.createStepList()

        self.createImageStackWidget()
        self.relation_node_list_widget = StepListWidget(steps=None)
        self.relation_node_list_widget.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        hbox2.addWidget(self.step_list_widget,10)
        hbox2.addWidget(self.image_stack_widget,80)
        hbox2.addWidget(self.relation_node_list_widget,10)
        stepWidget.setLayout(hbox2)
        vbox.addWidget(self.createButtons(),15)
        vbox.addWidget(stepWidget,85)
        # self.comment_widget=QTextEdit(self)
        # vbox.addWidget(self.comment_widget,15)
        self.setLayout(vbox)

    def createImageStackWidget(self):
        self.image_stack_widget = QStackedWidget(self)
        for step in self.section["steps"]:
            image_widget=ImageDisplayWidget(step["imageSrc"])
            self.image_stack_widget.addWidget(image_widget)


    def createStepList(self):
        step_list_widget = QListWidget()
        if self.section["steps"]:
            for step in self.section["steps"]:
                step_list_widget.addItem(StepListWidgetItem(step["name"],step["id"],step["imageSrc"]))
        step_list_widget.itemClicked.connect(self.step_clicked)
        step_list_widget.currentRowChanged.connect(self.image_display)
        return step_list_widget

    # step点击，将当前step_id设置为目前值，显示图片值
    def step_clicked(self,item):
        self.current_step_id=item.id
        stepVo=RequestTools.get_method(PathConstant.GET_STEP+"/"+str(item.id))
        self.relation_node_list_widget.addStepItem(stepVo["relationSteps"])

    # 显示图片
    def image_display(self,i):
        self.image_stack_widget.setCurrentIndex(i)







    # 获取buttons工具栏
    def createButtons(self):
        buttons = QWidget()
        grid = QGridLayout(buttons)
        names = ['步骤新增', '步骤编辑', '步骤删除',
                '关联步骤新增', '关联步骤编辑', '关联步骤删除',
                '关联题新增', '关联题编辑', '关联题删除']

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
        if button_text =="步骤新增":
            dialog=StepDialog(self.section_id)
            dialog.exec_()
        if button_text =="关联步骤新增":
            if self.current_step_id != 0:
                dialog=RelationStepDialog(self.current_step_id)
                dialog.exec_()

        if button_text =="关联新增":
            self.addStep()

    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.gif)", options=options)
        if file_path:
            with open(file_path, 'rb') as image_file:
                files = {'file': (file_path, image_file)}
                response = requests.post(PathConstant, files=files)

                if response.status_code == 200:
                    print("Image uploaded successfully")
                    return response.data
                else:
                    print("Image upload failed. Status code:", response.status_code)
                    return ''

    @pyqtSlot(QDialog)
    def show_dialog_in_table_widget(self, dialog):
        self.add_dialog_signal.emit(dialog)