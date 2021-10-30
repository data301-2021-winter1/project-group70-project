#step 3
import pandas as pd
def cleanYear(data):
    i=1950
    for x in range(151):
        data['Year'][x]=i
        i=i+1
    return data
def load_and_process(path='../data/raw/Hottest_Day.csv' ):
    # Method Chain 1 (hist data processing)

    hist= (
         pd.read_csv(path)
      
           [0:55]
            .dropna(axis='columns',how='all')
            .drop(columns=["Historical Range (high)","Historical Range (low)"])
      
      )

    # Method Chain 2 (projected data processing)

    proj= (
         
          pd.read_csv(path='../data/raw/Hottest_Day.csv')
      
           [56:151]
            .dropna(axis='columns',how='all')
            .drop(columns=["RCP 8.5 Range (high)","RCP 8.5 Range (low)","RCP 4.5 Range (high)","RCP 4.5 Range (low)","RCP 2.6 Range (high)","RCP 2.6 Range (low)"])
        
      )
    hist=cleanYear(hist)
    proj=cleanYear(proj)
return (hist, proj) 

