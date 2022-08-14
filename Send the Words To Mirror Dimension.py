#!/usr/bin/env python
# coding: utf-8

# #Write a Python program that accepts a word from the user and reverse it.

# In[3]:


word = input("Input a word to reverse: ")     # I entered the word Edyoda
 
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n")

#my output is adoydE


# In[ ]:




