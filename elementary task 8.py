#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fib(low, high):
    n1 = 0
    n2 = 1 
    n3 = 1
    result = []
    while (n1 <= high):
        if (n1 >= low):
            result.append(n1)
        n1 = n2
        n2 = n3
        n3 = n1 + n2
    return result

if __name__ == "__main__":

    print(fib(50,1000000))

