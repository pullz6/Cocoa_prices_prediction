import pandas as pd 
import numpy as np 

import mlflow

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

uri = mlflow.get_tracking_uri()
mlflow.set_tracking_uri(uri)

mlflow.set_experiment("Cocoa_price_prediction")

#mlflow.start_run()



