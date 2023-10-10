#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

f=pd.read_csv('03 - corr.csv')

f['t0'] = pd.to_numeric(f['t0'], downcast = 'float')

plt.acorr(f['t0'],maxlags=10)

t_1 = f['t0'].shift(1).to_frame()
t_1.columns = ['t_1']

t_2 = f['t0'].shift(2).to_frame()
t_2.columns = ['t_2']

result=pd.concat([f['t0'], t_1,t_2], axis = 1)
result


# In[ ]:





# In[ ]:




