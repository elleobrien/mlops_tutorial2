from sklearn.datasets import make_regression
import pandas as pd
import os
import numpy as np

# If there's no dataset in the project directory, create a reasonably large one. 
# If it exists, append some new observations. 
if os.path.isfile("data.csv"):
    n = 1
else:
    n = 50

for i in range(0,n):    
    X, y = make_regression(10000,n_features = 10)
    df = pd.DataFrame(X)
    df.to_csv("data.csv",mode='a')
