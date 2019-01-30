
while True:
    try:
        a = float(input('Please enter side a of first envelope \n '))
        if a <=0:
            a=float(input("Side can't be negative, please try again: \n"))
            
        b = float(input('Please enter side b of first envelope \n'))
        if b <=0:
            b=float(input("Side can't be negative, please try again: \n"))
        
        c = float(input('Please enter side c of second envelope \n'))
        if c <=0:
            c=float(input("Side can't be negative, please try again: \n"))
        
        d = float(input('Please enter side d of second envelope \n'))
        if  d <= 0:
            d=float(input("Side can't be negative, please try again: \n"))
    
        if((a<c)and(b<d))or((a<d)and(b<c)) or ((c<a)and(d<b))or((c<b)and(d<a)):
            print ("Yes, first envelope can be put into second envelope \n")
        else:
            print("No, first envelope can not be put into second envelope \n")
    
    except (ValueError):
        print ("This is not a number! \n")
    
    try_again = input("Try Again? ").lower()
    if try_again.lower() != "y":
        if try_again.lower() != "yes":
              break 

