#!/usr/bin/env python
# coding: utf-8

# In[2]:


rows = int(input ("Enter the Number of rows:"))
columns = int(input ("Enter the Number of Columns:"))

print("Enter the Element of First Matrix:")
matrix_a=[[int(input()) for i in range (columns)] for i in range(rows)]
print("First matrix is :")
for n in matrix_a :
    print(n)
    
print("Enter the Element of Second Matrix:")
matrix_b=[[int(input()) for i in range (columns)] for i in range(rows)]
print("Second matrix is :")
for n in matrix_b :
    print(n)
result=[[0 for i in range(columns)] for i in range(rows)]
for i in range(rows):
    for j in range(columns):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]
        print("The Sum of Above two matrices is:")
        for r in result:
            print(r)


# In[ ]:




