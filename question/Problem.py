# -*- coding: utf-8 -*-
import requests
# Form implementation generated from reading ui file 'Problem.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QFileDialog

from myreqeust.PathConstant import PathConstant
from myreqeust.RequestTools import RequestTools


class Problem(QDialog):
    def __init__(self,chapter_id):
        super().__init__()
        self.chapter_id=chapter_id
        self.setupUi()
        self.setWindowModality(Qt.ApplicationModal)

    def setupUi(self):
        self.setObjectName("Problem")
        self.resize(765, 783)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(410, 720, 341, 20))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 571, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.number_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.number_lineEdit.setObjectName("number_lineEdit")
        self.gridLayout.addWidget(self.number_lineEdit, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.problem_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.problem_comboBox.setObjectName("problem_comboBox")
        self.problem_comboBox.addItem("")
        self.problem_comboBox.addItem("")
        self.gridLayout.addWidget(self.problem_comboBox, 4, 1, 1, 1)
        self.type_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.type_comboBox.setObjectName("type_comboBox")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.gridLayout.addWidget(self.type_comboBox, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.name_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 0, 1, 1, 1)
        self.order_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.order_lineEdit.setObjectName("order_lineEdit")
        self.gridLayout.addWidget(self.order_lineEdit, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.uploadImage)
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.image_lable = QtWidgets.QLabel(self)
        self.image_lable.setGeometry(QtCore.QRect(40, 400, 591, 241))
        self.image_lable.setObjectName("label_7")

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.add_problem) # type: ignore
        self.buttonBox.rejected.connect(self.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "题类型"))
        self.problem_comboBox.setItemText(0, _translate("Dialog", "选择题"))
        self.problem_comboBox.setItemText(1, _translate("Dialog", "大题"))
        self.type_comboBox.setItemText(0, _translate("Dialog", "练习题"))
        self.type_comboBox.setItemText(1, _translate("Dialog", "真题"))
        self.type_comboBox.setItemText(2, _translate("Dialog", "模拟题"))
        self.label_2.setText(_translate("Dialog", "数量"))
        self.label_3.setText(_translate("Dialog", "序号"))
        self.label_6.setText(_translate("Dialog", "题"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label_4.setText(_translate("Dialog", "类型"))
        self.label.setText(_translate("Dialog", "名称"))
        self.image_lable.setText(_translate("Dialog", "TextLabel"))

    def uploadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.gif)",
                                                   options=options)
        if file_path:
            with open(file_path, 'rb') as image_file:
                files = {'file': (file_path, image_file)}
                response = requests.post(PathConstant.UPLOAD_IMAGE, files=files)

                if response.status_code == 200:
                    self.image_src=response.json()["msg"]
                    self.display_online_image(self.image_src)
                    print("Image uploaded successfully")
                else:
                    print("Image upload failed. Status code:", response.status_code)

    def add_problem(self):
        data = {}
        data["name"] = self.name_lineEdit.text()
        data["sort"] = self.order_lineEdit.text()
        data["choiceNum"] = self.number_lineEdit .text()
        data["chapter"] = self.chapter_id
        data["type"] = str(self.type_comboBox.currentIndex())
        data["problemType"] = str(self.problem_comboBox.currentIndex())
        if self.image_src:
            data["imageSrc"]=self.image_src
            RequestTools.post_method(PathConstant.ADD_QUESTION, data)
        self.accept()

# 显示在线图片
    def display_online_image(self, image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.image_lable.setPixmap(pixmap)
            self.image_lable.setScaledContents(True)  # 自动缩放图片以适应标签大小
        else:
            self.image_label.setText("Failed to load image")