word = 'brontosaurus'
d = dict()
for c in word:
    #this idiom is the same as the four lines, if statement 
    """
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
    """

    d[c] = d.get(c,0) + 1
print(d)