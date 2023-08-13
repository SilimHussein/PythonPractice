fname = input('Enter file name:')
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for w in words:
        if w not in lst:
            lst.append(w)
lst.sort()
print(lst)