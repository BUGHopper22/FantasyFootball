import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, QRectF, Qt,  Signal,Slot


from PySide2.QtWidgets import QPushButton, QLineEdit, QLabel, QGridLayout, QWizardPage, QWizard, QMainWindow, QFileDialog, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QProgressBar
import pandas as pd

class IntroductionPage(QtWidgets.QWizardPage):

    def __init__(self,*args, **kwargs):
        super(IntroductionPage, self).__init__(*args, **kwargs)
        # ___________________NEW AUCTION_________________________
        self.titleNewAuction = QLabel("New auction:")
        self.titleNumberOfContenders = QLabel('Select number of contenders')
        self.numberOfContenders = QtWidgets.QComboBox()
        self.numberOfContenders.addItems(['1','2','3','4','5','6','7','8','9','10','11','12'])

        # ___________________LOAD DATA_________________________
        self.titleLoadData = QLabel("Load data:")
        self.file_Select_Btn = QPushButton()
        # self.file_Select_Btn.setGeometry(QtCore.QRect(1082, 80, 121, 28))
        self.file_Select_Btn.setObjectName("file_Select_Btn")
        self.file_Select_Btn.setText("search saved file")

        # ___Add Elements to layout___
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.titleNewAuction)
        self.layout.addWidget(self.titleNumberOfContenders)
        self.layout.addWidget(self.numberOfContenders)
        self.layout.addWidget(self.titleLoadData)
        self.layout.addWidget(self.file_Select_Btn)

        

        self.registerField("contenderCount*",
                            self.numberOfContenders)
                            # ,
                            # self.numberOfContenders.itemData(self.numberOfContenders.currentIndex()),
                            # "currentTextChanged")

        self.numberOfContenders.currentTextChanged
        
        # self.numberOfContenders.editTextChanged.connect(lambda: self.setField('contenderCount*',self.numberOfContenders))
        self.setLayout(self.layout)

        
    def nextId(self):
        return Wizard.class1

    # def initializePage(self):
    #     print("you click next button 1")



class ClassesPage1(QtWidgets.QWizardPage):

    lineEditNameList = []

    def __init__(self, *args, **kwargs):
        super(ClassesPage1, self).__init__(*args, **kwargs)

        self.setCommitPage(True)

        self.setTitle("Insert names of contenders")

        # self.layout = QtWidgets.QVBoxLayout()
        self.layout = QGridLayout()
        

        temp = self.field("contenderCount")
        print("contenderCount",self.field("contenderCount"))

        self.createLineEdit(-1)

        self.setLayout(self.layout)

        # emit signal when NEXT button is clicked
        self.completeChanged


    def createLineEdit(self,maxLim):
        self.initializePage()
        for lineEditIndex in range(0,maxLim+1 ):
            print('Creating line edit')

            # self.lineEditName = 'contendersNameButton' + str(lineEditIndex)
            self.lineEditName = QLineEdit()

            self.layout.addWidget(   QLabel('contender Name ' + str(lineEditIndex)),
                                    lineEditIndex,
                                    0)
            
            self.layout.addWidget(self.lineEditName,lineEditIndex,1)

            self.lineEditNameList.append('contender Name ' + str(lineEditIndex))

        


    # def initializePage(self):
    #     print("ENTRAAAA")
        # lineEditName is the name of the element lineEdit
        # for lineEditEl in self.lineEditNameList:
        #     print(lineEditEl + "*")
        #     self.registerField(lineEditEl + "*",self.lineEditEl)



    # def initializePage(self):
    #     print("initialPAge 222")
    #     self.temp = self.field("contenderCount")
    
    def nextId(self):
        return Wizard.class2


class ClassesPage2(QtWidgets.QWizardPage):
    playersData = pd.read_csv('./data/Quotazioni_Fantacalcio.csv')
    AttaccantiDF = {} 
    CentrocampistiDF = {} 
    PortieriDF = {}
    DifensoriDF = {}
    roleList = []
    

    def __init__(self, *args, **kwargs):
        super(ClassesPage2, self).__init__(*args, **kwargs)

        AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF = self.divideForRole(self.playersData)
        roleList = [AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF]
        

        self.titleRole = QLabel("Choose a role to start auction:")

        self.GoalkeeperButton = QPushButton()
        self.GoalkeeperButton.setText("Goalkeeper")

        self.DefenderButton = QPushButton()
        self.DefenderButton.setText("Defender")

        self.midfielderButton = QPushButton()
        self.midfielderButton.setText("midfielder")

        self.forwardButton = QPushButton()
        self.forwardButton.setText("forward")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.titleRole)
        self.layout.addWidget(self.GoalkeeperButton)
        self.layout.addWidget(self.DefenderButton)
        self.layout.addWidget(self.midfielderButton)
        self.layout.addWidget(self.forwardButton)

        self.setLayout(self.layout)

    def nextId(self):
        return Wizard.class3

    def divideForRole(self,playersData):
        AttaccantiDF =playersData.loc[playersData['R']=='A']
        CentrocampistiDF =playersData.loc[playersData['R']=='C']
        PortieriDF =playersData.loc[playersData['R']=='P']
        DifensoriDF = playersData.loc[playersData['R']=='D']
        
        return AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF


class ClassesPage3(QtWidgets.QWizardPage):

    def __init__(self, *args, **kwargs):
        super(ClassesPage3, self).__init__(*args, **kwargs)

    

class Wizard(QtWidgets.QWizard):
    

    num_of_pages = 5
    (intro, class1, class2, class3, conclusion) = range(num_of_pages)

    # def updateNum(number):
    #     print('update1')
    #     contendersNumber = number

    def __init__(self, *args, **kwargs):
        
        super(Wizard, self).__init__()
        
        self.setOption(QtWidgets.QWizard.NoCancelButton)
        self.setOption(QtWidgets.QWizard.DisabledBackButtonOnLastPage)

        # IDSWizard = intro, class1, class2, class3, conclusion
        # setPage(id,page)
        
        self.setPage(self.intro, IntroductionPage(self))
 
        self.setPage(self.class1, ClassesPage1(self))

        self.setPage(self.class2, ClassesPage2(self))

        self.setPage(self.class3, ClassesPage3(self))



        self.page(self.intro).numberOfContenders.currentTextChanged.connect(self.slotIntroToPage1)
        self.page(self.class1).completeChanged.connect(self.slotPage1ToPage2)

    @Slot(str)  
    def slotIntroToPage1(self,param):
        print("slot")
        print(type(self.page(self.intro)))
        print(param)
        self.page(self.class1).createLineEdit(self.page(self.class1).field("contenderCount"))

    @Slot()  
    def slotPage1ToPage2(self):
        print("HAI  CLICCATO SU NEXT")
    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    wizard = Wizard()

    wizard.setWindowTitle("Fantacalcio")
    wizard.setSideWidget(None)
    wizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
    wizard.show()

    sys.exit(app.exec_())