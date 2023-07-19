word = 'brontosauraus'
d = dict()
#for loop traverses the string, if c is not in dict, we create it, if it is, we increment
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] +1
print(d)