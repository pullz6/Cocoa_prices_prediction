import pandas as pd 
import numpy as np 
from utils_and_constants import read_data

import mlflow

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

uri = mlflow.get_tracking_uri()
mlflow.set_tracking_uri(uri)
mlflow.set_experiment("Cocoa_price_prediction")

df = read_data('processed_df.csv','')
X = df[['Price_Lag1', 'Price_Lag2','Price_Lag3','Price_Lag4','Price_Lag5','Price_Lag6','Price_Lag7', 'MA_7']]
y = df['ICCO daily price (US$/tonne)']

# Enable autologging for scikit-learn
mlflow.sklearn.autolog()

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

with mlflow.start_run(): 
    model = LinearRegression().fit(X_train, y_train)
    # Evaluation metrics are automatically captured
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    print(f"Training accuracy: {train_score:.3f}")
    print(f"Test accuracy: {test_score:.3f}")






