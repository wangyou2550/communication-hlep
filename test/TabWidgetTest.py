import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QPushButton, QWidget, QVBoxLayout, \
    QCheckBox


class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()


class TreeWithCheckBoxAndButton(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(3)
        self.setHeaderLabels(["Item", "CheckBox", "Button"])

        # root = QTreeWidgetItem(self, ["Root"])
        for i in range(3):
            child = QTreeWidgetItem(self, ["Child " + str(i)])
            # child.set
            checkbox = QCheckBox()
            checkbox.setCheckable(True)
            self.setItemWidget(child, 1, checkbox)

            button = QPushButton("Button " + str(i))
            self.setItemWidget(child, 2, button)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.tree_widget = TreeWithCheckBoxAndButton()

        self.layout.addWidget(self.tree_widget)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
