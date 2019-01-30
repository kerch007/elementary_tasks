#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Chess_desk():

  def __init__(self, horizont, vertical):
    
    self.horizont = horizont
    self.vertical = vertical
    
  def print_stars(self):
    try:
        
            
        if int(self.horizont) > 0 and int(self.vertical) > 0:
            for i in range(self.horizont):
                if (i % 2 == 0):
                    print('* ' * self.vertical)
                else:
                    print(' *' * self.vertical)
        
        if (self.horizont <=0) or (self.vertical <=0):
            print("Positive numbers only please.")
      
    except ValueError:
        print("No.. String entered. Please enter positive integer number")
    
if __name__ == "__main__":
    chess_desk = Chess_desk(1,6)
    chess_desk.print_stars()
    print()


