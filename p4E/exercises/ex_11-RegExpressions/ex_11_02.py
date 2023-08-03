import re
fname = input('Enter file name:')

if len(fname) < 1:
    fname = 'mbox.txt'

try:
    fhand = open(fname)
except:
    print('cannot open file:',fname)
    exit()
lst = []
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        lst.append(int(x[0]))
        
print(int(sum(lst)/len(lst)))