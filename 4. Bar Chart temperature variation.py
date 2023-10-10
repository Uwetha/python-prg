#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 

#Create a list of cities and temperatures
x_cities = ['New York', 'London', 'Dubai', 'New Delhi', 'Tokyo']
y_temp = [75,65,105,98,90]

#Change the chart labels
plt.title("Temperature Variation")
plt.xlabel("Cities")
plt.ylabel("Temperature")

#Create the Bar Chart
plt.bar(x_cities, y_temp)

#Show the plot
plt.show()


# In[ ]:




