import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton



class TabWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Closeable TabWidget Example')

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.closeTable)
        layout.addWidget(self.tab_widget)

        tab1_content = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel('Content of Tab 1'))
        tab1_content.setLayout(tab1_layout)

        tab2_content = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel('Content of Tab 2'))
        tab2_content.setLayout(tab2_layout)

        self.tab_widget.addTab(tab1_content, 'Tab 1')
        self.tab_widget.addTab(tab2_content, 'Tab 2')

        main_widget.setLayout(layout)

        self.show()

    def closeTable(self,index):
        if index> 0:
            self.tab_widget.removeTab(index)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TabWidgetExample()
    sys.exit(app.exec_())
