
def square(numbers):
    try:
        numbers[1], numbers[2], numbers[3] = float(numbers[1]), float(numbers[2]), float(numbers[3])
        p = (numbers[1] + numbers[2] + numbers[3]) / 2
        s = (p * (p - numbers[1]) * (p - numbers[2]) * (p - numbers[3])) ** 0.5
        return(f'{numbers[0]}:' ,round(s,2))
    except ValueError:
        print("No.. String entered. Please enter positive number")
a = []

while True:
    inp = input('Please enter specifications of triangle in format: <name>, <side length>, <side length>, <side length> \n').split(",")
    a.append(inp)
    try_again = input("Would you like enter one more triangle data? ").lower()
    if try_again.lower() != "y":
        if try_again.lower() != "yes": break
    
computation = []
try:
    for i in range(len(a)):
        computation.append(square(a[i]))     
    computation = sorted(computation, key=lambda tup:(-tup[1], tup[0]))
    computation = [list(t) for t in computation]
    for i in range(len(computation)):
        computation[i][1] = str(computation[i][1])+(' cm2')
except:
    print('Please eneter correct data')
else:
    print ('============= Triangles list: ===============')
    for i in computation:
        print(f'{i}')    

