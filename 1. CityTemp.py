#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
np.zeros(10)


# In[10]:


np.ones(10)


# In[11]:


np.ones(10)*5


# In[12]:


np.arange(10,51)


# In[13]:


np.arange(10,51,2)


# In[14]:


np.arange(9).reshape(3,3)


# In[15]:


np.eye(3)


# In[16]:


np.random.rand(1)


# In[17]:


np.random.randn(25)


# In[18]:


mat=np.arange(1,26).reshape(5,5)
mat


# In[19]:


mat.std()


# In[20]:


t=(1,2,3)
t


# In[21]:


len(t)


# In[22]:


t=('one',2)
t


# In[23]:


t[0]


# In[24]:


t[-1]


# In[25]:


x=set()
x


# In[26]:


set()


# In[27]:


x.add(1)
x


# In[28]:


x.add(2)
x


# In[29]:


x.add(1)
x


# In[30]:


list1=[1,1,2,2,3,4,5,6,1,1]
list1


# In[31]:


set(list1)


# In[1]:


loc = 'Bank'
if loc == 'Auto Shop':
    print('welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank:')
else:
    print('Where are you?')


# In[2]:


list1=[1,2,3,4,5,6,7,8,10]
for num in list1:
    print(num)


# In[3]:


for num in list1:
    if num%2 == 0:
        print(num)


# In[4]:


tup=(1,2,3,4,5)
for t in tup:
    print(t)


# In[5]:


list2=[(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)


# In[6]:


for letter in 'this is a string':
    print(letter)


# In[7]:


for(t1,t2) in list2:
    print(t1)


# In[8]:


d={'k1':3,'k2':1,'k3':2}
for item in d:
    print(item)
    d.items()
list(d.keys())
sorted(d.values())


# In[7]:


cityTemp = open("citytemp.csv")
rec1 = cityTemp.readline()
city, temperature, unit = rec1.split(',')
prev_city = city

cityTemp.seek(0)

tempSum = 0.0
count = 0
averageTemp = 0.0

for records in cityTemp:
    records = records.rstrip('\n')
    city, temperature, unit = records.split(',')
    
    if unit == "C":
        temperature = (float(temperature) * 9/5) + 32

    if city != prev_city:
        averageTemp = tempSum/count
        print(prev_city + "  " + str(round(averageTemp,2)))
        prev_city = city
        tempSum = 0.0
        count = 0
        averageTemp = 0.0
    tempSum = tempSum + float(temperature)
    count = count + 1
else:
    averageTemp = tempSum/count
    print(prev_city + "  " + str(round(averageTemp,2)))


# In[ ]:




