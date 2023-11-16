import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#importing the data

train_data = pd.read_csv("train.csv")

y = train_data.SalePrice

features = ["LotArea","YearBuilt"]

X = train_data[features]


#spliting the data to test and train

train_X ,test_X, train_y, test_y = train_test_split(X, y, random_state=1)

rf_model = RandomForestRegressor(random_state=1)

rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(test_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, test_y)

print(" MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))