import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from gui.p00_main import mainPage

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainPage()

    window.setWindowTitle("Fantasy football")
    window.show()

    sys.exit(app.exec_())