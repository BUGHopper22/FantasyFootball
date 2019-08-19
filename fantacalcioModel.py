
import pandas as pd

class contenderTeamList():
    contenderList = []

    def __init__(self,newAuction):
        # load data from csv, else build void list
        if not newAuction:
            insertCvsInList(newAuction)

    def insertCvsInList(self):
        contenderList = pd.read_csv('./data/contenderTeam1.csv')

    def showList():
        print(contenderList)


class PlayerToChooseList():
    playersData = pd.read_csv('./data/Quotazioni_Fantacalcio.csv')
