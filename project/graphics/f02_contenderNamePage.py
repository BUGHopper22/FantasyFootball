from PySide2 import QtWidgets
from PySide2.QtWidgets import QGridLayout, QLineEdit, QLabel
from PySide2.QtCore import  Signal, Slot, QObject
# from .f00_fantacalcioGuiStart import Wizard

class contenderNamePage(QtWidgets.QWizardPage):

    # dictionary{'fieldName': QLineEditWidget}
    lineEditInfo = {}

    def __init__(self, *args, **kwargs):
        super(contenderNamePage, self).__init__(*args, **kwargs)

        self.setCommitPage(True)
        
        self.setTitle("Insert names of contenders")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # self.completeChanged

    @Slot()
    def memEditValue(self,textChan):
        print('signal QLineEdit')
        self.setField(self.fieldName,textChan)
        print(self.field(self.fieldName))
        print(self.fieldName)
        

    def createLineEdit(self,maxLim):
        self.initializePage()
        for lineEditIndex in range(1,maxLim+1 ):
            print('Creating line edit')

            lineEditTitle = 'contender Name ' + str(lineEditIndex)
            self.fieldName = 'contender' + str(lineEditIndex)

            self.actualLineEdit = QLineEdit()


            print(self.fieldName )
            print(self.fieldName )
            print(self.fieldName )
            self.registerField(     str(self.fieldName + '*'),
                                    self.actualLineEdit)

            
            self.layout.addWidget(   QLabel(lineEditTitle),
                                    lineEditIndex,
                                    0)

            self.layout.addWidget(self.actualLineEdit,lineEditIndex,1)
            self.lineEditInfo[self.fieldName] = self.actualLineEdit

            self.lineEditInfo[self.fieldName].textEdited
            self.lineEditInfo[self.fieldName].textEdited.connect(self.memEditValue)

    def nextId(self):
        # return the id of the next page, retrun 2 because Wizard.class1 has problems
        return 2
        # return Wizard.class2