import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


#generating random data set
np.random.seed(0) 
#np.random.seed(0) makes
#the random numbers predictable

x = np.random.rand(100,1)
y = 2+3*x +np.random.rand(100,1)

#sci-kit implementation

#Model initialization

regression_model = LinearRegression()

#Fit the data(train the model)

regression_model.fit(x,y)

#predicting

y_predicted = regression_model.predict(x)

#model evaluation
rmse = mean_squared_error(y , y_predicted)
r2 = r2_score(y,y_predicted)

#printing values
print("Slope : ", regression_model.coef_)
print("Intercept : ", regression_model.intercept_)
print("Root mean sqaured error : " , rmse)
print("R2 score : ", r2)

#plot

#data points
plt.scatter(x,y,s=10)
plt.xlabel('x')
plt.ylabel('y')

#predicted values
plt.plot(x,y_predicted,color = "r")
plt.show()



