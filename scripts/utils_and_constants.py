import pandas as pd 
import numpy as np 
from pathlib import Path


def read_data(name,type): 
    '''Reading the data'''
    data_path = Path(__file__).parent.parent / "data" / name
    df = pd.read_csv(data_path)
    if type=='raw': 
        df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')
    else:
        df['Date'] = pd.to_datetime(df['Date'],format='ISO8601')
    return df
