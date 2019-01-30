#!/usr/bin/env python
# coding: utf-8

# In[30]:


def lucky_ticket(a):
    b = a//1000
    one = b // 100
    two = b // 10 % 10    
    three = b % 10
    c = a % 1000
    four = c // 100
    five = c // 10 % 10
    six = c % 10
    if algoritm == 3:  
        if (two+four+six)==(one+three+five):
            return (1)
        else:
            return (0)
    if algoritm == 1:
        if (one+two+three)==(four+five+six):
            return (1)
        else:
            return (0)
    if algoritm ==2:
        even = 0
        odd = 0
        for x in (one, two, three, four, five, six):
            if x % 2 == 0: 
                even = even+x
            else:
                odd = odd+x
        if even == odd:
            return(1)
        else:
            return(0)


try:
    filepath = input("Please enter file path: \n")
    file = open(filepath, 'r')
    text = file.read().strip()
    file.close()


    data = list(map(int, text.split(',')))
    algoritm = data[2]
    
    range_of_tickets =  [i for i in range(data[0],data[1])]
    print ()

    print('Range of tickets',data[0:2], 'Method: ', data[2])
    print('The number of "happy" tickets calculated by this method = ',sum(list(map(lucky_ticket, range_of_tickets))))

except IOError:
    print ("Error: File does not appear to exist.")

