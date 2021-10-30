import pandas as pd
def cleanYear(data):
    i=1950
    for x in range(151):
        data['Year'][x]=i
        i=i+1
    return data
def load_and_process(path):
    past=(
        pd.read_csv(path)
        .iloc[:55]
        .dropna(axis='columns', how='any')
        .rename(columns={"DateTime": "Year"})
    )
    future1=(
        pd.read_csv(path)
        .iloc[56:151]
        .dropna(axis='columns', how='any')
        .rename(columns={"DateTime": "Year"})
    )
    future2=(
        future1
        .assign(Comparison=future1['RCP 8.5 Median']-future1['RCP 2.6 Median'])
    )
    past=cleanYear(past)
    future=cleanYear(future2)
    return (past,future2)