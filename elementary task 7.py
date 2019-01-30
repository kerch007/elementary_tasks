#!/usr/bin/env python
# coding: utf-8

# In[6]:


class square_of_number():
    def __init__(self, n):
        
        self.n = n
    def check(n):
        try:
            if (int(n) < 0):
                print('No.. Negative number entered. Please enter positive integer number')
            res = []
            for i in range(n):
                
                if i ** 2 < n:
                    res.append(i)
            return res
            
            
        except (ValueError,RuntimeError, TypeError, NameError):
            print("No.. String entered. Please enter positive integer number")

if __name__ == "__main__":

    print(square_of_number.check(1500))

