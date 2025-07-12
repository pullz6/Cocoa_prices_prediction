import pandas as pd 
import numpy as np 
from pathlib import Path


def read_data(name): 
    '''Reading the data'''
    data_path = Path(__file__).parent.parent / "data" / name
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'],format='ISO8601')
    return df
