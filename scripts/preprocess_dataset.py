import pandas as pd
import numpy as np 
from pathlib import Path

data_path = Path(__file__).parent.parent / "data" / "Daily_Prices_Home_NEW.csv"

df = pd.read_csv(data_path)
df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')

df['London futures (£ sterling/tonne)'] = df['London futures (£ sterling/tonne)'].str.replace(',', '')
df['London futures (£ sterling/tonne)'] = df['London futures (£ sterling/tonne)'].astype(float)

df['New York futures (US$/tonne)'] = df['New York futures (US$/tonne)'].str.replace(',', '')
df['New York futures (US$/tonne)'] = df['New York futures (US$/tonne)'].astype(float)

df['ICCO daily price (US$/tonne)'] = df['ICCO daily price (US$/tonne)'].str.replace(',', '')
df['ICCO daily price (US$/tonne)'] = df['ICCO daily price (US$/tonne)'].astype(float)

df['ICCO daily price (Euro/tonne)'] = df['ICCO daily price (Euro/tonne)'].str.replace(',', '')
df['ICCO daily price (Euro/tonne)'] = df['ICCO daily price (Euro/tonne)'].astype(float)
