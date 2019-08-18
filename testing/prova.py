import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWizard, QWizardPage, QLineEdit, QGridLayout, QLabel,QVBoxLayout
# from qgis.core import *
# import qgis.utils

class Page1(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('General Properties')
        self.setSubTitle('Enter general properties for this project.')
        
        # create some widgets
        self.project_number_line_edit = QLineEdit()
        self.project_title_line_edit = QLineEdit()
        self.author_line_edit = QLineEdit()        

        # set the page layout
        layout = QGridLayout()
        layout.addWidget(QLabel('Project Number'),0,0)
        layout.addWidget(self.project_number_line_edit,0,1)
        layout.addWidget(QLabel('Title'),1,0)
        layout.addWidget(self.project_title_line_edit,1,1)
        layout.addWidget(QLabel('Author'),2,0)
        layout.addWidget(self.author_line_edit,2,1)
        self.setLayout(layout)

        self.registerField('number*',self.project_number_line_edit)
        self.registerField('title*',self.project_title_line_edit)
        self.registerField('author*',self.author_line_edit)

    def nextId(self):
        # return super().nextId()
        return ProjectWizard.Page2()

class Page2(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('Project Coordinate System')
        self.setSubTitle('Choosing an appropriate projection is important to ensure accurate distance and area measurements.')
        
        print(self.field('number'))

class ProjectWizard(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addPage(Page1(self))
        self.setWindowTitle("New Project")

def runNewProjectWizard():
    app = QtWidgets.QApplication(sys.argv)

    wizard = ProjectWizard()

    wizard.setWindowTitle("Fantacalcio")
    wizard.setSideWidget(None)
    wizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
    print("arriva")
    wizard.show()

    sys.exit(app.exec_())

    # Set the project title
    title=wizard.field('title')
    # QgsProject.instance().setTitle(wizard.field('title'))
    
    number=wizard.field('number')
    author=wizard.field('author')


if __name__ == "__main__":
    runNewProjectWizard()