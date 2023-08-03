import re
fname = input('Enter file:')
if len(fname) < 1:
    fname = 'regex_sum_1737618.txt'
try:
    fhand = open(fname)
except:
    print('Cannot open file', fname)
    exit()

lst = []
for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        #print(x)
        for num in x:
            #lst.append(int(x[0]))
            lst.append(int(num))
#print(lst)
print(sum(lst))