
import re
    
method = int(input('Please chose method:\n 1 - Count the number of line entries in a text file.\n 2 - Replace a string with another in the specified file.\n'))

if method == 1:
    try:
        filepath = input("Please enter file path: \n")
        with open(filepath, 'r+') as file:
            text = file.read()
        file.close()
        stringa = input("Please enter string for counting: \n")
        rePages = re.compile(stringa)
        tmp = rePages.findall(text)
        print ('Number of entries:',len(tmp))
    except IOError:
        print ("Error: File does not appear to exist. \n")
    
if method == 2:
    try:
        filepath = input("Please enter file path: \n")
        with open (filepath, 'r') as file:
            text = file.read()
        file.close()
        stringa_find = input("Please enter text which need to replace: \n")
        stringa_change = input("Please enter text for replacement: \n")
        new_data = text.replace(stringa_find, stringa_change)
        with open (filepath, 'w') as file:
            file.write(new_data)
        print('Strings replaced...')
    
    except IOError:
        print ("Error: File does not appear to exist.")

