from PySide2 import QtWidgets
from PySide2.QtWidgets import QWizard 
from PySide2.QtCore import  Signal, Slot, QObject
from .f01_introductionPage import IntroductionPage
from .f02_contenderNamePage import contenderNamePage
from .f03_selectRolePage import selectRolePage
from .f04_randomPickPage import randomPickPage
from model.fantacalcioModel import AuctionData



class Wizard(QtWidgets.QWizard):
    

    num_of_pages = 5
    # self.intro == 0, self.class1 == 1 ecc
    (intro, class1, class2, class3, conclusion) = range(num_of_pages)
    
    # AuctionData(True) build auctionData with default value
    data = AuctionData()

    def __init__(self, *args, **kwargs):
        
        super(Wizard, self).__init__()

        

        self.setOption(QWizard.NoCancelButton)
        self.setOption(QWizard.DisabledBackButtonOnLastPage)

        # IDSWizard = intro, class1, class2, class3, conclusion
        # setPage(id,page)
        self.setPage(self.intro, IntroductionPage(self))
        self.setPage(self.class1, contenderNamePage(self))
        self.setPage(self.class2, selectRolePage(self))
        self.setPage(self.class3, randomPickPage(self))


        # EXAMPLE TO CONNECT SIGNALBUTTON OF PAGES
        # self.page(self.intro).completeChanged.connect(self.slotIntroToPage1)

        
        # ____ATTENZIONE:
        #       ID==0 EMESSO SEGNALE ALLO START
        #       ID==2 EMESSO SEGNALE DALLA PAGEINTRO ALLA PAGE 1   
        self.currentIdChanged
        self.currentIdChanged.connect(self.slotChangePage)
        

    @Slot()  
    def slotChangePage(self,id):
        print("ENTRA")
        print(self.currentPage())
        if(id==0):
            print("___slot start to intro___")
            # print(self.currentPage())
            
            
        if(id==1):
            print("___slot intro To page1___")
            # print(self.currentPage())
            # createLineEdit is a method to create line edit in page 1
            self.currentPage().createLineEdit(self.field("contenderCount"))
            
        if(id==2):
            print("___slot page1 To page2___")
            
            # 1/4 insert data in contendersName
            for i in range(1,self.field('contenderCount')+1):
                print('contender' + str(i))
                print(self.field( 'contender' + str(i)))
                self.data.contenderNames.append(self.field( 'contender' + str(i))) 
            
            # 2/4 insert data in contenderTeams
            for name in self.data.contenderNames:
                self.data.contenderTeams[name] = []

            # 3/4 insert data in contenderTeams
            self.data.insertDataInDictionaryListForRole()

            print('1_______________________________1')
            print(self.data.playersRemainDF)
            print('2_______________________________2')
            print(self.data.dictionaryListForRole)
            print('3_______________________________3')
            print(self.data.contenderTeams)
            print('4_______________________________4')
            print(self.data.contenderNames)


    def insertContenderNameList(self):
        listC = []
        for i in range(1,self.field("contenderCount")):
            listC.append(self.field('contender' + str(i)))
        return listC
    

