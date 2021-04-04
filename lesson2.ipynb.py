#!/usr/bin/env python
# coding: utf-8

# Задание 1

# In[2]:


from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))
c100 = combinations(100,85)
c100


# In[3]:


pk = 0.8 ** 85
pk


# In[4]:


q = 1 - 0.8
qnk = q ** (100 - 85)
qnk


# In[5]:


p = c100 * pk * qnk
p


# Задание 2

# In[9]:


l = 5000 * 0.0004
l


# In[12]:


from math import factorial, exp
p = (l ** 0) * exp(-l) / factorial(0)
p


# In[13]:


from math import factorial, exp
p = (l ** 2) * exp(-l) / factorial(2)
p


# Задание 3

# In[14]:


from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))
c144 = combinations(144,70)
c144


# In[15]:


pk = 0.5 ** 70
pk


# In[16]:


q = 1 - 0.5
qnk = q ** (144 - 70)
qnk


# In[17]:


p = c144 * pk * qnk
p


# Задание 4

# Все белые

# In[7]:


p = combinations(7,2) / combinations(10,2) * combinations(9,2) / combinations(11,2)
p


# Два мяча белые

# In[6]:


p1 = combinations(7,2) / combinations(10,2) * combinations(2,2) / combinations(11,2)
p2 = (combinations(7,1) * combinations(3,1) / combinations(10,2)) * (combinations(9,1) * combinations(2,1) / combinations(11,2))
p3 = combinations(3,2) / combinations(10,2) * combinations(9,2) / combinations(11,2)
print(p1+p2+p3)


# Хотя бы один белый

# In[10]:


p = 1 - (combinations(3,2) / combinations(10,2) * combinations(2,2) / combinations(11, 2))
p


# In[ ]:




