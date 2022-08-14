#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Enter any number                                               #0,1,1,2,3,5....
num=int(input("Enter the number for Fibonacci series"))          # im entering num= 10
a=0                                         #first element of series
b=1                                         #second element of series
if num<=0:
    print("The requested series is",f)
else:
    print(a,b,end=" ")
    for i in range(2,num):
        next=a+b                           
        print(next,end=" ")
        a=b
        b=next

# my output is 0 1 1 2 3 5 8 13 21 34


# In[ ]:





# In[ ]:





# In[ ]:




