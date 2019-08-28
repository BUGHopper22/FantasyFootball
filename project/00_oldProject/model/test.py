

import pandas as pd
from roleLists import  roleLists

# import model.roleLists as r
# from model.fantacalcioModel import AuctionData

if __name__ == "__main__":
    print("this is main")

    # SETTER FUNZIONANO_______________________OK
    roleIstance = roleLists()
    goalkeeperPath = '../data/testData/Quotazioni_Fantacalcio.csv'
    defenderPath = '../data/testData/Quotazioni_Fantacalcio.csv'
    midfielderPath = '../data/testData/Quotazioni_Fantacalcio.csv'
    forwardPath = '../data/testData/Quotazioni_Fantacalcio.csv'
    roleIstance.setGoalkeeper(goalkeeperPath)
    roleIstance.setDefender(defenderPath)
    roleIstance.setMidfielder(midfielderPath)
    roleIstance.setForward(forwardPath)

    print(roleIstance.goalkeeper)

    # RANDOMPICK METHOD WORK__________________OK
    randomPlayer = roleIstance.randomPick('goalkeeper')
    print(randomPlayer)

    folderPath = '../data/testData/' 
    roleIstance.saveAll(folderPath)

    goalkeeperPath = '../data/testData/goalkeeper.csv'
    roleIstance.setGoalkeeper(goalkeeperPath)
    print(roleIstance.goalkeeper)

