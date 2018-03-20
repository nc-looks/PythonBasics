
# coding: utf-8

# In[3]:


# import python library into script
import numpy as np


# In[98]:


# ways to create arrays
a = np.array([1,2,3])
b = np.array([(1,2,3), (3,5,6)])
c = np.array([(4,5,6.3), (7,8,9)], dtype = float)
d = np.array([[1,3,4], [5,2,5]], dtype = int)


# creating an array of 0's and 1's 
e = np.zeros((3,4), dtype = int)
f = np.ones((1,2), dtype = int)

# creating an array of evenly spaced values 
## the first number specifies starting value, second value ending, and third step size 
g = np.arange(10,20,2)

## the first number specified starting value, second value ending, and third the number of samples
h = np.linspace(2,5,10)


# create a constant array
## first number is rows, second is columns, and third is the constant
i = np.full((2,3), 7)

# create a matrix of 1's and 0's alternating 
j = np.eye(5)

# create a random array 
## first number is rows, second is columns

k = np.random.random((2,3))

## random integers. first number is up to, second is number of samples
l = np.random.randint(3, size = 10)


# In[103]:


# how to learn about your array
#c.shape

print()


# In[ ]:


# perform basic arithmetic operations


# In[10]:


# aggregate functions


# In[11]:


# copy array


# In[12]:


# sort array

