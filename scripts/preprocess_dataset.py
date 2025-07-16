import pandas as pd
import numpy as np 
from pathlib import Path
from utils_and_constants import read_data

def preprocess_data(df): 
    # Step 1: Drop rows with missing dates
    df = df[df['Date'].notna()].copy()  # Explicit copy to avoid warnings
    
    # Step 2: Convert date first
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    
    # Step 3: Clean numeric columns (remove commas, convert to float)
    numeric_cols = [
        'London futures (£ sterling/tonne)',
        'New York futures (US$/tonne)',
        'ICCO daily price (US$/tonne)',
        'ICCO daily price (Euro/tonne)'
    ]
    for col in numeric_cols:
        df[col] = df[col].str.replace(',', '').astype(float)
    
    # Step 4: Create lag/rolling features (BEFORE filling NaNs)
    df['Price_Lag1'] = df['ICCO daily price (US$/tonne)'].shift(1)
    # ... (add other lags)
    
    df['Rolling_Mean_7'] = df['ICCO daily price (US$/tonne)'].rolling(window=7).mean()
    df['Rolling_Std_7'] = df['ICCO daily price (US$/tonne)'].rolling(window=7).std()
    df['MA_7'] = df['ICCO daily price (US$/tonne)'].rolling(window=7).mean()
    df['MA_30'] = df['ICCO daily price (US$/tonne)'].rolling(window=30).mean()
    
    # Step 5: Fill remaining NaNs (if needed)
    df.fillna(0, inplace=True)  # Or use df.dropna() to remove rows with missing values
    
    return df

def save_preprocessed_data(df): 
    '''Saving the preprocessed the data folder'''
    save_path = Path(__file__).parent.parent / "data" / "processed_df.csv"
    df.to_csv(save_path)
    return df

df = read_data("Daily_Prices_Home_NEW.csv",'raw')
preprocessed_df = preprocess_data(df)
save_preprocessed_data(preprocessed_df)
