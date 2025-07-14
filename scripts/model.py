import pandas as pd 
import numpy as np 

import mlflow

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.start_run()



