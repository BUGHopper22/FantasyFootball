import csv
import os
import pandas as pd

if __name__ == "__main__":
    l = ['Alberto','Alessio','Gezzim']
    d = {'name':l}
    p = pd.DataFrame(data=d)
    if os.path.exists('contendersNames.csv'):  
        os.remove("contendersNames.csv")
    print(p)
    
    p.to_csv('contendersNames.csv',index=False)

    # with open('contendersNames.csv','w', newline='') as w:
    #     a = csv.writer(w,delimiter=',')
    #     a.writerows(l)

    # with open('contendersNames.csv', "wb") as csv_file:
    #     writer = csv.writer(csv_file, delimiter=',')
    #     for line in l:
    #         print(line)
    #         writer.writerow(line)
