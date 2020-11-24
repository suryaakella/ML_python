import pandas as pd
import numpy as np
import sklearn
file = pd.read_csv('games.csv')
y = file['average_rating']
X = file.drop(columns = 'average_rating')
print(X.shape)
print(y.shape)
