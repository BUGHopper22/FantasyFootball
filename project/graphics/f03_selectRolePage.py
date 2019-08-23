from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QDialog, QRadioButton,QTextEdit, QWidget, QHBoxLayout, QGroupBox, QGridLayout, QMainWindow, QVBoxLayout, QPushButton, QLabel
from PySide2.QtCore import Signal, Slot
import pandas as pd

class GoalkeeperWindow(QDialog):
    def __init__(self, title, data):
        super(GoalkeeperWindow, self).__init__()

        print("body of goalkeeper window")

        # self.resize(500, 500)

        self.setWindowTitle(title)

        # ____________RANDOM PLAYER CONTENT__________
        self.externalLayout = QVBoxLayout()

        

        self.externalLayout.addWidget(self.createRandomGroup(title,data))
        self.externalLayout.addWidget(self.createContendentButtonsGroup(data))
        self.externalLayout.addWidget(self.createUtilityButtonsGroup())
        self.setLayout(self.externalLayout)




    # _________METHODS FOR VREATE GUI GROUPS___________________
    def createRandomGroup(self,title,data):
        self.randomGroup = QGroupBox('random player')

        self.randomButton = QPushButton()
        self.randomButton.setText('random ' + title)
        self.randomPlayerText = QLabel('pozzo')

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.randomButton)
        self.vBox.addWidget(self.randomPlayerText)
        
        self.randomGroup.setLayout(self.vBox)

        self.randomButton.clicked.connect(data.randomPick('P'))
        return self.randomGroup

    def createContendentButtonsGroup(self,data):
        self.contendentGroup = QGroupBox('insert player in contender teams')
        self.GBox = QGridLayout()

        for name in data.contenderNames:
            self.contenderButton = QPushButton(name)
            self.contenderButton.setText(name)
            self.GBox.addWidget(self.contenderButton)
        
        self.contendentGroup.setLayout(self.GBox)
        return self.contendentGroup

    def createUtilityButtonsGroup(self):
        self.utilityGroup = QGroupBox('')

        self.backOneButton = QPushButton()
        self.backOneButton.setText('back one')
        self.discardsButton = QPushButton()
        self.discardsButton.setText('restore discards')
        self.saveButton = QPushButton()
        self.saveButton.setText('save')
        
        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.backOneButton)
        self.hBox.addWidget(self.discardsButton)
        self.hBox.addWidget(self.saveButton)
        
        self.utilityGroup.setLayout(self.hBox)
        return self.utilityGroup



class selectRolePage(QtWidgets.QWizardPage):
    

    def __init__(self, *args, **kwargs):
        super(selectRolePage, self).__init__(*args, **kwargs)

        # AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF = self.divideForRole(self.playersData)
        # roleList = [AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF]
        

        # ____CREATE WIDGET____
        self.titleRole = QLabel("Choose a role to start auction:")

        self.GoalkeeperButton = QPushButton()
        self.GoalkeeperButton.setText("Goalkeeper")

        self.DefenderButton = QPushButton()
        self.DefenderButton.setText("Defender")

        self.midfielderButton = QPushButton()
        self.midfielderButton.setText("midfielder")

        self.forwardButton = QPushButton()
        self.forwardButton.setText("forward")

        self.GoalkeeperButton.clicked.connect(self.GoalkeeperButtonOpenWindow)
        # self.DefenderButton.clicked(self.DefenderButtonOpenWindow)
        # self.midfielderButton.clicked(self.midfielderButtonOpenWindow)
        # self.forwardButton.clicked(self.forwardButtonOpenWindow)

        

        # ____MODIFY DEFAULT BUTTONS____
        # self.setButtonText()

        # ____ADD WIDGET TO LAYOUT____
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.titleRole)
        self.layout.addWidget(self.GoalkeeperButton)
        self.layout.addWidget(self.DefenderButton)
        self.layout.addWidget(self.midfielderButton)
        self.layout.addWidget(self.forwardButton)

        self.setLayout(self.layout)

    def nextId(self):
        # return the id of the next page, retrun 3 because Wizard.class1 has problems
        return 3
        # return Wizard.class3

    @Slot()  
    def GoalkeeperButtonOpenWindow(self):
        print("entra in goalkeeper button_______________")
        self.GoalkeeperW = GoalkeeperWindow('Goalkeeper',self.wizard().data)
        self.GoalkeeperW.show()
        # self.exit(GoalkeeperW.exec_())


    # def DefenderButtonOpenWindow(self):
    # def midfielderButtonOpenWindow(self):
    # def forwardButtonOpenWindow(self):