xfile = input('Enter file name: ')
try:
    fhandle = open(xfile)
except:
    print('no file with name', xfile)
    exit()
    
for line in fhandle:
    line = line.rstrip()
    uppercase_text = line.upper()
    print(uppercase_text)