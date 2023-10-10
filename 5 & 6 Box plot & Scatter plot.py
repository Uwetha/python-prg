#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Pyplot
import matplotlib.pyplot as plt

#Open the file in read mode and read lines
f=open('salesdata.csv', 'r')
salefile = f.readlines()

#Create the sales list
sale_list=[]

#Append all the records from the file to the sales list
for records in salefile:
    sale_list.append(int(records))
    
#Change the chart labels
plt.title("Box plot of sales")

#Create the Plot
plt.boxplot(sale_list)

#Show the Plot
plt.show()


# In[1]:


#Import Pyplot
import matplotlib.pyplot as plt

#Open the file in read mode and read lines
f=open('salesdata2.csv', 'r')
salefile = f.readlines()

#Create the sales list
s_list=[]
c_list=[]

#Append all the records from the file to the sales list
for records in salefile:
    sale,cost=records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))
    
#Change the chart labels
plt.title("Sales vs Cost")
plt.xlabel("Sales")
plt.ylabel("Cost")

#Create the Plot
plt.scatter(s_list,c_list)

#Show the Plot
plt.show()


# In[ ]:




                                                                                                                                                                           

