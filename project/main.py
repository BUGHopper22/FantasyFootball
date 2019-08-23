import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from graphics.f00_fantacalcioGuiStart import Wizard
# from project import *
# import testing.test

if __name__ == "__main__":
    app = QApplication(sys.argv)

    wizard = Wizard()

    wizard.setWindowTitle("Fantacalcio")
    wizard.setSideWidget(None)
    wizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
    wizard.show()

    sys.exit(app.exec_())