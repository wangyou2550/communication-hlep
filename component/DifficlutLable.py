
from PyQt5.QtWidgets import  QMainWindow, QHBoxLayout,  QWidget, QLabel


class DifficultLables(QMainWindow):
    def __init__(self,count,trueCount):
        super().__init__()

        # 创建水平布局管理器
        layout = QHBoxLayout()

        # 创建按钮并添加到布局中
        # 创建标签
        self.label1 = QLabel('提交次数: '+str(count))
        self.label2= QLabel('通过次数: '+str(trueCount))
        self.label3= QLabel('通过率: '+self.rateCount(trueCount,count))

        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)


        # 创建部件并设置布局
        widget = QWidget()
        widget.setLayout(layout)

        # 将部件设置为主窗口的中心部分
        self.setCentralWidget(widget)
    def rateCount(self,a,b):
        result = a / b
        percentage = result * 100

        # 将结果格式化为百分比形式，保留两位小数
        formatted_percentage = "{:.2f}%".format(percentage)
        return formatted_percentage
