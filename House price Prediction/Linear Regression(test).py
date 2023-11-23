#importing libraries
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x = np.random.rand(100,1)
y = 2*x + 1 + 0.1*np.random.rand(100,1)

x_train ,x_test , y_train , y_test = train_test_split(x,y, test_size=0.2,random_state=42)

model =LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)

print("coefficients:", model.coef_)
print("mean squared  mean:", mse)

plt.plot(x_train,y_train)

