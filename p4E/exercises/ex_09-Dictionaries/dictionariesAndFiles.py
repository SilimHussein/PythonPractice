fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
#outer loop reads the lines of the file
for line in fhand:
    words = line.rstrip()
    words = line.split()
    #the inner loop iterates through each of the words on that particular line.
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            
print(counts)