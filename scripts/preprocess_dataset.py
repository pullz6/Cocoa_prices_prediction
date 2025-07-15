import pandas as pd
import numpy as np 
from pathlib import Path
from utils_and_constants import read_data

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
    
    df['Price_Lag1'] = df['ICCO daily price (US$/tonne)'].shift(1) 
    df['Price_Lag2'] = df['ICCO daily price (US$/tonne)'].shift(2)
    df['Price_Lag3'] = df['ICCO daily price (US$/tonne)'].shift(3)
    df['Price_Lag4'] = df['ICCO daily price (US$/tonne)'].shift(4)
    df['Price_Lag5'] = df['ICCO daily price (US$/tonne)'].shift(5)
    df['Price_Lag6'] = df['ICCO daily price (US$/tonne)'].shift(6)
    df['Price_Lag7'] = df['ICCO daily price (US$/tonne)'].shift(7)
    
    df['Rolling_Mean_7'] = df['ICCO daily price (US$/tonne)'].rolling(window=7).mean()
    df['Rolling_Std_7'] = df['ICCO daily price (US$/tonne)'].rolling(window=7).std()
    
    df['MA_7'] = df['ICCO daily price (US$/tonne)'].rolling(window=7).mean()
    df['MA_30'] = df['ICCO daily price (US$/tonne)'].rolling(window=30).mean()
    
    return df

def save_preprocessed_data(df): 
    '''Saving the preprocessed the data folder'''
    save_path = Path(__file__).parent.parent / "data" / "processed_df.csv"
    df.to_csv(save_path)
    return df

df = read_data("Daily_Prices_Home_NEW.csv",'raw')
preprocessed_df = preprocess_data(df)
save_preprocessed_data(preprocessed_df)
