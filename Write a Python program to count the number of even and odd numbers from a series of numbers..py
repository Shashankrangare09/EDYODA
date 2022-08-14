#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1 = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
total_odd = 0
total_even = 0
for i in list1:
        if(i % 2 == 0):
            total_even = total_even + 1
        else:
            total_odd = total_odd + 1
print("Total odd numbers :",total_odd)
print("Total even numbers :",total_even)

#Total odd numbers : 5
#Total even numbers : 4


# In[ ]:




