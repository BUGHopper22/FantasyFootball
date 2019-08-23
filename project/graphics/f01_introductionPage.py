
from PySide2 import QtWidgets
from PySide2.QtWidgets import QGroupBox, QHBoxLayout, QRadioButton, QLabel, QComboBox, QPushButton, QVBoxLayout
from PySide2.QtCore import  Signal, Slot

# from graphics.f00_fantacalcioGuiStart import Wizard



class IntroductionPage(QtWidgets.QWizardPage):

    def __init__(self,*args, **kwargs):
        super(IntroductionPage, self).__init__(*args, **kwargs)

        # ____COMBO BOX____
        self.radioButtonsContent = QGroupBox('new auction OR load auction')
        self.radioButtonNew = QRadioButton('new')
        self.radioButtonLoad = QRadioButton('load')

        self.radioHBox = QHBoxLayout()
        self.radioHBox.addWidget(self.radioButtonNew,0)
        self.radioHBox.addWidget(self.radioButtonLoad,1)
        self.radioButtonsContent.setLayout(self.radioHBox)


        self.radioButtonNew.toggled
        self.radioButtonNew.toggled.connect(self.changeViewFromRadio)

        

        # ___________________SELECT NUMBER OF CONTENDER_________________________

        self.newViewContent = QGroupBox('new auction:')
        self.newViewContent.setVisible(False)
        self.titleNumberOfContenders = QLabel('Select number of contenders')
        self.numberOfContenders = QComboBox()
        self.numberOfContenders.addItems(['0','1','2','3','4','5','6','7','8','9','10','11','12'])

        self.newViewBoxLayout = QHBoxLayout()
        self.newViewBoxLayout.addWidget(self.titleNumberOfContenders,0)
        self.newViewBoxLayout.addWidget(self.numberOfContenders,1)
        self.newViewContent.setLayout(self.newViewBoxLayout)

        self.registerField("contenderCount*",self.numberOfContenders)

        # ___________________LOAD DATA_________________________

        self.loadViewContent = QGroupBox('Load data:')
        self.loadViewContent.setVisible(False)
        self.titleLoadData = QLabel("Select folder with save")
        self.loadButton = QPushButton()
        self.loadButton.setText("search saved file")
        
        self.loadViewBoxLayout = QVBoxLayout()
        self.loadViewBoxLayout.addWidget(self.titleLoadData)
        self.loadViewBoxLayout.addWidget(self.loadButton)
        self.loadViewContent.setLayout(self.loadViewBoxLayout)

        # ___Add Elements to layout___
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.radioButtonsContent)
        self.layout.addWidget(self.newViewContent)
        self.layout.addWidget(self.loadViewContent)

        

        self.setLayout(self.layout)


    def checkableNew(self):
        self.newViewContent.setVisible(True)
        self.loadViewContent.setVisible(False)

    def checkableLoad(self):
        self.newViewContent.setVisible(False)
        self.loadViewContent.setVisible(True)

    @Slot()  
    def loadDataClicked(self):
        print("newAuctionSetted to False")

    @Slot()  
    def changeViewFromRadio(self,IsRadioButtonNew):
        if IsRadioButtonNew:
            print("new RadioButton clicked")
            self.checkableNew()
        else:
            print("load RadioButton clicked")
            self.checkableLoad()
        

    def nextId(self):
        # return the id of the next page, retrun 1 because Wizard.class1 has problems
        if self.radioButtonNew.isChecked():
            return 1
        else:
            return 2
        # return Wizard.class1