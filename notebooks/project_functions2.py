import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pylab as plt
def load_and_process(path='../data/raw/Total_Precitation.csv'): 
    """ This creates a new dataframe for historic data, removes NaN values, 
    and replaces "DateTime" with "Year"""
    Historic = (
         pd.read_csv('../data/raw/Total_Precitation.csv')
        .loc[0:55]
        .dropna(axis='columns', how ='any')
        .assign(Year = lambda x: range(1950,2006))
        .drop("DateTime", 1)
)
    """ This creates a new dataframe for future data, removes NaN values, 
    and replaces "DateTime" with "Year"""
    Future = (
         pd.read_csv('../data/raw/Total_Precitation.csv')
        .loc[55:151]
        .dropna(axis='columns', how ='any')  
        .assign(Year = lambda x: range(2005,2101))
        .drop("DateTime", 1)
)
    return (Historic, Future)