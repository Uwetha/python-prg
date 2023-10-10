#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Pyplot
import matplotlib.pyplot as plt

#Open the file in read mode and read lines
f=open('salesdata2.csv', 'r')
salefile = f.readlines()

#Create the sales list
sale_list=[]
s_list=[]
c_list=[]

#Append all the records from the file to the sales list
for records in salefile:
    sale,cost=records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))

#Create a list of lists
sale_list.append(s_list)
sale_list.append(c_list)

#Plot the scatter plot
plt.figure('My scatter plot')
plt.title("sales vs cost")
plt.xlabel("sale")
plt.ylabel("cost")
plt.scatter(s_list,c_list)
plt.savefig('01Scatter.png')

#plot the boxplot
plt.figure('My Boxplot')
plt.title("Box plot of sales")
plt.ylabel("USD")
plt.boxplot(sale_list)
plt.savefig('01boxplot.png')

#Show the Plot
plt.show()


# In[3]:


#Import Pyplot
import matplotlib.pyplot as plt

#Open the file in read mode and read lines
f=open('salesdata2.csv', 'r')
salefile = f.readlines()

#Create the sales list
sale_list=[]
s_list=[]
c_list=[]

#Append all the records from the file to the sales list
for records in salefile:
    sale,cost=records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))

#Create a list of lists
sale_list.append(s_list)
sale_list.append(c_list)

#Plot 1 for scatter plot
plt.subplot(2,2,1)
plt.title("sales vs cost")
plt.xlabel("sale")
plt.ylabel("cost")
plt.scatter(s_list,c_list)

#plot 2 for boxplot
plt.subplot(2,2,2)
plt.title("Box plot of sales")
plt.ylabel("USD")
plt.boxplot(sale_list)

#subplot 3 for boxplot
plt.subplot(2,2,3)
plt.title("Histogram of sales")
plt.ylabel("USD")
plt.hist(s_list, bins=5, rwidth=0.9)

#Subplot 4 for scatter plot
x_day = [1,2,3,4,5]
y_price = [9,9.5,10.1,10,12]
plt.subplot(2,2,4)
plt.title("stockprice history")
plt.xlabel("Price")
plt.ylabel("Day")
plt.scatter(x_day,y_price)

#tight_layout to void overlap
plt.tight_layout()

#save the figure as png picture filled
plt.savefig('01Subplot.png')

#Show the Plot
plt.show()


# In[ ]:




