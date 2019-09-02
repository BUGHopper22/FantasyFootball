
from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox, QLabel, QComboBox, QHBoxLayout, QLineEdit, QGridLayout

class contenderPage(QWidget):
    
    # QLineEdit widget inside
    lineEditInfo = []
    # QLineEdit text inside
    lineEditText = []

    def __init__(self,fantasyFootball):
        super(contenderPage, self).__init__()

        self.fantasyFootball = fantasyFootball

        # FIRST BOX
        self.newViewContent = QGroupBox('contender numbers')
        self.titleNumberOfContenders = QLabel('Select number of contenders')
        self.numberOfContenders = QComboBox()
        self.numberOfContenders.addItems(['0','1','2','3','4','5','6','7','8','9','10','11','12'])

        self.newViewBoxLayout = QHBoxLayout()
        self.newViewBoxLayout.addWidget(self.titleNumberOfContenders,0)
        self.newViewBoxLayout.addWidget(self.numberOfContenders,1)
        self.newViewContent.setLayout(self.newViewBoxLayout)

        # SECOND BOX
        self.nameViewContent = QGroupBox('contender names')

        self.nameBoxLayout = QGridLayout()
        self.numbers = 0
        self.numberOfContenders.currentIndexChanged.connect(self.numberOfContendersAction)

        # THIRD BOX

        self.utilityViewContent = QGroupBox('')
        self.contenderFinishButton = QPushButton('Start')
        self.contenderBackButton = QPushButton('Back')

        self.utilityViewBoxLayout = QHBoxLayout()
        self.utilityViewBoxLayout.addWidget(self.contenderBackButton,0)
        self.utilityViewBoxLayout.addWidget(self.contenderFinishButton,1)
        self.utilityViewContent.setLayout(self.utilityViewBoxLayout)

        self.contenderFinishButton.clicked.connect(self.finishAction)


        # MAIN LAYOUT
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.newViewContent)
        self.layout.addWidget(self.nameViewContent)
        self.layout.addWidget(self.utilityViewContent)
        self.setLayout(self.layout)

    def numberOfContendersAction(self,id):
        self.numbers = id



        self.createLineEdit(self.numbers)




    def createLineEdit(self,maxLim):

        if self.nameBoxLayout is not None: 
            while self.nameBoxLayout.count(): 
                item = self.nameBoxLayout.takeAt(0) 
                widget = item.widget() 
                if widget is not None: 
                    widget.deleteLater()
                    print('delete') 
                # else: 
                #     deleteItems(item.layout()) 
        self.lineEditInfo.clear()


        # child = self.nameBoxLayout.takeAt(0)
        # while child:
            
        #     print(child)
        #     print(self.nameBoxLayout.count())
        #     del child
        #     child = self.nameBoxLayout.takeAt(0)
        
        for self.lineEditIndex in range(1, maxLim+1 ):
            print('Creating line edit')

            lineEditTitle = 'contender Name ' + str(self.lineEditIndex)
            self.fieldName = 'contender' + str(self.lineEditIndex)

            self.actualLineEdit = QLineEdit()

            self.nameBoxLayout.addWidget(QLabel(lineEditTitle),
                                    self.lineEditIndex,
                                    0)

            self.nameBoxLayout.addWidget(self.actualLineEdit,self.lineEditIndex,1)
            
            
            self.lineEditInfo.append(self.actualLineEdit)
        self.nameViewContent.setLayout(self.nameBoxLayout)
        print(self.lineEditInfo)

    def finishAction(self):
        # insert QLineEdit tex inside list
        for i in range(0,len(self.lineEditInfo)):
            self.lineEditText.append(self.lineEditInfo[i].text()) 
        print(self.lineEditText)
        self.fantasyFootball.setContendersNames(self.lineEditText)

        

