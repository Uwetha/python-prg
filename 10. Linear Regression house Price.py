#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

USAhousing = pd.read_csv("USA_Housing.csv")
USAhousing.head()
USAhousing.describe()
sns.pairplot(USAhousing)
sns.distplot(USAhousing['Price'])
sns.heatmap(USAhousing.corr())
x=USAhousing[['Avg.Area Income', 'Avg.Area House Age', 'Avg.Area Number of Rooms', 'Avg.Area Number of Bedrooms', 'Area Population']]
y=USAhousing['Price']

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(x_train,y_train)

LinearRegression(copy_x=True,fit_intercept=True,n_jobs=1,normalize=False)
print(lm.intercept_)

coeff_df = pd.DataFrame(lm.coef_,x.columns,columns=['coefficient'])
coeff_df
predictions=lm.predict(x_test)
plt.scatter(y_test,predictions)


# In[ ]:




