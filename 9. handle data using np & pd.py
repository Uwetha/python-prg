#!/usr/bin/env python
# coding: utf-8

# In[14]:


from sklearn.datasets import load_boston
import numpy as np
import pandas as pd 
import seaborn as sns
from scipy import stats

#load data
x,y = load_boston(return_X_y = True)

#create data frame
boston = load_boston()
columns = boston.feature_names
df = pd.DataFrame(x,columns=columns)
df

#df.describe()
df_1 = df[['TAX','B']]
df_2 = df[['CRIM','ZN','INDUS','RM','AGE','DIS','RAD','PTRATIO','LSTAT']]
df_3 = df[['CHAS','NOX']]

ax = sns.boxplot(data = df_2, orient = "h" , palette = "Set2")
ax


# In[10]:


df


# In[ ]:




