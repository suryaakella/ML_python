import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
games = pd.read_csv('/home/surya/Documents/ml_projects/board_game_prediction/games.csv')
# Remove any rows without user reviews.
games = games[games["users_rated"] > 0]
# Remove any rows with missing values.
games = games.dropna(axis=0)
# Get all the columns from the dataframe.

y = games['average_rating']
X = games.drop(columns = ["bayes_average_rating", "average_rating", "type", "name", "id"])
from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(X, y, test_size = 0.2)
print('x_train',x_train.shape)
print('x_test',x_test.shape)
print('y_train',y_train.shape)
print('y_test',y_test.shape)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# polynomial regression
poly = PolynomialFeatures(degree = 1)
x_poly_train = poly.fit_transform(x_train)
x_poly_test = poly.fit_transform(x_test)
model = LinearRegression()
model.fit(x_poly_train, y_train)
predictions = model.predict(x_poly_test)
print(mean_squared_error(np.array(y_test), np.array(predictions)))

# linear regression
model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(mean_squared_error(np.array(y_test), np.array(predictions)))
#
# # support vector regression
# from sklearn.svm import SVR
# model = SVR(kernel='rbf')
# model.fit(x_train, y_train)
# predictions = model.predict(x_test)
# print(mean_squared_error(np.array(y_test), np.array(predictions)))

# decision tree regressor
from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(mean_squared_error(np.array(y_test), np.array(predictions)))

# random forest regressor
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 100)
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(mean_squared_error(np.array(y_test), np.array(predictions)))
