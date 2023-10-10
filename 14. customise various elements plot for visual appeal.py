#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt

f=open('salesdata2.csv','r')
salefile = f.readlines()

sale_list=[]
s_list=[]
c_list=[]
    
for records in salefile:
    sale,cost=records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))

sale_list.append(s_list)
sale_list.append(c_list)

plt.subplot(2,2,1)
plt.title("sales vs cost")
plt.xlabel("sale")
plt.ylabel("cost")
plt.scatter(s_list,c_list)

plt.scatter(s_list,c_list,marker='x',s=100, c='#FF5733')

plt.subplot(2,3,2)
plt.title("Box plot of sales")
plt.ylabel("USD")
plt.boxplot(sale_list,
            patch_artist=True,
            boxprops=dict(facecolor='g',color='r',linewidth=2),
            whiskerprops=dict(color='r',linewidth=2),
            medianprops = dict(color='w',linewidth=1),
            capprops = dict(color='k',linewidth=2),
            flierprops=dict(markerfacecolor='r',marker='o',markersize=7))

plt.subplot(2,3,3)
plt.title("Histogram of sales")
plt.ylabel("USD")
plt.hist(s_list, bins=5, rwidth=0.9, color='c')

x_day = [1,2,3,4,5]
y_price = [9,9.5,10.1,10,12]
plt.subplot(2,2,4)
plt.title("stockprice history")
plt.xlabel("Price")
plt.ylabel("Day")
plt.scatter(x_day,y_price,color='green',marker='o',linewidth=3,linestyle='--')

x_cities = ['NewYork','London','Dubai','New Delhi','Tokyo']
y_temp = [75,65,105,98,90]
plt.subplot(2,3,5)
plt.title("Temperature variation")
plt.xlabel("cities")
plt.ylabel("temperature")
plt.xticks(rotation='45')
plt.bar(x_cities,y_temp,color = ['r','g','c','y','m'])

plt.tight_layout()

plt.show()


# In[ ]:




