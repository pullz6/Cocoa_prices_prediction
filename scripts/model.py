import pandas as pd 
import numpy as np 
import json
from utils_and_constants import read_data, save_plot
import matplotlib.pyplot as plt

import mlflow

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

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
    
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Training accuracy: {train_score:.3f}")
    print(f"Test accuracy: {test_score:.3f}")
    print("Mean Absolute Error: ", mae)
    print("Mean Squared Error: ", mse)
    print("R2 Score: ", r2)
    
    eval = {"Training accuracy": train_score,"Test accuracy": test_score,"Mean Absolute Error": mae,"Mean Squared Error": mse,"R2 Score": r2}
    
    with open("metrics/metrics.json", 'w') as f:
        json.dump(eval, f)
    
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs. Predicted Chocolate Prices")
    save_plot('Predictions')
    #plt.show()
    
    residuals = y_test - model.predict(X_test)
    plt.scatter(y_test, residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel("Actual Prices")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    save_plot('residual_plot')
    #plt.show()






