import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#importing the data

train = pd.read_csv(r"C:\Users\USER\Downloads\train.csv")
test = pd.read_csv(r"C:\Users\USER\Downloads\test.csv")

#feature selection

y = train.SalePrice

feautures = ["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd"]
