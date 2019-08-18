import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, QRectF, Qt,  Signal,Slot


from PySide2.QtWidgets import QWizardPage, QWizard, QMainWindow, QFileDialog, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QProgressBar


class IntroductionPage(QtWidgets.QWizardPage):

    # si = Signal(str)

    def __init__(self,*args, **kwargs):
        super(IntroductionPage, self).__init__(*args, **kwargs)
        
        self.titleIdsButton = QtWidgets.QLabel()
        self.titleIdsButton.setText('Select number of contenders')
        self.numberOfContenders = QtWidgets.QComboBox()
        self.numberOfContenders.addItems(['1','2','3','4','5','6','7','8','9','10','11','12'])

        # ___Add Elements to layout___
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.titleIdsButton)
        self.layout.addWidget(self.numberOfContenders)

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

    def initializePage(self):
        print("you click next button 1")
        # self.si.emit(111)
        

        # self.titleLine.setText = self.field("contenderCount")

    # def initializePage(self):
    #     print("you click next button1111111111111")
    #     print(self.field("contenderCount"))
    #     self.setField("contenderCount",self.numberOfContenders.itemData(self.numberOfContenders.currentIndex()))
        



class ClassesPage1(QtWidgets.QWizardPage):

    temp = 0

    def __init__(self, *args, **kwargs):
        super(ClassesPage1, self).__init__(*args, **kwargs)

        self.setTitle("Insert names of contenders")

        self.layout = QtWidgets.QVBoxLayout()

        temp = self.field("contenderCount")
        print("contenderCount",self.field("contenderCount"))


        if(temp == None):
            temp = 0

        self.createButton(-1)

        

        self.setLayout(self.layout)

    def createButton(self,maxLim):
        self.initializePage()
        for actulaButton in range(1,maxLim+2 ):
            print('Creating line edit')
            self.titleLine = QtWidgets.QLabel()
            self.titleLine.setText('contender Name' + str(actulaButton))

            buttonName = 'contendersNameButton' + str(actulaButton)
            self.buttonName = QtWidgets.QLineEdit()
            self.buttonName.setGeometry(QtCore.QRect(1082, 80, 121, 28))
            self.buttonName.setObjectName("contendersNameButton"+str(actulaButton))
            # self.buttonName.setText(str("contendersNameButton"+str(actulaButton)))

            self.layout.addWidget(self.titleLine)
            self.layout.addWidget(self.buttonName)
            # self.contendersListWidget = contendersListWidget + (self.buttonName,)

    def initializePage(self):
        print("initialPAge 222")
        self.temp = self.field("contenderCount")
    
    def nextId(self):

        return Wizard.class2

# class ClassesPage1(QtWidgets.QWizardPage):

class Wizard(QtWidgets.QWizard):
    

    num_of_pages = 5
    (intro, class1, class2, class3, conclusion) = range(num_of_pages)

    def updateNum(number):
        print('update1')
        contendersNumber = number

    def __init__(self, *args, **kwargs):
        
        super(Wizard, self).__init__()
        
        self.setOption(QtWidgets.QWizard.NoCancelButton)
        self.setOption(QtWidgets.QWizard.DisabledBackButtonOnLastPage)

        # IDSWizard = intro, class1, class2, class3, conclusion
        # setPage(id,page)
        introP = IntroductionPage(self)
        self.setPage(self.intro, introP)

        pageOne = ClassesPage1(self)
        self.setPage(self.class1, pageOne)



        self.page(self.intro).numberOfContenders.currentTextChanged.connect(self.slotP)

    @Slot(str)  
    def slotP(self,param):
        print(type(self.page(self.intro)))
        print("slot")
        print(param)
        self.page(self.class1).createButton(self.page(self.class1).field("contenderCount"))
        # self.page(self.intro).setField("contenderCount",
        #                             self.page(self.intro).numberOfContenders.currentText())





        # collego il segnale ad una funzione
        # QtWidgets.QWizardPage.connect(IntroductionPage,SIGNAL("updateNumbersOfContenders(number)"),self.updateNum())

        # print(self.contendersNumber)
        # print(type(self.contendersNumber))
        
       
        # self.setPage(self.class1, ClassesPage1(self))
        # self.setStartId(self.intro)
    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    wizard = Wizard()

    wizard.setWindowTitle("Fantacalcio")
    wizard.setSideWidget(None)
    wizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
    wizard.show()

    sys.exit(app.exec_())