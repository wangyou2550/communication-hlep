import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel, QPushButton, QMenu, QAction, \
    QActionGroup


class NavigationMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.isCollapse = True

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 添加单选按钮组
        radio_group = QRadioButton("展开")
        radio_group.setChecked(False)
        radio_group.toggled.connect(self.onRadioButtonClicked)
        layout.addWidget(radio_group)

        # 添加菜单按钮
        self.menu_button = QPushButton("点击查看菜单")
        self.menu_button.clicked.connect(self.showMenu)
        layout.addWidget(self.menu_button)

        # 设置布局
        self.setLayout(layout)

        # 创建菜单
        self.menu = QMenu(self)
        self.createMenu()

    def onRadioButtonClicked(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            if radio_button.text() == "展开":
                self.isCollapse = False
            else:
                self.isCollapse = True

    def showMenu(self):
        self.menu.exec_(self.menu_button.mapToGlobal(self.menu_button.rect().bottomLeft()))

    def createMenu(self):
        # 添加菜单项
        submenu1 = self.menu.addMenu("导航一")
        submenu1.addAction("选项1")
        submenu1.addAction("选项2")
        submenu2 = self.menu.addMenu("导航二")
        submenu2.addAction("选项3")
        submenu3 = submenu2.addMenu("选项4")
        submenu3.addAction("选项5")
        submenu3.addAction("选项6")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 添加导航菜单
        nav_menu = NavigationMenu()
        layout.addWidget(nav_menu)

        self.setLayout(layout)
        self.setWindowTitle("Navigation Menu Example")
        self.setGeometry(100, 100, 300, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
