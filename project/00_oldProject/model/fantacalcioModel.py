
import pandas as pd

class AuctionData():

    # dataframe con tutti i players ancora da scegliere
    playersRemainDF = []
    # DictionaryListForRole = {'attaccanti':{DFAttaccanti},'Difensori':{DFDifensori}}
    dictionaryListForRole ={}
    # lista contenente i teams dei contenders {'contender1':{team1},'contender2':{team2}}
    contenderTeams = {}
    # lista con i nomi dei contenders
    contenderNames = []


    def randomPick(self, role):
        idsSeries = self.dictionaryListForRole[role]['Id']
        # serie with random Id as value
        randomIdFromSerie = idsSeries.sample(n=1)

        # random id as integer
        randomID = randomIdFromSerie.iloc[0]

        # single line dataframe with picked player
        playerPicked = self.dictionaryListForRole[role].loc[self.dictionaryListForRole[role]['Id'] == randomID]
    
        print(playerPicked)

        # drop line of singleRoleDF where Id == randomID
        SingoloRuoloIdColDF = self.dictionaryListForRole[role].set_index("Id")
        SingoloRuoloIdColDF = SingoloRuoloIdColDF.drop(randomID, axis=0)

        

    def insertDataInDictionaryListForRole(self):
        GoalkeeperDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='P']
        DefenderDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='D']
        midfielderDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='C']
        forwardDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='A']
        
        self.dictionaryListForRole = {  'Goalkeeper': GoalkeeperDF, 
                                        'Defender': DefenderDF,
                                        'midfielder': midfielderDF,
                                        'forward': forwardDF }

    def insertDataInContenderTeams(self,folderNameToLoad,contenderNames):
        for contenderName in contenderNames:
            
            print('contenderName')
            print(contenderName)
            # prende dal file pippo.csv il df col team di pippo
            singleContenderTeamDF = pd.read_csv('./data/'+ folderNameToLoad +'/' + contenderName + '.csv')
            self.contenderTeams[contenderName] = singleContenderTeamDF


    # def SETTER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def __init__( self,folderNameToLoad = '', contenderNames = []):
        # if isDefault is 'default' => start a new auction, else load data from defaultValue folder
        if (folderNameToLoad == ''):
            self.playersRemainDF = pd.read_csv('./data/default/Quotazioni_Fantacalcio.csv')
            # test if it works
            self.insertDataInDictionaryListForRole() # self.DictionaryListForRole = self.divideForRole(playersRemainDF)
            self.contenderTeams = {}
            self.contenderNames = []
        else:
            self.playersRemainDF = pd.read_csv('./data/' + folderNameToLoad + '/Quotazioni_Fantacalcio.csv')
            self.insertDataInDictionaryListForRole()
            self.contenderNames = contenderNames
            self.insertDataInContenderTeams(folderNameToLoad,contenderNames)


    # def insertCvsInList(self):
    #     contenderList = pd.read_csv('../data/contenderTeam1.csv')

if __name__ == "__main__":
    print('start')
    # TEST(PASSED) : BUILD auctionData WITH DEFAULT CONSTRUCTOR
    # isDefault = True
    # newAuction = AuctionData(isDefault)
    # print(newAuction.playersRemainDF)
    
    # TEST(PASSED) : BUILD auctionData WITHOUT DEFAULT CONSTRUCTOR
    # fakeListName = ['ugo','pippo','kate']
    # fakeFolderName = 'save_1'
    # isDefault = False
    # auctionLoaded = AuctionData(isDefault,fakeFolderName,fakeListName)
    # print(auctionLoaded.contenderTeams)


