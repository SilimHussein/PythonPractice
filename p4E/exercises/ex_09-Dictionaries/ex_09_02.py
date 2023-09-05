fname = input('Enter file name :')
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
    #print("debug, a list of lines that start with from:", words)
    days = words[2].split()
    #print("debug, value at index[2] are the days:",days)
    for day in days:
        counts[day] = counts.get(day, 0) + 1

print(counts)
