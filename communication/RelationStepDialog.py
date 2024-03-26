# -*- coding: utf-8 -*-
import requests
# Form implementation generated from reading ui file 'RelationStep.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog

from myqt.QTreeWidgetItem import QTreeWidgetItem
from myqt.StepListWidgetItem import StepListWidgetItem
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools


class RelationStepDialog(QDialog):
    def __init__(self,step_id):
        super().__init__()
        self.step_id=step_id
        self.setupUi()
        self.setWindowModality(Qt.ApplicationModal)
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(757, 842)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(390, 790, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.chapter_label = QtWidgets.QLabel(self)
        self.chapter_label.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.chapter_label.setObjectName("chapter_label")
        self.comboBox = QtWidgets.QComboBox(self)
        self.create_chapter_combox()
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.section_treeWidget = QtWidgets.QTreeWidget(self)
        self.section_treeWidget.setGeometry(QtCore.QRect(20, 80, 251, 311))
        self.section_treeWidget.setObjectName("section_treeWidget")
        self.step_listWidget = QtWidgets.QListWidget(self)
        self.step_listWidget.setGeometry(QtCore.QRect(450, 90, 256, 301))
        self.step_listWidget.setObjectName("step_listWidget")
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(QtCore.QRect(90, 440, 581, 231))
        self.image_label.setObjectName("image_label")


        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.add_relation_step) # type: ignore
        self.buttonBox.rejected.connect(self.reject) # type: ignore
        self.handle_selection_change(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.chapter_label.setText(_translate("Dialog", "章"))
        self.image_label.setText(_translate("Dialog", "TextLabel"))

    def create_chapter_combox(self):
        # chapters=RequestTools.get_method(PathConstant.GET_CHAPTER_SIMPLE_LIST)
        chapters=HttpTool.get(PathConstant.GET_CHAPTER_SIMPLE_LIST)
        for chapter in chapters:
            self.comboBox.addItem(chapter["name"],str(chapter["id"]))
        self.comboBox.currentIndexChanged.connect(self.handle_selection_change)

    def handle_selection_change(self,index):
        chapter_id=self.comboBox.itemData(index)
        chapter_name=self.comboBox.currentText()
        # 先清空，在刷新
        self.section_treeWidget.clear()
        sections=HttpTool.get(PathConstant.GET_SECTION_BY_CHAPTERID+"/"+chapter_id)
        # 添加树节点
        self.section_treeWidget.headerItem().setText(0, chapter_name)
        # 树节点点击事件
        self.section_treeWidget.itemClicked.connect(self.on_section_clicked)
        for section in sections:
            section_item = QTreeWidgetItem(self.section_treeWidget, section["name"], section["id"], 0)
            self.recursive_node_traversal(section["childList"], section_item)

    def recursive_node_traversal(self,data,item):
        if data:
            for node in data:
                node_item = QTreeWidgetItem(item, str(node["sort"]) + node["name"], node["id"],node["pid"])
                self.recursive_node_traversal(node["childList"], node_item)

    def on_section_clicked(self,item):
        section_id=item.id
        section=HttpTool.get(PathConstant.GET_SECTION+"/"+str(section_id))
        steps=section["steps"]
        self.step_listWidget.clear()
        if steps:
            for step in steps:
                self.step_listWidget.addItem(StepListWidgetItem(step["name"],step["id"],step["imageSrc"]))
        self.step_listWidget.itemClicked.connect(self.step_clicked)
    # 点击步骤显示图片
    def step_clicked(self,item):
        self.current_step_id=item.id
        self.current_step_name=item.name
        image_path=item.image_src
        response = requests.get(image_path)
        if response.status_code == 200:
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

    def add_relation_step(self):
        if self.current_step_name:
            data={}
            data["stepId"]=self.step_id
            data["relationStepId"]=self.current_step_id
            data["relationStepName"]=self.current_step_name
            HttpTool.post(PathConstant.ADD_RELATION_STEP, data)
        self.accept()