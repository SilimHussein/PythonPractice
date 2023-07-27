import string
fname = input('Enter file name : ')
try:
    fhand = open(fname)
except:
    print('cannot open file:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.whitespace))
    print(line)
    #words = line.split()
    #letters = words.split()
    #print(letters)
"""
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)
"""
