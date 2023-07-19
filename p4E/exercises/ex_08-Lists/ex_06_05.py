fname = input('Enter the name of the file: ')
count = 0
try:
    fhand = open(fname)
except:
    print('No such file')
    exit()
    
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[1])
    count = count + 1

print('There were',count, 'lines in the file with From as the first word')