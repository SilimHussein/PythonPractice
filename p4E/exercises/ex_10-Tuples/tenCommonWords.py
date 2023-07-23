fhand = open('romeo.txt')
counts = dict()
#reading a file, creating a dictionary of words and their counts from the file
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#creating a list of words in reverse order(value, key) from the dictionary
lst = list()
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

#sorting the list
lst = sorted(lst, reverse=True)

#printing the first ten items of the new list.
for val, key in lst[:10]:
    print(key, val)
    