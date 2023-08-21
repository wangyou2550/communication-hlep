
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from communication.HomePage import Home_Page
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    MainWindow = QMainWindow()  # 创建主窗口
    # word = Word.get_word()
    # word.Visible = True
    # ui = MyMainWindow()
    # # ui.setupUi(MainWindow)
    #
    # # MainWindow.show()  # 显示主窗口
    # ui.show()
    #
    # ui=Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    ui=Home_Page()

    sys.exit(app.exec_())  # 在主线程中退出
