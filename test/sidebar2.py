import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class Widget1(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.show_widget2)
        button2 = QPushButton("Button 2")
        button2.clicked.connect(self.show_widget3)
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)

    def show_widget2(self):
        main_window.show_widget(Widget2())

    def show_widget3(self):
        main_window.show_widget(Widget3())


class Widget2(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Widget 2"))
        self.setLayout(layout)


class Widget3(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Widget 3"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget1 = Widget1()
        self.widget2 = Widget2()
        self.widget3 = Widget3()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.widget1)
        self.layout.addWidget(QWidget())  # 占位部件，用于显示 widget2 或 widget3

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def show_widget(self, widget):
        # 删除占位部件并添加新的部件
        self.layout.itemAt(1).widget().deleteLater()
        self.layout.addWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("Horizontal Layout Demo")
    main_window.setGeometry(100, 100, 800, 600)
    main_window.show()
    sys.exit(app.exec_())