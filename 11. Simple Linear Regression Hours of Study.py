#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import pandas for data processing
import pandas as pd

#read the csv file
dataset=pd.read_csv('01Students.csv')
df=dataset.copy()

#split into x (independent) and y (Predicted)
x=df.iloc[:,:-1]
y=df.iloc[:, -1]

#create the training and test datasets
from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test=train_test_split(x,y,test_size = 0.4,random_state=1234)

#train the simple Linear Regression
from sklearn.linear_model import LinearRegression
std_reg=LinearRegression()
std_reg.fit(x_train, y_train)

#predict the results
y_predict=std_reg.predict(x_test)

#get the R_squared
slr_score=std_reg.score(x_test, y_test)

#coefficient and intercept
slr_coefficient=std_reg.coef_
slr_intercept=std_reg.intercept_

#equation of the line
# y=34.27 + 5.02 * x

#calculate the errors using RMSE
from sklearn.metrics import mean_squared_error 
import math
slr_rmse = math.sqrt(mean_squared_error (y_test, y_predict))

#Plot the result using matplotlib
import matplotlib.pyplot as plt
plt.scatter(x_test,y_test)
plt.plot(x_test, y_predict)
plt.ylim(ymin = 0)
plt.show()


# In[ ]:





# In[ ]:




