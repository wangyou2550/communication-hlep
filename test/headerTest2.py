import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QListWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Demo Application")
        self.setGeometry(100, 100, 1200, 800)

        # 创建主窗口和布局
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # 创建顶部工具栏
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        home_action = QAction(QIcon("home.png"), "首页", self)
        user_action = QAction(QIcon("user.png"), "用户管理", self)
        toolbar.addAction(home_action)
        toolbar.addAction(user_action)

        # 创建侧边栏
        sidebar = QTreeWidget()
        sidebar.setHeaderHidden(True)
        system_management = QTreeWidgetItem(["系统管理"])
        user_management = QTreeWidgetItem(["用户管理"])
        role_management = QTreeWidgetItem(["角色管理"])
        menu_management = QTreeWidgetItem(["菜单管理"])
        system_management.addChild(user_management)
        system_management.addChild(role_management)
        system_management.addChild(menu_management)
        sidebar.addTopLevelItem(system_management)

        # 创建主内容区域
        content_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        search_layout = QHBoxLayout()

        search_layout.addWidget(QLabel("登录名称:"))
        search_layout.addWidget(QLineEdit())
        search_layout.addWidget(QLabel("手机号:"))
        search_layout.addWidget(QLineEdit())
        search_layout.addWidget(QLabel("用户状态:"))
        search_layout.addWidget(QLineEdit())
        search_layout.addWidget(QPushButton("搜索"))
        search_layout.addWidget(QPushButton("重置"))

        content_layout.addLayout(search_layout)

        table = QTableWidget(2, 4)
        table.setHorizontalHeaderLabels(["用户ID", "登录名称", "手机号", "用户状态"])
        table.setItem(0, 0, QTableWidgetItem("1"))
        table.setItem(0, 1, QTableWidgetItem("admin"))
        table.setItem(0, 2, QTableWidgetItem("15888888888"))
        table.setItem(0, 3, QTableWidgetItem("在线"))
        table.setItem(1, 0, QTableWidgetItem("2"))
        table.setItem(1, 1, QTableWidgetItem("ry"))
        table.setItem(1, 2, QTableWidgetItem("15666666666"))
        table.setItem(1, 3, QTableWidgetItem("离线"))

        content_layout.addWidget(table)

        top_layout.addWidget(sidebar, 1)
        top_layout.addLayout(content_layout, 3)

        main_layout.addLayout(top_layout)

        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())