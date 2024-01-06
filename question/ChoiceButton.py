from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor, QFont

class ChoiceButton(QWidget):
    def __init__(self,serial_number):
        super().__init__()
        # 题的序号
        self.serial_number = serial_number

        self.initUI()
    def initUI(self):
        # 创建四个单选按钮
        self.serial_lable=QLabel(str(self.serial_number))
        self.radioButtonA = QRadioButton('A')
        self.radioButtonB = QRadioButton('B')
        self.radioButtonC = QRadioButton('C')
        self.radioButtonD = QRadioButton('D')
        font = QFont("Arial", 10, QFont.Bold)  # 创建一个字体对象，设置字体名称、大小和加粗
        self.radioButtonA.setFont(font)  # 设置单选按钮的字体
        self.radioButtonB.setFont(font)  # 设置单选按钮的字体
        self.radioButtonC.setFont(font)  # 设置单选按钮的字体
        self.radioButtonD.setFont(font)  # 设置单选按钮的字体


        # 设置未选中状态的样式为灰色圆形
        self.radioButtonA.setStyleSheet("QRadioButton::indicator { border-radius: 20px; background-color: gray; }")
        self.radioButtonB.setStyleSheet("QRadioButton::indicator { border-radius: 20px; background-color: gray; }")
        self.radioButtonC.setStyleSheet("QRadioButton::indicator { border-radius: 20px; background-color: gray; }")
        self.radioButtonD.setStyleSheet("QRadioButton::indicator { border-radius: 20px; background-color: gray; }")

        # 设置选中状态的样式为绿色圆形
        self.radioButtonA.setStyleSheet("QRadioButton::indicator:checked { background-color: green; }")
        self.radioButtonB.setStyleSheet("QRadioButton::indicator:checked { background-color: green; }")
        self.radioButtonC.setStyleSheet("QRadioButton::indicator:checked { background-color: green; }")
        self.radioButtonD.setStyleSheet("QRadioButton::indicator:checked { background-color: green; }")

        # 创建水平布局，并将四个单选按钮添加进去
        hbox = QHBoxLayout()
        hbox.addWidget(self.serial_lable)
        hbox.addWidget(self.radioButtonA)
        hbox.addWidget(self.radioButtonB)
        hbox.addWidget(self.radioButtonC)
        hbox.addWidget(self.radioButtonD)
        # 连接单选按钮的clicked信号到处理槽函数
        self.radioButtonA.clicked.connect(self.printSelectedOption)
        self.radioButtonB.clicked.connect(self.printSelectedOption)
        self.radioButtonC.clicked.connect(self.printSelectedOption)
        self.radioButtonD.clicked.connect(self.printSelectedOption)

        # 创建垂直布局，并将水平布局添加进去
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.show()
    def printSelectedOption(self):
        # 获取被选中的选项并进行打印
        if self.radioButtonA.isChecked():
            self.answer="A"
        elif self.radioButtonB.isChecked():
            self.answer="B"
        elif self.radioButtonC.isChecked():
            self.answer="C"
        elif self.radioButtonD.isChecked():
            self.answer="D"