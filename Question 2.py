#!/usr/bin/env python
# coding: utf-8

# In[3]:


##Python Candidates -
#Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating is given in the
#comments of the code. Also you will have to print the following after validation in respective functions:-

#1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)

#2.Valid Triangle:If the triangle sum property of sides is valid.

#3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b

#4.Invalid Rectangle: If Not Valid rectangle as stated above.

#Input Format:

#The side length of triangle followed by for rectangle in the next line in order.

#Output Format:

#since object are created in order, so first validate info about triangle will come and than rectangle.

#Sample Input 0:

# 3 4 5

#2 4 2 4

#Sample Output 0:

#Valid Triangle

#Valid Rectangle


# In[4]:


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validate_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")


class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def validate_rectangle(self):
        if self.l == self.b:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")


a, b, c = map(int, input().split())
t = Triangle(a, b, c)
t.validate_triangle()

l1, b1, l2, b2 = map(int, input().split())
r = Rectangle(l1, b1)
r.validate_rectangle()


# In[ ]:




