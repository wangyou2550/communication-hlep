from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QListWidget, QHBoxLayout, QPushButton, QStackedWidget, \
    QTextEdit, QWidget, QDesktopWidget, QMenu, QAction, QGridLayout, QFileDialog

from communication.FeedbackDialog import Feedback_Dialog
from communication.RelationStepDialog import RelationStepDialog
from communication.StepDialog2 import StepDialog
import requests

from communication.StepSearchDialog import StepSearchDialog
from component.ImageViewer import ImageViewer
from component.ZoomableGraphicsView import ZoomableGraphicsView
from config.GlobalConstant import GlobalConstant
from myqt.StepListWidget import StepListWidget
from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.HttpTool import HttpTool
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
        self.feedback_value = 0
        self.favorite_value = 0
        self.title=section_name
        # self.section=RequestTools.get_method(PathConstant.ADD_SECTION+"/"+str(section_id))
        self.section=HttpTool.get(PathConstant.ADD_SECTION+"/"+str(section_id))
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
        self.hbox2 = QHBoxLayout(stepWidget)
        self.step_list_widget=self.createStepList()

        vbox.addLayout(self.create_feed_favorite_button(), 10)
        self.createImageStackWidget()

        vbox2=QVBoxLayout()
        self.relation_node_list_widget = StepListWidget(steps=None)
        self.relation_node_list_widget.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        self.related_node_list_widget = StepListWidget(steps=None)
        self.related_node_list_widget.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        vbox2.addWidget(self.relation_node_list_widget)
        vbox2.addWidget(self.related_node_list_widget)
        self.hbox2.addWidget(self.step_list_widget,10)
        # self.hbox2.addWidget(self.image_stack_widget,80)
        self.hbox2.addWidget(self.image_widget,80)
        self.hbox2.addLayout(vbox2,10)
        # self.hbox2.addWidget(self.relation_node_list_widget,10)
        stepWidget.setLayout(self.hbox2)
        if GlobalConstant.IS_ADMIN:
            vbox.addWidget(self.createButtons(),15)

        vbox.addWidget(stepWidget,85)


        # self.comment_widget=QTextEdit(self)
        # vbox.addWidget(self.comment_widget,15)
        self.setLayout(vbox)

    def createImageStackWidget(self):
        # self.image_stack_widget = QStackedWidget(self)
        self.image_widget = QStackedWidget(self)
        # 预加载第一张图片
        if len(self.section["steps"])>0:
            self.current_step_id =self.section["steps"][0]["id"]
            self.image_widget = ImageViewer(self.section["steps"][0]["imageSrc"])
            self.update_step_feedback_favorite(self.section["steps"][0])
            # self.image_stack_widget.addWidget(image_widget)
        # for step in self.section["steps"]:
        #     # image_widget=ImageDisplayWidget(step["imageSrc"])
        #     # image_widget=ZoomableGraphicsView(step["imageSrc"])
        #     image_widget=ImageViewer(step["imageSrc"])
        #     self.image_stack_widget.addWidget(image_widget)


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
        stepVo=HttpTool.get(PathConstant.GET_STEP+"/"+str(item.id))
        self.update_step_feedback_favorite(stepVo["step"])
        self.relation_node_list_widget.addStepItem(stepVo["relationSteps"])
        self.related_node_list_widget.addRelatedStepItem(stepVo["relatedSteps"])

    # 跟新题的收藏反馈
    def update_step_feedback_favorite(self,step):
        if step["feedback"]:
            self.feedback_value = step["feedback"]
        else:
            self.feedback_value =0
        if step["favorite"]:
            self.favorite_value = step["favorite"]
        else:
            self.favorite_value =0
        self.updateButtons()

    # 显示图片
    def image_display(self,i):
        self.hbox2.removeItem(self.hbox2.itemAt(1))
        self.image_widget.deleteLater()
        self.image_widget = ImageViewer(self.section["steps"][i]["imageSrc"])
        self.hbox2.insertWidget(1,self.image_widget,80)

        # self.image_widget.updateImage(self.section["steps"][i]["imageSrc"])
        # self.image_stack_widget.setCurrentIndex(i)

# 收藏反馈按钮
    def create_feed_favorite_button(self):
        layout = QHBoxLayout()

        self.feedback_button = QPushButton()
        self.feedback_button.clicked.connect(self.feedbackClicked)
        layout.addWidget(self.feedback_button)

        self.favorite_button = QPushButton()
        self.favorite_button.clicked.connect(self.favoriteClicked)
        layout.addWidget(self.favorite_button)

        self.updateButtons()
        return layout

    def updateButtons(self):
        if self.feedback_value == 0:
            self.feedback_button.setText('反馈')
            self.feedback_button.setStyleSheet("background-color: green;")
        else:
            self.feedback_button.setText('已反馈')
            self.feedback_button.setStyleSheet("background-color: red;")

        if self.favorite_value == 0:
            self.favorite_button.setText('收藏')
            self.favorite_button.setStyleSheet("background-color: green;")
        else:
            self.favorite_button.setText('已收藏')
            self.favorite_button.setStyleSheet("background-color: red;")


    def feedbackClicked(self):
        self.feedback_value = 1-self.feedback_value
        data={}
        data["stepId"]=self.current_step_id
        data["feedback"]=self.feedback_value
        # //取消反馈，直接点击就可以
        if self.feedback_value==0:
            HttpTool.post(PathConstant.ADD_STEP_FEEDBACK_FAVORITE, data)
        else:
            feedDialog=Feedback_Dialog(data,1)
            feedDialog.exec_()
        self.updateButtons()

    def favoriteClicked(self):
        self.favorite_value = 1-self.favorite_value
        data={}
        data["stepId"]=self.current_step_id
        data["favorite"]=self.favorite_value
        HttpTool.post(PathConstant.ADD_STEP_FEEDBACK_FAVORITE, data)
        self.updateButtons()




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
                # dialog=RelationStepDialog(self.current_step_id)
                dialog=StepSearchDialog(self.current_step_id)
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