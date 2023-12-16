
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from communication.HomePage import Home_Page
from ui.MainWindow import MainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    # MainWindow = QMainWindow()  # 创建主窗口
    # ui=Home_Page()
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())  # 在主线程中退出
