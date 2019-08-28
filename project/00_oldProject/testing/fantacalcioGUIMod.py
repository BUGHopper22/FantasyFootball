import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, QRectF, Qt, SIGNAL
from PyQt5.QtCore import pyqtSignal,QObject,pyqtSlot


from PySide2.QtWidgets import QWizard, QMainWindow, QFileDialog, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QProgressBar
from PySide2.QtGui import QPixmap
import urllib.request
import time

def createIntroPage(self):
    page = QWizardPage()
    page.setTitle("Introduction")

    label = QLabel("This wizard will help you register your copy of Super Product Two.")
    label.setWordWrap(True)

    layout = QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page



# QWizardPage *createRegistrationPage()

#     ...


# def createConclusionPage(self):

#     ...




def main():
    app = QtWidgets.QApplication(sys.argv)

    # print("WW")
    # translatorFileName = "qt_"
    # translatorFileName += QLocale.system().name()
    # translator = QTranslator(app)
    # if translator.load(translatorFileName, QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
    #     app.installTranslator(translator)

    wizard = QWizard()
    wizard.addPage(createIntroPage())
    # wizard.addPage(createRegistrationPage())
    # wizard.addPage(createConclusionPage())

    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()

    return app.exec_()

if __name__ == "__main__":
    main()