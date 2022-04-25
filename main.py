from Telas.home_page import Ui_MainHomePage
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainHomePage = QtWidgets.QMainWindow()
    ui = Ui_MainHomePage()
    ui.setupUi(MainHomePage)
    MainHomePage.show()
    sys.exit(app.exec_())
