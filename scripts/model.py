import pandas as pd 
import numpy as np 
from utils_and_constants import read_data

import mlflow

from sklearn.linear_model import LinearRegression

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

uri = mlflow.get_tracking_uri()
mlflow.set_tracking_uri(uri)
mlflow.set_experiment("Cocoa_price_prediction")

df = read_data('processed_df.csv','')
X = df[['Price_Lag1', 'Price_Lag2', 'MA_7']]
y = df['ICCO daily price (US$/tonne)']
#model = LinearRegression().fit(X, y)

mlflow.start_run()





