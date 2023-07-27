fname = input('Enter file:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('Cannot open file', fname)
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    timestamp = words[5]
    timestamplst = timestamp.split(':')
    hourslst = timestamplst[0].split()
    for hours in hourslst:
        counts[hours] = counts.get(hours, 0) + 1
    
#print(counts)
#key = hours, val = counts
lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()
#print(lst)
for key, val in lst:
    print(key,val)
