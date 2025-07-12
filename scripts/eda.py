import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from utils_and_constants import read_data

sns.set_style('darkgrid')

def time_series(df): 
    plt.figure()
    sns.lineplot(x="Date", y="ICCO daily price (US$/tonne)",data=df)
    plt.show()
    
df = read_data('processed_df.csv')
time_series(df)