fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('Cannot open file:',fname)
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1].split()
    #print(email)
    for sender in email:
        counts[sender] = counts.get(sender, 0) + 1
    
print(counts)