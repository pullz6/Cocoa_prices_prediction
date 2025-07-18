import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from utils_and_constants import read_data,save_plot
from pathlib import Path

sns.set_style('darkgrid')

def time_series(df,save): 
    '''Create a scatter plot for the prices'''
    plt.figure()
    sns.lineplot(x="Date", y="ICCO daily price (US$/tonne)",data=df)
    sns.lineplot(x="Date", y="London futures (£ sterling/tonne)",data=df)
    sns.lineplot(x="Date", y="New York futures (US$/tonne)",data=df)
    if save ==True: 
        save_plot('time_series')
    plt.show()
  
df = read_data('processed_df.csv','')
time_series(df,save=True)