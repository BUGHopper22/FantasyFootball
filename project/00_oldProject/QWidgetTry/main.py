import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from pro.mainPage import introductionPage

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = introductionPage()

    window.setWindowTitle("Fantasy football")
    window.show()

    sys.exit(app.exec_())