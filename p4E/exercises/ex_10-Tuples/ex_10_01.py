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
    #print(words)
    emails = words[1].split()
    #print(emails)
    for email in emails:
        counts[email] = counts.get(email, 0) + 1

#print(counts)

#creating a list of words in reverse order(value, key) from the dictionary
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

#sorting the email and count list in reverse order i.e the most emails first
lst.sort(reverse = True)

#printing the emails and counts 
for val, key in lst:
    print(key, val)