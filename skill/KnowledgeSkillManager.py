import sys
import random

from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView, QScrollArea, QLabel, QComboBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QColor

from config.GlobalConstant import GlobalConstant
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
from skill.Skill import Skill
from skill.SkillDialog import SkillDialog


class KnowledgeSkillManager(QWidget):
    add_widget_signal = pyqtSignal(QWidget)
    def __init__(self):
        super().__init__()
        self.knowledge_points = []  # 存储知识点数据
        self.isShow = True  # 控制新增和修改按钮显示
        self.initUI()
        self.search_knowledge_points()  # 生成模拟数据

    def initUI(self):
        self.setWindowTitle('知识点管理')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # 搜索区域
        search_layout = QHBoxLayout()
        chapter_label=QLabel('章:')
        chapter_label.setFont(QFont('Arial', 14))
        self.create_chapter_combox()

        search_label = QLabel('搜索:')
        search_label.setFont(QFont('Arial', 14))
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText('输入知识点名称搜索...')
        self.search_input.setStyleSheet(
            "background-color: #f0f0f0; border: 1px solid #d0d0d0; padding: 5px; font-size: 14px;")
        self.search_button = QPushButton('搜索', self)
        self.search_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 5px 10px; border: none; border-radius: 4px; font-size: 14px;")
        self.search_button.clicked.connect(self.search_knowledge_points)
        search_layout.addWidget(chapter_label)
        search_layout.addWidget(self.chapter_combox)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)


        if GlobalConstant.IS_ADMIN:
            # 新增和修改按钮
            button_layout = QHBoxLayout()
            self.add_button = QPushButton('新增', self)
            self.add_button.setStyleSheet(
                "background-color: #4CAF50; color: white; padding: 5px 10px; border: none; border-radius: 4px; font-size: 14px;")
            self.add_button.clicked.connect(self.add_knowledge_point)
            self.edit_button = QPushButton('修改', self)
            self.edit_button.setStyleSheet(
                "background-color: #2196F3; color: white; padding: 5px 10px; border: none; border-radius: 4px; font-size: 14px;")
            self.edit_button.clicked.connect(self.edit_knowledge_point)
            button_layout.addWidget(self.add_button)
            button_layout.addWidget(self.edit_button)
            layout.addLayout(button_layout)

        # 控制新增和修改按钮的显示
        # if self.isShow:
        #     layout.addLayout(button_layout)

        # 表格
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)  # 修正为 6 列
        self.table.setHorizontalHeaderLabels(['ID', '名称', '真题数量', '习题数量', '操作'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setFont(QFont('Arial', 14))  # 设置表格字体大小

        # 设置表格样式
        self.table.setStyleSheet("QTableWidget {background-color: #f0f0f0; color: #333; font-size: 14px;}"
                                 "QTableWidget::item {padding: 5px;}"
                                 "QTableWidget::item:selected {background-color: #e0e0e0;}")

        # 设置操作列的宽度
        # self.table.setColumnWidth(5, 200)
        # 设置列宽
        default_column_width = 100  # 其他列的默认宽度
        self.table.setColumnWidth(0, default_column_width)  # ID 列
        self.table.setColumnWidth(1, default_column_width)  # 名称列
        self.table.setColumnWidth(2, default_column_width)  # 出题类型数量列
        self.table.setColumnWidth(3, default_column_width)  # 真题数量列
        self.table.setColumnWidth(4, default_column_width)  # 习题数量列
        self.table.setColumnWidth(5, default_column_width * 3)  # 操作列宽度为其他列的 3 倍

        # 添加滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table)

        layout.addLayout(search_layout)
        layout.addWidget(scroll_area)

        self.setLayout(layout)

    def create_chapter_combox(self):
        _translate = QtCore.QCoreApplication.translate
        self.chapter_combox = QComboBox()
        self.chapter_combox.setObjectName("comboBox")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.addItem("")
        self.chapter_combox.setItemText(0, _translate("Dialog", ""))
        self.chapter_combox.setItemText(1, _translate("Dialog", "第一章"))
        self.chapter_combox.setItemText(2, _translate("Dialog", "第二章"))
        self.chapter_combox.setItemText(3, _translate("Dialog", "第三章"))
        self.chapter_combox.setItemText(4, _translate("Dialog", "第四章"))
        self.chapter_combox.setItemText(5, _translate("Dialog", "第五章"))
        self.chapter_combox.setItemText(6, _translate("Dialog", "第六章"))
        self.chapter_combox.setItemText(7, _translate("Dialog", "第七章"))
        self.chapter_combox.setItemText(8, _translate("Dialog", "第八章"))
        self.chapter_combox.setItemText(9, _translate("Dialog", "第九章"))
        self.chapter_combox.setItemText(10, _translate("Dialog", "第十章"))
        self.chapter_combox.setItemText(11, _translate("Dialog", "第十一章"))
        self.chapter_combox.setCurrentIndex(0)


    # 更新查找的技巧
    def search_knowledge_points(self):
        chapter_id=self.chapter_combox.currentIndex()
        name = self.search_input.text()
        data={}
        data["name"] = self.search_input.text()
        data["chapterId"]=self.chapter_combox.currentIndex()
        skillList = HttpTool.get(PathConstant.GET_SKILL_LIST,data)
        if skillList:
            self.populate_table(skillList)


    def populate_table(self, skillList):
        self.table.setRowCount(0)  # 清空表格
        for skill in skillList:
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(str(skill['id'])))
                self.table.setItem(row_position, 1, QTableWidgetItem(skill['name']))
                self.table.setItem(row_position, 2, QTableWidgetItem(str(skill['realQuestionCount'])))
                self.table.setItem(row_position, 3, QTableWidgetItem(str(skill['exerciseCount'])))
                # 设置行高
                self.table.setRowHeight(row_position, 50)
                # 添加操作按钮
                query_button = QPushButton('查询', self)
                query_button.setStyleSheet(
                    "background-color: #2196F3; color: white; padding: 5px 5px; border: none; border-radius: 10px; font-size: 14px;")

                # 设置按钮的大小
                query_button.setFixedSize(60, 30)


                query_button.clicked.connect(lambda checked, id=skill['id']: self.query_knowledge_point(id))


                # 将按钮添加到表格单元格
                button_layout = QHBoxLayout()
                button_layout.addWidget(query_button)
                if GlobalConstant.IS_ADMIN:
                    edit_button = QPushButton('编辑', self)
                    edit_button.setStyleSheet(
                        "background-color: #4CAF50; color: white; padding: 5px 5px; border: none; border-radius: 10px; font-size: 14px;")
                    delete_button = QPushButton('删除', self)
                    delete_button.setStyleSheet(
                        "background-color: #f44336; color: white; padding: 5px 5px; border: none; border-radius: 10px; font-size: 14px;")

                    edit_button.setFixedSize(60, 30)
                    delete_button.setFixedSize(60, 30)
                    edit_button.clicked.connect(lambda checked, id=skill['id']: self.edit_knowledge_point(id))
                    delete_button.clicked.connect(lambda checked, id=skill['id']: self.delete_knowledge_point(id))
                    button_layout.addWidget(edit_button)
                    button_layout.addWidget(delete_button)

                # 创建一个 widget 来包含按钮
                button_widget = QWidget()
                button_widget.setLayout(button_layout)
                self.table.setCellWidget(row_position, 4, button_widget)

    def query_knowledge_point(self, id):
        skill = Skill(id)
        self.add_widget_signal.emit(skill)
        # skill.add_dialog_signal.connect(self.show_dialog_in_table_widget)
        # question.add_question_signal.connect(self.show_question_in_table_widget)

# 增加技巧
    def add_knowledge_point(self):
        dialog = SkillDialog(0)
        dialog.exec_()

    def edit_knowledge_point(self, id):
        QMessageBox.information(self, '编辑知识点', f'编辑知识点 ID: {id} 功能尚未实现')

    def delete_knowledge_point(self, id):
        self.knowledge_points = [kp for kp in self.knowledge_points if kp['id'] != id]
        self.populate_table()
