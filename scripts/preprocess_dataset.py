import pandas as pd
import numpy as np 
from pathlib import Path

def read_data(): 
    '''Reading the data'''
    data_path = Path(__file__).parent.parent / "data" / "Daily_Prices_Home_NEW.csv"
    df = pd.read_csv(data_path)
    return df


def preprocess_data(df): 
    '''General preprocessing, converting columns to the requires data types'''
    df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')

    df['London futures (£ sterling/tonne)'] = df['London futures (£ sterling/tonne)'].str.replace(',', '')
    df['London futures (£ sterling/tonne)'] = df['London futures (£ sterling/tonne)'].astype(float)

    df['New York futures (US$/tonne)'] = df['New York futures (US$/tonne)'].str.replace(',', '')
    df['New York futures (US$/tonne)'] = df['New York futures (US$/tonne)'].astype(float)

    df['ICCO daily price (US$/tonne)'] = df['ICCO daily price (US$/tonne)'].str.replace(',', '')
    df['ICCO daily price (US$/tonne)'] = df['ICCO daily price (US$/tonne)'].astype(float)

    df['ICCO daily price (Euro/tonne)'] = df['ICCO daily price (Euro/tonne)'].str.replace(',', '')
    df['ICCO daily price (Euro/tonne)'] = df['ICCO daily price (Euro/tonne)'].astype(float)
    
    return df

def save_preprocessed_data(df): 
    '''Saving the preprocessed the data folder'''
    save_path = Path(__file__).parent.parent / "data" / "processed_df.csv"
    df.to_csv(save_path)
    return df

df = read_data()
preprocessed_df = preprocess_data(df)
save_preprocessed_data(preprocessed_df)
